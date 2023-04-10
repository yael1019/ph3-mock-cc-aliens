import sqlite3

CONN = sqlite3.connect('lib/db/development.db')
CURSOR = CONN.cursor()

# BELOW ARE SQL COMMANDS THAT WILL CREATE THE TABLES #

create_aliens_sql = """CREATE TABLE IF NOT EXISTS aliens (
id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT,
age INTEGER
)
"""

create_planets_sql = """CREATE TABLE IF NOT EXISTS planets (
id INTEGER PRIMARY KEY,
name TEXT
)
"""

CURSOR.execute(create_aliens_sql)
CURSOR.execute(create_planets_sql)
