import sqlite3


def create_database():

    conn = sqlite3.connect("database/database.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recommendations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        predicted_demand INTEGER,
        supplier TEXT,
        route TEXT,
        expected_cost REAL,
        fuel_usage REAL,
        sustainability_score REAL,
        green_score REAL
    )
    """)

    conn.commit()
    conn.close()


def save_recommendation(
    predicted_demand,
    supplier,
    route,
    expected_cost,
    fuel_usage,
    sustainability_score,
    green_score
):

    conn = sqlite3.connect("database/database.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO recommendations (
        predicted_demand,
        supplier,
        route,
        expected_cost,
        fuel_usage,
        sustainability_score,
        green_score
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        predicted_demand,
        supplier,
        route,
        expected_cost,
        fuel_usage,
        sustainability_score,
        green_score
    ))

    conn.commit()
    conn.close()


if __name__ == "__main__":

    create_database()

    print("Database Created Successfully")