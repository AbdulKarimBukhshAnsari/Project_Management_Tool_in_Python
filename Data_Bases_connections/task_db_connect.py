import sqlite3
conn = sqlite3.connect('Data_Bases\\task.db')
cursorr = conn.cursor()
cursorr.execute('''
    Create table Task (
        st_id INTEGER PRIMARY KEY,
        name VARCHAR(50),
        description TEXT,
        start_date DATE,
        end_date DATE,
        priority TEXT,
        status TEXT
             )
''')
conn.commit()
conn.close()