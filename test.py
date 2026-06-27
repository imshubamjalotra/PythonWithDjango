import sqlite3
import json
from pathlib import Path

base_dir = Path(__file__).resolve().parent
movies_path = base_dir / "movies.json"
movies = json.loads(movies_path.read_text())
# movies = json.loads(movies)


def ConnectToDatabase():
    with sqlite3.connect("movies1.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                year INTEGER NOT NULL
                
            )
            """
        )

        for movie in movies:
            cursor.execute(
                "INSERT INTO movies (title, year) VALUES (?, ?)",
                (movie["title"], movie["year"]),
            )
    print("Creating database and table...", movies)


ConnectToDatabase()


def ReadFromDatabase():
    with sqlite3.connect("movies1.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies")
        rows = cursor.fetchall()
        for row in rows:
            print(row)


ReadFromDatabase()
