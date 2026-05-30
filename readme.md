# Konfiguracja Środowiska i Uruchomienie ArangoDB

Projekt zawiera skrypt automatyzujący uruchamianie bazy danych ArangoDB w kontenerze Docker oraz konfigurację struktury grafowej dla aplikacji streamingowej.

## 📋 Wymagania wstępne
Przed uruchomieniem upewnij się, że na Twoim komputerze są zainstalowane i włączone:
1. **Python 3** (wraz z menedżerem pakietów `pip`)
2. **Docker Desktop** (usługa Docker musi być uruchomiona w tle)

---

## 🚀 Instrukcja krok po kroku

### Krok 1: Instalacja biblioteki `python-arango`
Aby Python mógł komunikować się z bazą danych ArangoDB, musisz zainstalować oficjalnego klienta. Otwórz terminal (np. PowerShell) w folderze projektu i wykonaj poniższe polecenie:

```powershell
py -m pip install python-arango
```

### Krok 2: Uruchomienie skryptu inicjalizacyjnego
Upewnij się, że program Docker Desktop działa w tle. Następnie w terminalu wpisz poniższą komendę, aby odpalić skrypt:

```powershell
py .\db_config.py
```



