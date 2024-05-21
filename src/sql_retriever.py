import mysql.connector
from mysql.connector import Error


def sql_retrieval(host, user, password, db_name, table_name):
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        # Use db
        cursor.execute(f"USE {db_name}")
        # Execute the SQL command
        cursor.execute(f"""SELECT solving_methodology FROM {table_name};""")
        solving_methodology = cursor.fetchall()
        # Fetch all the rows

        # Commit changes (not necessary for SELECT queries) and close connection
        conn.commit()

        return solving_methodology # Return the fetched data
    except Error as e:
        print(f"Error: {e}")
        return None  # Return None in case of error

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed")