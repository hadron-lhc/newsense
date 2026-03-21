import sqlite3
from pathlib import Path
from core.fetcher import fetch_news

DATABASE_PATH = Path("/data/newsense.db")


def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()  # objeto para ejecutar SQL
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS articles (
                    title TEXT,
                    description TEXT,
                    url TEXT UNIQUE,
                    published_at TEXT,
                    author TEXT,
                    topic TEXT,
                    sentiment TEXT,
                    sentiment_score REAL
                )
                """)
    conn.commit()
    return conn


def insert_article(conn, article, topic):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT OR IGNORE INTO articles (title, description, url, published_at, author, topic, sentiment, sentiment_score)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            article["title"],
            article["description"],
            article["url"],
            article["publishedAt"],
            article["author"],
            topic,
            None,
            None,
        ),
    )
    conn.commit()


def save_articles(conn, articles, topic):
    for article in articles:
        insert_article(conn, article, topic)


def get_articles_by_topic(conn, topic):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles WHERE topic = ?", (topic,))
    return cursor.fetchall()


if __name__ == "__main__":
    conn = init_db()
    topic = "Apple"
    articles = fetch_news(topic)
    for article in articles:
        insert_article(conn, article, topic)
    recur = get_articles_by_topic(conn, topic)
    print(recur)
