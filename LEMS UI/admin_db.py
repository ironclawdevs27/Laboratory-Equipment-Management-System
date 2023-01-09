import sqlite3


def create_db():
    con = sqlite3.connect(database=r'admin.db')
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS admin(adminid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, desig TEXT)")
    cur.execute('''INSERT INTO admin VALUES (1, 'Aryan Raj', 'Student')''')
    cur.execute('''INSERT INTO admin VALUES (2, 'Arshia Dhiman', 'Student')''')
    cur.execute('''INSERT INTO admin VALUES (3, 'Ayush Gautam', 'Student')''')
    cur.execute('''INSERT INTO admin VALUES (4, 'Anavi Sharma', 'Student')''')
    cur.execute(
        '''INSERT INTO admin VALUES (5, 'Himanshu Kaushal', 'Student')''')
    cur.execute('''INSERT INTO admin VALUES (6, 'Mamta Juneja', 'Professor')''')
    cur.execute(
        '''INSERT INTO admin VALUES (7, 'Sakshi Kaushal', 'Co-ordinator')''')
    cur.execute(
        '''INSERT INTO admin VALUES (8, 'Akashdeep Verma', 'Assistant Professor')''')
    cur.execute(
        '''INSERT INTO admin VALUES (9, 'Sukhwinder Singh', 'Professor')''')
    cur.execute(
        '''INSERT INTO admin VALUES (10, 'Deepti Gupta', 'Assistant Professor')''')
    cur.execute(
        '''INSERT INTO admin VALUES (11, 'Puneet Kapur', 'Assistant Professor')''')
    cur.execute(
        '''INSERT INTO admin VALUES (12, 'Praveen Mehra', 'Lab Incharge')''')
    cur.execute(
        '''INSERT INTO admin VALUES (13, 'Gurwinder Saini', 'Lab Incharge')''')
    cur.execute(
        '''INSERT INTO admin VALUES (14, 'Hardy Sandhu', 'Lab Assistant')''')
    cur.execute(
        '''INSERT INTO admin VALUES (15, 'Akhil Singh', 'Lab Assistant')''')
    con.commit()


create_db()
