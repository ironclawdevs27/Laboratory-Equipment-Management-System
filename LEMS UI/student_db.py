import sqlite3


def create_db():
    con = sqlite3.connect(database=r'student.db')
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS student(studentid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, dept TEXT)")
    cur.execute('''INSERT INTO student VALUES (1, 'Aryan Raj', 'CSE')''')
    cur.execute('''INSERT INTO student VALUES (2, 'Arshia Dhiman', 'CSE')''')
    cur.execute('''INSERT INTO student VALUES (3, 'Ayush Gautam', 'CSE')''')
    cur.execute('''INSERT INTO student VALUES (4, 'Anavi Sharma', 'CSE')''')
    cur.execute(
        '''INSERT INTO student VALUES (5, 'Himanshu Kaushal', 'CSE')''')
    cur.execute('''INSERT INTO student VALUES (6, 'Dikit Paldon', 'IT')''')
    cur.execute(
        '''INSERT INTO student VALUES (7, 'Avishi Jain', 'IT')''')
    cur.execute(
        '''INSERT INTO student VALUES (8, 'Anshul Singh', 'IT')''')
    cur.execute(
        '''INSERT INTO student VALUES (9, 'Kamit Rastogi', 'Mech')''')
    cur.execute(
        '''INSERT INTO student VALUES (10, 'Akashdeep Singh', 'Mech')''')
    cur.execute(
        '''INSERT INTO student VALUES (11, 'Devanshi Verma', 'BioT')''')
    cur.execute(
        '''INSERT INTO student VALUES (12, 'Chetna Chopra', 'BioT')''')
    cur.execute(
        '''INSERT INTO student VALUES (13, 'Hitesh Bandhu', 'ECE')''')
    cur.execute(
        '''INSERT INTO student VALUES (14, 'Gunjan Sarode', 'ECE')''')
    cur.execute(
        '''INSERT INTO student VALUES (15, 'Sanitya Srivastava', 'EEE')''')
    con.commit()


create_db()
