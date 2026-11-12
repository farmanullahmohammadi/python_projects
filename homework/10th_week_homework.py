
import sqlite3

def connect():
    return sqlite3.connect("contacts.db")

def initialize_db():
    with connect() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT UNIQUE,
            category TEXT
        )
        """)

def add_contact(name, phone, email, category):
    with connect() as conn:
        conn.execute("""
        INSERT INTO contacts
        (name, phone, email, category)
        VALUES (?, ?, ?, ?)
        """, (name, phone, email, category))

def get_contacts():
    with connect() as conn:
        return conn.execute(
            "SELECT * FROM contacts"
        ).fetchall()

def search_contacts(term):
    with connect() as conn:
        return conn.execute("""
        SELECT * FROM contacts
        WHERE name LIKE ?
        """, (f"%{term}%",)).fetchall()

def update_contact(contact_id, name, phone, email, category):
    with connect() as conn:
        conn.execute("""
        UPDATE contacts
        SET name=?, phone=?, email=?, category=?
        WHERE id=?
        """, (name, phone, email, category, contact_id))

def delete_contact(contact_id):
    with connect() as conn:
        conn.execute("""
        DELETE FROM contacts WHERE id=?
        """, (contact_id,))
