import psycopg2

DB_NAME = "esxbzxjm"
DB_USER = "esxbzxjm"
DB_PASS = "xcokxIYMBjRCnQpVJBTSCSMBGvdCEzh-"
DB_HOST = "ziggy.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
print("Database connected successfully")

cur = conn.cursor()

cur.execute("DELETE FROM Entry_Prevention_System_Table WHERE id = 2")
conn.commit

print("Data deleted successfully")
print("Total rows affected: " + str(cur.rowcount))