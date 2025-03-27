import sqlite3

def vypsat(cursor):
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if not rows:
        print("Nejsou žádné záznamy.")
        return
    for row in rows:
        info = f"id={row[0]}, name={row[1]}, age={row[2]}, grade={row[3]}"
        print(info)

def pridat(cursor, conn):
    while True:
        name = input("Jméno: ")
        while True:
            age = int(input("Věk: "))
            if age <= 0:
                print("Špatný věk")
            else:
                break
        grade = input("Známka: ")
        cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
        conn.commit()
        dalsi = input("Přidat další? (A/N): ")
        if dalsi == "N":
            break

conn = sqlite3.connect("school.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL
    )
''')
conn.commit()

while True:
    print("\n MENU:")
    print("1. Přidat záznam")
    print("2. Vypsat záznamy")
    print("3. Konec")
    volba = input("Vyberte akci: ")
    if volba == "1":
        pridat(cursor, conn)
    elif volba == "2":
        vypsat(cursor)
    elif volba == "3":
        print("Exit")
        break
    else:
        print("Neplatná volba. Vyberte znovu.")
conn.close()
