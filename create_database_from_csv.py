import csv
import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

table_name = 'movies'
columns = 'Film TEXT, Genre TEXT, Lead Studio TEXT, AudienceScore INTEGER, Profitability REAL, RottenTomatoes INTEGER, WorldwideGross REAL, Year INTEGER'
cursor.execute(f'CREATE TABLE {table_name}({columns})')

with open('data_movie.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute(f"INSERT INTO {table_name} VALUES (?,?,?,?,?,?,?,?)", row)

conn.commit()
conn.close()
