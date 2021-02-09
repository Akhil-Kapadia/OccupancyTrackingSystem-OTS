"""
SQL Code:

CREATE DATABASE PL3_Database;
USE PL3_Database;
CREATE TABLE Entry_Prevention_System_Table(id INTEGER, date DATE, time TIME, current_occupancy INTEGER, entries INTEGER, exits INTEGER);
INSERT INTO Entry_Prevention_System_Table(current_occupancy, entries, exits) VALUES (1, 1, 0);
SELECT * FROM Entry_Prevention_System_Table;
"""