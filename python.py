import mysql.connector

# Replace these with your database credentials
host = "localhost"
user = "root"
password = ""
database = "palgakalkulaator"

# Create a database connection
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Execute SQL queries here to interact with your database
# For example, fetching salary data or performing calculations

# Close the cursor and connection when done
cursor.close()
conn.close()
