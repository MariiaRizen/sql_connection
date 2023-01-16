import sqlite3
con = sqlite3.connect('work_file.db')
cur = con.cursor()
cur.execute("CREATE TABLE persons(id INTEGER, name varchar(255), birthdate varchar(32))")
cur.execute("""
    INSERT INTO persons VALUES
        (1, 'Kos Anna', '06.11.1987'),
        (2, 'Lesiv Pavlo', '31.12.1998'),
        (3, 'Pavliv Andriy', '03.02,1999') 
""")


cur.execute("CREATE TABLE employees(id INTEGER PRIMARY KEY, position varchar(255), salary INTEGER, FOREIGN KEY (id) REFERENCES persons(id))")
cur.execute("""
    INSERT INTO employees VALUES
        (1, 'teacher', 2000),
        (3, 'director', 2500)
""")

cur.execute("CREATE TABLE contacts(id INTEGER, type varchar(255), value varchar(255), FOREIGN KEY (id) REFERENCES persons(id))")
cur.execute("""
    INSERT INTO contacts VALUES
    (1, 'phone', '+380501213222'),
    (1, 'mail', 'assads@gmail.com'),
    (1, 'homephone', '044127654'),
    (2, 'phone', '+380632221254'),
    (3, 'mail', 'vcddcff@gmail.com'),
    (3, 'phone', '+380976664543')
""")


