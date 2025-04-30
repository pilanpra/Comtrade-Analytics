import mysql.connector

# MySQL server connection parameters
db_config = {
    'host': 'localhost',
    'port': 3306,           # default MySQL port
    'user': 'root',      # your docker user
    'password': 'my-secret-pw',  # your docker password
    'database': 'trade_db',    # database to use
    'allow_local_infile': True # required if loading CSVs later
}

# Path to your SQL script
sql_file_path = 'setup_trade_table.sql'

# Connect to MySQL
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print("✅ Connected to MySQL.")

    # Read and run SQL file
    with open(sql_file_path, 'r') as file:
        sql_script = file.read()

    # Split and execute each SQL command separately
    for statement in sql_script.split(';'):
        statement = statement.strip()
        if statement:
            cursor.execute(statement)
    
    conn.commit()
    print("✅ SQL script executed successfully.")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

# finally:
#     if conn & conn.is_connected():
#         cursor.close()
#         conn.close()
#         print("🔒 Connection closed.")
#     else:
