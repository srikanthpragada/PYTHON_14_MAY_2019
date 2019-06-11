import sqlite3  # module to access Sqlite

con = sqlite3.connect(r"e:\classroom\python\may14\catalog.db")  # 1
cur = con.cursor()  # 2
try:
    name = input("Enter publisher name   :")
    email = input("Enter publisher email  :")
    mobile = input("Enter publisher mobile :")

    cur.execute("insert into publishers(name,email,phone) values(?,?,?)",
                (name, email, mobile))  # 3
    con.commit()
    print("Added Publisher!")
except Exception as ex:
    print("Sorry! Error : ", ex)
finally:
    cur.close()
    con.close()
