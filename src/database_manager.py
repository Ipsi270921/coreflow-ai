import sqlite3

# SQLite database file
DB_PATH = "pipeline_data.db"


def initialize_database():
    """Connects to SQLite and creates the data tracking table if it doesn't exist."""
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

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
    INSERT INTO project_issues (
        original_text,
        assigned_category,
        calculated_priority,
        clean_summary
    )
    VALUES (?, ?, ?, ?);
    """

    values = (
        original_text,
        ai_data["category"],
        ai_data["priority"],
        ai_data["summary"]
    )

    cursor.execute(query, values)
    connection.commit()
    connection.close()

    print("[SQL SUCCESS] Record committed to project_issues table.")


def get_all_issues():
    """Fetches all records from the database table."""
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM project_issues ORDER BY created_at DESC;"
    )

    records = cursor.fetchall()

    connection.close()
    return records


if __name__ == "__main__":
    initialize_database()
