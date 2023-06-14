import sqlite3

con = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\database\\basketball_maindb.db')
cur = con.cursor()

cur.execute("SELECT * from TEST4may903598")
fetch = cur.fetchall()

temp = ""
for i in fetch:
    temp += str(i) + '\n'

print(temp)

con.commit()
con.close()
