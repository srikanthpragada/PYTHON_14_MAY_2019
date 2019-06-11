import sqlite3  # module to access Sqlite

con = sqlite3.connect(r"e:\classroom\python\may14\catalog.db")  # 1
cur = con.cursor()  # 2
try:
    cur.execute("select * from publishers")  # 3
    for pub in cur.fetchall():  # 4
        print(f"{pub[0]:4}  {pub[1]:15}  {pub[2]:30} {pub[3]}")
except Exception as ex:
    print("Sorry! Error : ", ex)
finally:
    cur.close()
    con.close()
