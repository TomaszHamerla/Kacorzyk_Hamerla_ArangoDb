import subprocess
import time
from arango import ArangoClient

print("Uruchamianie bazy ArangoDB z docker-compose...")
subprocess.run(["docker-compose", "up", "-d"], check=True)

print("Czekam 5 sekund na start serwera...")
time.sleep(5)

client = ArangoClient(hosts='http://localhost:8529')
sys_db = client.db('_system', username='root', password='root')

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

print("Infrastruktura gotowa! Czas na magię AQL w przeglądarce.")