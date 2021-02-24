import psycopg2

DB_NAME = "esxbzxjm"
DB_USER = "esxbzxjm"
DB_PASS = "xcokxIYMBjRCnQpVJBTSCSMBGvdCEzh-"
DB_HOST = "ziggy.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
print("Database connected successfully")

cur = conn.cursor()

cur.execute("INSERT INTO Entry_Prevention_System_Table (id, Date, Time, CurrentOccupancy, Entry, People) VALUES(1, '2/16/2021', '10:15', 2, 'true', 2);")
cur.execute("INSERT INTO Entry_Prevention_System_Table (id, Date, Time, CurrentOccupancy, Entry, People) VALUES(2, '2/16/2021', '12:30', 5, 'true', 3);")
cur.execute("INSERT INTO Entry_Prevention_System_Table (id, Date, Time, CurrentOccupancy, Entry, People) VALUES(3, '2/16/2021', '13:45', 3, 'false', 2);")
cur.execute("INSERT INTO Entry_Prevention_System_Table (id, Date, Time, CurrentOccupancy, Entry, People) VALUES(4, '2/16/2021', '15:15', 4, 'true', 1);")
cur.execute("INSERT INTO Entry_Prevention_System_Table (id, Date, Time, CurrentOccupancy, Entry, People) VALUES(5, '2/16/2021', '16:55', 2, 'false', 2);")
cur.execute("INSERT INTO Entry_Prevention_System_Table (id, Date, Time, CurrentOccupancy, Entry, People) VALUES(6, '2/16/2021', '18:30', 3, 'true', 1);")
cur.execute("INSERT INTO Entry_Prevention_System_Table (id, Date, Time, CurrentOccupancy, Entry, People) VALUES(7, '2/16/2021', '19:15', 0, 'false', 3);")
conn.commit()
print("Data interted successfully")
conn.close()