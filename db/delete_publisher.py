import sqlite3  # module to access Sqlite

con = sqlite3.connect(r"e:\classroom\python\may14\catalog.db")  # 1
cur = con.cursor()  # 2
try:
    id = input("Enter publisher id   :")
    cur.execute("delete from publishers where id = ?",(id,))
    if cur.rowcount == 1:
        con.commit()
        print("Deleted successfully!")
    else:
        print("Sorry! Invalid Publisher ID")
except Exception as ex:
    print("Sorry! Error : ", ex)
finally:
    print("Closing cur and con")
    cur.close()
    con.close()
