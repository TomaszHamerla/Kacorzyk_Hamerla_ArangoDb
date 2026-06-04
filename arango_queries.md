# ArangoDB AQL Queries


## 1. CREATE

### 1.1 Dodanie użytkowników (Vertices)
```aql
LET users_data = [
  { _key: "u1", name: "Jan", surname: "Kowalski", age: 30 },
  { _key: "u2", name: "Anna", surname: "Nowak", age: 25 },
  { _key: "u3", name: "Piotr", surname: "Wiśniewski", age: 40 },
  { _key: "u4", name: "Katarzyna", surname: "Wójcik", age: 22 },
  { _key: "u5", name: "Michał", surname: "Kamiński", age: 35 },
  { _key: "u6", name: "Agnieszka", surname: "Lewandowska", age: 28 },
  { _key: "u7", name: "Tomasz", surname: "Zieliński", age: 45 },
  { _key: "u8", name: "Magdalena", surname: "Szymańska", age: 31 },
  { _key: "u9", name: "Krzysztof", surname: "Dąbrowski", age: 50 },
  { _key: "u10", name: "Maja", surname: "Kozłowska", age: 27 }
]
FOR u IN users_data
  INSERT u INTO users
```

#### (Dodawanie pojedyncze)
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
LET movies_data = [
  { _key: "m1", title: "Incepcja", year: 2010, genre: "Sci-Fi" },
  { _key: "m2", title: "Matrix", year: 1999, genre: "Sci-Fi" },
  { _key: "m3", title: "Avatar", year: 2009, genre: "Fantasy" },
  { _key: "m4", title: "Interstellar", year: 2014, genre: "Sci-Fi" },
  { _key: "m5", title: "Joker", year: 2019, genre: "Drama" },
  { _key: "m6", title: "Gladiator", year: 2000, genre: "Action" },
  { _key: "m7", title: "Titanic", year: 1997, genre: "Romance" },
  { _key: "m8", title: "The Dark Knight", year: 2008, genre: "Action" },
  { _key: "m9", title: "Forrest Gump", year: 1994, genre: "Drama" },
  { _key: "m10", title: "The Lord of the Rings", year: 2001, genre: "Fantasy" },
  { _key: "m11", title: "Fight Club", year: 1999, genre: "Drama" },
  { _key: "m12", title: "Pulp Fiction", year: 1994, genre: "Crime" },
  { _key: "m13", title: "The Shawshank Redemption", year: 1994, genre: "Drama" },
  { _key: "m14", title: "The Godfather", year: 1972, genre: "Crime" },
  { _key: "m15", title: "Se7en", year: 1995, genre: "Crime" }
]
FOR m IN movies_data
  INSERT m INTO movies
```

#### (Dodawanie pojedyncze)
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
LET watched_data = [
  { _from: "users/u1", _to: "movies/m1", rating: 5, watchDate: "2023-10-01" },
  { _from: "users/u1", _to: "movies/m2", rating: 4, watchDate: "2023-10-05" },
  { _from: "users/u1", _to: "movies/m4", rating: 5, watchDate: "2023-10-12" },
  { _from: "users/u2", _to: "movies/m1", rating: 5, watchDate: "2023-10-10" },
  { _from: "users/u2", _to: "movies/m3", rating: 4, watchDate: "2023-10-14" },
  { _from: "users/u2", _to: "movies/m5", rating: 5, watchDate: "2023-10-20" },
  { _from: "users/u3", _to: "movies/m3", rating: 3, watchDate: "2023-10-15" },
  { _from: "users/u3", _to: "movies/m6", rating: 4, watchDate: "2023-10-18" },
  { _from: "users/u3", _to: "movies/m7", rating: 2, watchDate: "2023-10-22" },
  { _from: "users/u4", _to: "movies/m8", rating: 5, watchDate: "2023-10-02" },
  { _from: "users/u4", _to: "movies/m9", rating: 4, watchDate: "2023-10-08" },
  { _from: "users/u5", _to: "movies/m10", rating: 5, watchDate: "2023-10-11" },
  { _from: "users/u5", _to: "movies/m11", rating: 4, watchDate: "2023-10-15" },
  { _from: "users/u5", _to: "movies/m12", rating: 5, watchDate: "2023-10-25" },
  { _from: "users/u5", _to: "movies/m5", rating: 3, watchDate: "2023-10-28" },
  { _from: "users/u5", _to: "movies/m6", rating: 4, watchDate: "2023-10-30" },
  { _from: "users/u6", _to: "movies/m1", rating: 4, watchDate: "2023-11-01" },
  { _from: "users/u6", _to: "movies/m13", rating: 5, watchDate: "2023-11-05" },
  { _from: "users/u6", _to: "movies/m14", rating: 5, watchDate: "2023-11-10" },
  { _from: "users/u7", _to: "movies/m15", rating: 4, watchDate: "2023-11-12" },
  { _from: "users/u7", _to: "movies/m2", rating: 3, watchDate: "2023-11-15" },
  { _from: "users/u8", _to: "movies/m4", rating: 5, watchDate: "2023-11-18" },
  { _from: "users/u8", _to: "movies/m7", rating: 4, watchDate: "2023-11-20" },
  { _from: "users/u9", _to: "movies/m8", rating: 5, watchDate: "2023-11-22" },
  { _from: "users/u9", _to: "movies/m9", rating: 5, watchDate: "2023-11-25" },
  { _from: "users/u10", _to: "movies/m10", rating: 4, watchDate: "2023-11-28" },
  { _from: "users/u10", _to: "movies/m12", rating: 5, watchDate: "2023-11-30" },
  { _from: "users/u10", _to: "movies/m1", rating: 3, watchDate: "2023-12-02" },
  { _from: "users/u6", _to: "movies/m2", rating: 4, watchDate: "2023-12-05" },
  { _from: "users/u7", _to: "movies/m10", rating: 5, watchDate: "2023-12-08" }
]
FOR w IN watched_data
  INSERT w INTO watched
```
#### (Dodawanie pojedyncze)
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

