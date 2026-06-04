# ArangoDB AQL Queries

Poniżej znajduje się zestawienie kilkunastu zapytań w języku AQL (ArangoDB Query Language) operujących na bazie `streaming_db`, kolekcjach wierzchołków `users` i `movies`, kolekcji krawędzi `watched` oraz grafie `StreamingGraph`.

## 1. CREATE (Dodawanie danych)

### 1.1 Dodanie użytkowników (Vertices)
```aql
INSERT { _key: "u1", name: "Jan", surname: "Kowalski", age: 30 } INTO users
```
```aql
INSERT { _key: "u2", name: "Anna", surname: "Nowak", age: 25 } INTO users
```
```aql
INSERT { _key: "u3", name: "Piotr", surname: "Wiśniewski", age: 40 } INTO users
```

### 1.2 Dodanie filmów (Vertices)
```aql
INSERT { _key: "m1", title: "Incepcja", year: 2010, genre: "Sci-Fi" } INTO movies
```
```aql
INSERT { _key: "m2", title: "Matrix", year: 1999, genre: "Sci-Fi" } INTO movies
```
```aql
INSERT { _key: "m3", title: "Avatar", year: 2009, genre: "Fantasy" } INTO movies
```

### 1.3 Dodanie relacji obejrzenia filmu (Edges)
```aql
INSERT { _from: "users/u1", _to: "movies/m1", rating: 5, watchDate: "2023-10-01" } INTO watched
```
```aql
INSERT { _from: "users/u1", _to: "movies/m2", rating: 4, watchDate: "2023-10-05" } INTO watched
```
```aql
INSERT { _from: "users/u2", _to: "movies/m1", rating: 5, watchDate: "2023-10-10" } INTO watched
```
```aql
INSERT { _from: "users/u3", _to: "movies/m3", rating: 3, watchDate: "2023-10-15" } INTO watched
```

## 2. READ (Pobieranie danych)

### 2.1 Pobranie wszystkich użytkowników
```aql
FOR u IN users
  RETURN u
```

### 2.2 Pobranie filmów Sci-Fi posortowanych od najnowszego
```aql
FOR m IN movies
  FILTER m.genre == "Sci-Fi"
  SORT m.year DESC
  RETURN m
```

### 2.3 Pobranie konkretnego użytkownika po kluczu
```aql
RETURN DOCUMENT("users/u1")
```

## 3. UPDATE / REPLACE (Modyfikacja danych)

### 3.1 Zmiana wieku użytkownika
```aql
UPDATE "u1" WITH { age: 31 } IN users
```

### 3.2 Zmiana oceny w relacji watched
```aql
FOR w IN watched
  FILTER w._from == "users/u3" AND w._to == "movies/m3"
  UPDATE w WITH { rating: 4 } IN watched
```

## 4. DELETE (Usuwanie danych)

### 4.1 Usunięcie krawędzi (relacji obejrzenia)
```aql
FOR w IN watched
  FILTER w._from == "users/u1" AND w._to == "movies/m2"
  REMOVE w IN watched
```

### 4.2 Usunięcie filmu
```aql
REMOVE "m2" IN movies
```

## 5. ZAPYTANIA GRAFOWE I BARDZIEJ ZŁOŻONE

### 5.1 Graf: Filmy obejrzane przez użytkownika u1
```aql
FOR v, e, p IN 1..1 OUTBOUND "users/u1" GRAPH "StreamingGraph"
  RETURN {
    movieTitle: v.title,
    rating: e.rating,
    watchDate: e.watchDate
  }
```

### 5.2 Agregacja: Najpopularniejsze filmy (liczba obejrzeń)
```aql
FOR w IN watched
  COLLECT movieId = w._to WITH COUNT INTO watchCount
  SORT watchCount DESC
  LET movie = DOCUMENT(movieId)
  RETURN {
    title: movie.title,
    views: watchCount
  }
```

### 5.3 Złączenie (JOIN-like): Użytkownicy, którzy ocenili film na 5 gwiazdek
```aql
FOR w IN watched
  FILTER w.rating == 5
  LET u = DOCUMENT(w._from)
  LET m = DOCUMENT(w._to)
  RETURN {
    userName: CONCAT(u.name, " ", u.surname),
    movieTitle: m.title,
    rating: w.rating
  }
```

### 5.4 Graf: Użytkownicy, którzy obejrzeli ten sam film co użytkownik u1 (Współwidzowie)
Zapytanie to szuka wierzchołków znajdujących się dokładnie 2 kroki od `u1` w dowolnym kierunku (ANY), upewniając się, że znaleziony węzeł należy do kolekcji `users`. Ponieważ ścieżka wygląda tak: `user -> movie <- user`, używamy `ANY`.
```aql
FOR v, e, p IN 2..2 ANY "users/u1" GRAPH "StreamingGraph"
  FILTER IS_SAME_COLLECTION("users", v)
  RETURN DISTINCT {
    userName: v.name,
    userSurname: v.surname
  }
```

### 5.5 Graf: Rekomendacja filmów dla użytkownika u2
Pobiera filmy obejrzane przez użytkowników o podobnym guście (takich, którzy widzieli te same filmy co `u2`), z pominięciem filmów, które `u2` już obejrzał.
```aql
FOR v, e, p IN 3..3 ANY "users/u2" GRAPH "StreamingGraph"
  FILTER IS_SAME_COLLECTION("movies", v)
  // Ignorujemy filmy już obejrzane przez u2
  FILTER v._id NOT IN (
    FOR v2 IN 1..1 OUTBOUND "users/u2" GRAPH "StreamingGraph" RETURN v2._id
  )
  RETURN DISTINCT {
    recommendedMovie: v.title,
    genre: v.genre
  }
```

### 5.6 Graf: Najkrótsza ścieżka (Shortest Path) pomiędzy dwoma użytkownikami
Zwraca najkrótszą ścieżkę powiązań między dwoma użytkownikami w grafie (np. przez wspólne filmy), ignorując kierunek krawędzi (ANY).
```aql
FOR v IN ANY SHORTEST_PATH "users/u1" TO "users/u2" GRAPH "StreamingGraph"
  RETURN v._id
```