import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent.parent / "database" / "newsense.db"


def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()  # objeto para ejecutar SQL
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS articles (
                    title TEXT,
                    descrition TEXT,
                    url TEXT UNIQUE,
                    published_at TEXT,
                    author TEXT,
                    topic TEXT,
                    sentiment TEXT,
                    sentiment_score TEXT
                )
                """)
    conn.commit()
    return conn
