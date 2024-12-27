import sqlite3

db_name = 'my_fyrst.db'
with sqlite3.connect(db_name) as connection:
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
    select id, priority, description,
    status, deadline from my_task
    where project = ?
    """, "Magic_month")
    for it_row in cursor.fetchall():
        id, priority, description,
        status, deadline = it_row
        print(it_row['id'])