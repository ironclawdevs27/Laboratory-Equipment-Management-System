import sqlite3


def create_db():
    con = sqlite3.connect(database=r'login.db')
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS login(id text, pass TEXT)")
    cur.execute('''INSERT INTO login VALUES ('admin', '1234')''')
    cur.execute('''INSERT INTO login VALUES ('student', '1234')''')
    con.commit()


create_db()
