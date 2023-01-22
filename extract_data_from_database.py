"""
SQL Mini Demo:

- Prints the column names and data types of the table.
- Finds the average audience score for movies by year.
- Finds the average audience score for movies by genre.
- Sorts the movies by profitability.
- Finds the top 5 profitable movies.
- Finds movies that were released in a specific year 2010.
- Finds movies that have a specific genre Drama.
- Closes the connection to the database.
"""

# Libaries
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
table_name = 'movies'

# Print the column names and data types of the 'movies' table
cursor.execute(f'PRAGMA table_info({table_name})')
result = cursor.fetchall()
print("The columns and data types of the 'movies' table:")
print(result)

# Find the average audience score for movies by year
cursor.execute(f'SELECT Genre, AVG("AudienceScore") FROM {table_name} GROUP BY Year')
result = cursor.fetchall()
print("The average audience score for movies by year:")
print(result)

# Find the average audience score for movies by genre
cursor.execute(f'SELECT Genre, AVG("AudienceScore") FROM {table_name} GROUP BY Genre')
result = cursor.fetchall()
print("The average audience score for movies by genre:")
print(result)

# Sort the movies by profitability
cursor.execute(f'SELECT * FROM {table_name} ORDER BY Profitability DESC')
result = cursor.fetchall()
print("The movies sorted by profitability:")
print(result)

# Top 5 profitable movies
cursor.execute(f'SELECT Film, Profitability FROM {table_name} ORDER BY Profitability DESC LIMIT 5')
result = cursor.fetchall()
print("The top 5 profitable movies:")
print(result)

# Movies that were released in a specific year
cursor.execute(f'SELECT Film FROM {table_name} WHERE Year = 2010')
result = cursor.fetchall()
print("Movies that were released in 2010:")
print(result)

# Movies that have a specific genre
cursor.execute(f'SELECT Film FROM {table_name} WHERE Genre = "Drama"')
result = cursor.fetchall()
print("Movies that are of Drama genre:")
print(result)

# Close the connection to the database
conn.close()
