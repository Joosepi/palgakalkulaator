import mysql.connector

# Replace these with your database credentials
host = "localhost"
user = "root"
password = "Dragon196575"
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
selectquery="select*from {employees}"  

# Execute a SELECT query
cursor.execute("SELECT * FROM selectquery")

# Fetch the results
results = cursor.fetchall()

# Process the results
for row in results:
    print(row)


# Close the cursor and connection when done
cursor.close()
conn.close()



