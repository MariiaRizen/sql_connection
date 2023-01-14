import sqlite3
con = sqlite3.connect('work_file.db')
cur = con.cursor()
res = cur.execute("""SELECT contacts.type, contacts.value, employees.position 
            FROM persons
            LEFT JOIN employees ON persons.id=employees.id
            LEFT JOIN contacts ON persons.id=contacts.id
""")
print(res)
#SELECT employees.position, contacts.type, contacts.value ... WHERE emplyees.id={id})