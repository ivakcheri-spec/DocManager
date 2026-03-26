import sqlite3
import os
import sys


DB_PATH = os.path.join("data","documents.db")
sys.path.append(DB_PATH)

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():

    conn = get_connection()
    cursor = conn.cursor()
    
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     name  TEXT,
     path  TEXT ,
     thumbnail_path TEXT,
     tags TEXT,
     description TEXT,
     upload_date TEXT,
     lecture_date TEXT,
     total_pages INTEGER                                         
                   )
    """
    )

    conn.commit()
    print("DB operation successful")
    conn.close()
    