import sqlite3
import os

conn = None

def get_db_connection():
    """Establishes a connection to the database."""
    global conn
    if os.environ.get("FLASK_ENV") == "testing":
        if conn is None:
            conn = sqlite3.connect(":memory:", check_same_thread=False)
            conn.row_factory = sqlite3.Row
        return conn
    else:
        conn = sqlite3.connect("users.db", check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

def execute_query(query, params=(), fetchone=False, commit=False):
    """Executes a SQL query with parameters."""
    conn = get_db_connection()
    cursor = conn.cursor()

    result = None
    cursor.execute(query, params)
    if fetchone:
        result = cursor.fetchone()
    else:
        result = cursor.fetchall()
    if commit:
        conn.commit()

    if os.environ.get("FLASK_ENV") != "testing":
        conn.close()

    return result
