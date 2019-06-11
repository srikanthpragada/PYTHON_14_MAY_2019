import sqlite3  # module to access Sqlite
import sys

con = sqlite3.connect(r"e:\classroom\python\may14\catalog.db")  # 1
cur = con.cursor()  # 2
try:
    id = input("Enter publisher id   :")
    cur.execute("select email from publishers where id = ?",(id,))
    pub = cur.fetchone()
    if pub is None:
        print("Sorry! Invalid publisher Id")
        sys.exit(0)

    print("Current email address : ", pub[0])
    email = input("Enter new email address : ")
    cur.execute("update publishers set email = ? where id = ?",(email,id))
    con.commit()
    print("Updated successfully!")
except Exception as ex:
    print("Sorry! Error : ", ex)
finally:
    print("Closing cur and con")
    cur.close()
    con.close()
