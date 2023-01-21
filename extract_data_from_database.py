import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
table_name = 'movies'

cursor.execute(f'PRAGMA table_info({table_name})')
result = cursor.fetchall()
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

# Close the connection to the database
conn.close()

