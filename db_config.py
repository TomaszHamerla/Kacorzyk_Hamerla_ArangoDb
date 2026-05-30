import subprocess
import time
from arango import ArangoClient

print("Uruchamianie bazy ArangoDB z docker-compose...")
subprocess.run(["docker", "compose", "up", "-d"], check=True)

print("Czekam na pełne uruchomienie serwera ArangoDB", end="")
client = ArangoClient(hosts='http://localhost:8529')
sys_db = None

# Pętla czekająca na gotowość bazy danych (maksymalnie 30 prób)
for i in range(30):
    try:
        sys_db = client.db('_system', username='root', password='root')
        # Próba wykonania prostej operacji, aby upewnić się, że baza odpowiada
        sys_db.has_database("streaming_db")
        print("\n Połączono pomyślnie!")
        break
    except Exception:
        print(".", end="", flush=True)
        time.sleep(1)

if sys_db is None:
    print("\n[BŁĄD] Nie udało się połączyć z ArangoDB w ciągu 30 sekund.")
    exit(1)

# Reset bazy
if sys_db.has_database("streaming_db"):
    print("Resetowanie środowiska (usuwam starą bazę)...")
    sys_db.delete_database("streaming_db")

print("Tworzę nową, czystą bazę 'streaming_db'...")
sys_db.create_database("streaming_db")
db = client.db("streaming_db", username="root", password="root")

print("Tworzenie pustych kolekcji i definicji grafu...")
streaming_graph = db.create_graph("StreamingGraph")
users = streaming_graph.create_vertex_collection("users")
movies = streaming_graph.create_vertex_collection("movies")
watched = streaming_graph.create_edge_definition(
    edge_collection="watched",
    from_vertex_collections=["users"],
    to_vertex_collections=["movies"]
)

print("Infrastruktura gotowa => http://localhost:8529")