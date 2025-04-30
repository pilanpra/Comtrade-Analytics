import mysql.connector

# Connect to MySQL
db_config = {
    'host': 'localhost',
    'port': 3306,           # default MySQL port
    'user': 'root',      # your docker user
    'password': 'my-secret-pw',  # your docker password
    'database': 'trade_db',    # database to use
    'allow_local_infile': True # required if loading CSVs later
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Enable LOCAL INFILE
cursor.execute("SET GLOBAL local_infile = 1;")

# Load data
csv_file_path = '/Users/prasadpilankar/Documents/BAN/DE2025/Comtrade-Analytics/data-transform/cleandata_trade_cleaned.csv'  # must be absolute path

load_query = f"""
LOAD DATA LOCAL INFILE '{csv_file_path}'
INTO TABLE trade_summary
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(typecode, refyear, reporteriso, reporterdesc, partneriso, partnerdesc, flowcode, cmdcode, cmddesc, qty, netwgt, cifvalue, fobvalue, primaryvalue, isreported);
"""

cursor.execute(load_query)
conn.commit()

print("✅ Data uploaded successfully!")

cursor.close()
conn.close()