## 2. READ

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

## 3. UPDATE

### 3.1 Zmiana wieku użytkownika
```aql
UPDATE "u5" WITH { age: 32 } IN users
```

### 3.2 Zmiana oceny w relacji watched
```aql
FOR w IN watched
  FILTER w._from == "users/u5" AND w._to == "movies/m5"
  UPDATE w WITH { rating: 4 } IN watched
```

## 4. DELETE

### 4.1 Usunięcie krawędzi (relacji obejrzenia)
```aql
FOR w IN watched
  FILTER w._from == "users/u5" AND w._to == "movies/m6"
  REMOVE w IN watched
```

### 4.2 Usunięcie filmu
```aql
REMOVE "m15" IN movies
```

### 4.3 Kaskadowe usunięcie użytkownika (Usuwanie powiązanych krawędzi)
```aql
LET userId = "users/u5"

FOR w IN watched
    FILTER w._from == userId
    REMOVE w IN watched

REMOVE "u5" IN users
```

## 5. ZAPYTANIA GRAFOWE

### 5.1 Graf: Filmy obejrzane przez użytkownika u5
```aql
FOR v, e, p IN 1..1 OUTBOUND "users/u5" GRAPH "StreamingGraph"
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

### 5.4 Graf: Użytkownicy, którzy obejrzeli ten sam film co użytkownik u5 (Współwidzowie)
Zapytanie to szuka wierzchołków znajdujących się dokładnie 2 kroki od `u5` w dowolnym kierunku (ANY), upewniając się, że znaleziony węzeł należy do kolekcji `users`. Ponieważ ścieżka wygląda tak: `user -> movie <- user`, używamy `ANY`.
```aql
FOR v, e, p IN 2..2 ANY "users/u5" GRAPH "StreamingGraph"
  FILTER IS_SAME_COLLECTION("users", v)
  RETURN DISTINCT {
    userName: v.name,
    userSurname: v.surname
  }
```

### 5.5 Graf: Rekomendacja filmów dla użytkownika u6
Pobiera filmy obejrzane przez użytkowników o podobnym guście (takich, którzy widzieli te same filmy co `u6`), z pominięciem filmów, które `u6` już obejrzał.
```aql
FOR v, e, p IN 3..3 ANY "users/u6" GRAPH "StreamingGraph"
  FILTER IS_SAME_COLLECTION("movies", v)
  // Ignorujemy filmy już obejrzane przez u6
  FILTER v._id NOT IN (
    FOR v2 IN 1..1 OUTBOUND "users/u6" GRAPH "StreamingGraph" RETURN v2._id
  )
  RETURN DISTINCT {
    recommendedMovie: v.title,
    genre: v.genre
  }
```

### 5.6 Graf: Najkrótsza ścieżka (Shortest Path) pomiędzy dwoma użytkownikami
Zwraca najkrótszą ścieżkę powiązań między dwoma użytkownikami w grafie (np. przez wspólne filmy), ignorując kierunek krawędzi (ANY).
```aql
FOR v IN ANY SHORTEST_PATH "users/u5" TO "users/u7" GRAPH "StreamingGraph"
  RETURN v._id
```