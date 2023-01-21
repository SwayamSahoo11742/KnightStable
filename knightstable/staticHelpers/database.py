import sqlite3
import os
path = os.path.abspath("games.db").replace("staticHelpers\\", "")

try:
    database = sqlite3.connect(path)
    db = database.cursor()
    db.execute("CREATE TABLE games ( id INTEGER PRIMARY KEY AUTOINCREMENT, site TEXT, white TEXT, black TEXT, result TEXT, white_elo INTEGER, black_elo INTEGER, moves TEXT , opening TEXT);")
    db.execute("CREATE TABLE opening ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, color TEXT, win_rate NUMERIC, draw_rate NUMERIC, loss_rate NUMERIC, moves TEXT);")
    db.execute("CREATE TABLE ksgame ( game_id  INTEGER PRIMARY KEY AUTOINCREMENT, site   NUMERIC, black TEXT, white TEXT, status TEXT, pgn TEXT, time TEXT, rated TEXT, white_rating INTEGER, black_rating INTEGER, result NUMERIC, datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
    db.execute("CREATE TABLE users ( id integer PRIMARY KEY autoincrement, username text NOT NULL, hash numeric NOT NULL, email NUMERIC NOT NULL, rating INTEGER NOT NULL DEFAULT 100, pfp TEXT NOT NULL DEFAULT \"logo.jpg\", about TEXT DEFAULT \"I'm Cool\", uscf INTEGER);")
    db.close()
except Exception as e:
    print(e)