import sqlite3

DATABASE = "jobs.db"


def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


def init_db():
    db = get_db()

    db.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            status TEXT NOT NULL,
            application_date TEXT,
            job_url TEXT,
            notes TEXT
        )
    """)

    columns = db.execute("PRAGMA table_info(jobs)").fetchall()
    column_names = [column[1] for column in columns]

    if "application_date" not in column_names:
        db.execute("ALTER TABLE jobs ADD COLUMN application_date TEXT")

    if "job_url" not in column_names:
        db.execute("ALTER TABLE jobs ADD COLUMN job_url TEXT")

    if "notes" not in column_names:
        db.execute("ALTER TABLE jobs ADD COLUMN notes TEXT")

    db.commit()
    db.close()