import sqlite3  # module to access Sqlite

con = sqlite3.connect(r"e:\classroom\python\may14\catalog.db")  # 1
cur = con.cursor()  # 2
try:
    cur.execute("select count(*) from publishers")  # 3
    print("No. of publishers : ", cur.fetchone()[0])
except Exception as ex:
    print("Sorry! Error : ", ex)
finally:
    cur.close()
    con.close()
