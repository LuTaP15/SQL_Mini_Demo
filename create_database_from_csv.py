"""
SQL Mini Demo:

- Imports data from CSV to SQLite database
- Creates 'movies' table
- Inserts data from CSV to table
- Commits and closes database connection
"""
# Libaries
import csv
import sqlite3

# Connect to the database and create a cursor
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Create the 'movies' table
table_name = 'movies'
columns = 'Film TEXT, Genre TEXT, LeadStudio TEXT, AudienceScore INTEGER, Profitability REAL, RottenTomatoes INTEGER, WorldwideGross REAL, Year INTEGER'
cursor.execute(f'CREATE TABLE {table_name}({columns})')

# Open the CSV file and insert the data into the 'movies' table
with open('data_movie.csv') as f:
    next(f) # Skip the header row
    cursor.executemany('INSERT INTO movies VALUES (?,?,?,?,?,?,?,?)', csv.reader(f))

# Commit the transaction and close the connection
conn.commit()
conn.close()
