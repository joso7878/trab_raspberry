from database import connect_db

def insert_value(value):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO data (value) VALUES (?)',
            (value,)
        )
        conn.commit()

def get_all_values():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM data')
        rows = cursor.fetchall()

    return [
        {"id": row[0], "data": row[1]}
        for row in rows
    ]