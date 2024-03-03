import adodbapi
import pandas as pd

# Connection string
conn_str = "Provider=MSOLAP;Data Source=localhost:60668;Initial Catalog=d87ae86c-8953-4448-a0cd-dcce467ea175;"

conn = adodbapi.connect(conn_str)

# Create a cursor
curs = conn.cursor()

# SQL to query the DMV for a list of table names
sql_tables = "SELECT * FROM $SYSTEM.TMSCHEMA_TABLES"

curs.execute(sql_tables)

# Fetch table names
table_names = curs.fetchall()

# Dictionary to hold each table DataFrame
tables_df = {}

# Iterate through each table name and load it into a DataFrame
for row in table_names:
    table_name = row[2]  # Assuming the table name is in the third column
    print(f"Loading DataFrame for table: {table_name}")
    sql = f"EVALUATE '{table_name}'"
    curs.execute(sql)
    rows = curs.fetchall()
    # Assuming first row contains column headers
    headers = [column[0] for column in curs.description]
    df = pd.DataFrame(rows, columns=headers)
    tables_df[table_name] = df
    print(f"Created DataFrame: {table_name}")
    #display(tables_df[table_name])

    # Print the DataFrame explicitly
    print(f"DataFrame '{table_name}' contents:")
    #print(tables_df[table_name])
    display(tables_df[table_name])
    

# Close the cursor and connection
curs.close()
conn.close()
