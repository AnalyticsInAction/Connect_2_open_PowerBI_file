import adodbapi

# Connection string
#easiest place to get the PORT (60668 in the example below) is from DAX Studio
#similarly the Initial Catalog can be accessed from the connection page in DAX Studio under "advanced options"
conn_str = "Provider=MSOLAP;Data Source=localhost:60668;Initial Catalog=d87ae86c-8953-4448-a0cd-dcce467ea175;"

conn = adodbapi.connect(conn_str)

# Create a cursor
curs = conn.cursor()

# Replace with your actual query
sql = "EVALUATE 'SalesLT Product'"  # Example SQL query
curs.execute(sql)

# Fetch and print rows
rows = curs.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
curs.close()
conn.close()
