import psycopg2
import requests
from bs4 import BeautifulSoup

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        database="dse",
        user="postgres",
        password="admin",
        port = "5432"
    )
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    # Execute a simple query
    cursor.execute("SELECT version()")
    # Fetch the query result
    result = cursor.fetchone()
    # Print the PostgreSQL server version
    print("Connected to PostgreSQL")
    print("PostgreSQL version:", result[0])
    # Close the cursor and the connection
    cursor.close()
    conn.close()
except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)

    
#creating table in postgres db
def create_table():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="dse",
        user="postgres",
        password="admin"
    )

    cursor = conn.cursor()

    table_name = "company_t"
    table_schema = """
                    CREATE TABLE IF NOT EXISTS company_t (
                        company_id SERIAL PRIMARY KEY,
                        company_name VARCHAR(255),
                        scrip_code INTEGER,
                        trading_code VARCHAR(100),
                        sector VARCHAR(100),
                        url VARCHAR(100),
                        address VARCHAR(200)
                    )
    """.format(table=table_name)

    cursor.execute(table_schema)

    conn.commit()
    cursor.close()
    conn.close()

create_table()

