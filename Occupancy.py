import psycopg2

DB_NAME = "esxbzxjm"
DB_USER = "esxbzxjm"
DB_PASS = "xcokxIYMBjRCnQpVJBTSCSMBGvdCEzh-"
DB_HOST = "ziggy.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
print("Database connected successfully")

cur = conn.cursor()
cur.execute ("CREATE TABLE Entry_Prevention_System_Table(id INTEGER, date DATE, time TIME, current_occupancy INTEGER, entries INTEGER, exits INTEGER);")

conn.commit()
print("Table created successfully")





















"""
SQL Code:

CREATE DATABASE PL3_Database;
USE PL3_Database;
CREATE TABLE Entry_Prevention_System_Table(id INTEGER, date DATE, time TIME, current_occupancy INTEGER, entries INTEGER, exits INTEGER);
INSERT INTO Entry_Prevention_System_Table(current_occupancy, entries, exits) VALUES (1, 1, 0);
SELECT * FROM Entry_Prevention_System_Table;
"""