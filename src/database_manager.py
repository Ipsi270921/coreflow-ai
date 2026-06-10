import sqlite3
import os

DB_PATH = "pipeline_data.db"

# Define the absolute path to ensure the database file sits inside the 'data' folder
def initialize_database():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

def initialize_database():
    """Connects to SQLite and creates the data tracking table if it doesn't exist."""
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    
    # We write an explicit SQL schema tracking raw text and structured data fields
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_issues (
        issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_text TEXT NOT NULL,
        assigned_category TEXT NOT NULL,
        calculated_priority TEXT NOT NULL,
        clean_summary TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    
    connection.commit()
    connection.close()
    print("[SQL SUCCESS] Database schema built and verified.")

def insert_issue(original_text, ai_data):
    """
    Takes raw user text and the processed AI dictionary, 
    and commits them directly to the relational database table.
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    
    query = """
    INSERT INTO project_issues (original_text, assigned_category, calculated_priority, clean_summary)
    VALUES (?, ?, ?, ?);
    """
    
    # Safe tuple mapping to protect our SQL queries
    values = (
        original_text,
        ai_data['category'],
        ai_data['priority'],
        ai_data['summary']
    )
    
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    print("[SQL SUCCESS] Record committed to project_issues table.")

def get_all_issues():
    """Fetches all records from the database table to display on our web portfolio dashboard."""
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM project_issues ORDER BY created_at DESC;")
    records = cursor.fetchall()
    
    connection.close()
    return records

# Initialize the database immediately if this file is run directly
if __name__ == "__main__":
    initialize_database()
