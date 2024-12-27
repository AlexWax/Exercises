import os
import sqlite3

if __name__ == '__main__':
    db_name = 'my_fyrst.db'
    db_table_name = 'my_first_def.sql'
    db_is_creates = os.path.exists(db_name)
    connection = sqlite3.connect(db_name)

    if db_is_creates:
        print('Connect with existing db')
    else:
        print('Creating db')

    with open(db_table_name, 'rt') as table_file:
        my_table = table_file.read()
    connection.executescript(my_table)

    connection.executescript("""
        insert into my_project(name, description,
        deadline)
        values ('MagicMonth', 'Study python in 21
        day', '2024-12-27')
    """)

    connection.executescript("""
        insert into my_task(description, deadline, status, project)
        values ('Syntaxis', '2025-01-31', 'done', 'MagicMonth')
    """)
    connection.executescript("""
        insert into my_task(description, deadline, status, project)
        values ('Func', '2025-01-31', 'wait', 'MagicMonth')
    """)
    connection.executescript("""
        insert into my_task(description, deadline, status, project)
        values ('Errors', '2025-01-15', 'wait', 'MagicMonth')
    """)