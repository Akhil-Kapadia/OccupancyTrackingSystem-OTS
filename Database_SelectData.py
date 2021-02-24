import psycopg2

DB_NAME = "esxbzxjm"
DB_USER = "esxbzxjm"
DB_PASS = "xcokxIYMBjRCnQpVJBTSCSMBGvdCEzh-"
DB_HOST = "ziggy.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
print("Database connected successfully")

cur = conn.cursor()

cur.execute("SELECT id, Date, Time, CurrentOccupancy, Entry, People FROM Entry_Prevention_System_Table")
rows = cur.fetchall()

for data in rows:
    print("id: " + str(data[0]))
    print("Date: " + str(data[1]))
    print("Time: " + str(data[2]))
    print("CurrentOccupancy: " + str(data[3]))
    print("Entry: " + str(data[4]))
    print("People: " + str(data[5]))

print("Data Selected Successfully")
conn.close