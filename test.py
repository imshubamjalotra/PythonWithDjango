import sqlite3
import json
from pathlib import Path
movies = (Path("movies.json").read_text(encoding="utf-8"))
# movies = json.loads(movies)


print("Creating database and table...", movies)
