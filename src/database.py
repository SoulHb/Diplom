import mysql.connector
import os
from mysql.connector import Error
from src.text_processing import *


def create_database(host, user, password, db_name, table_name, DATA_PATH):

    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Check if the 'diploma' database already exists
        cursor.execute(f"SHOW DATABASES LIKE '{db_name}'")
        db_exists = cursor.fetchone()

        if not db_exists:
            # Create a new database named 'diploma'
            create_db_query = f"CREATE DATABASE {db_name}"
            cursor.execute(create_db_query)
            print(f"Database '{db_name}' created successfully")
        else:
            print(f"Database '{db_name}' already exists")
            return
        cursor.execute(f"USE {db_name}")

        # Create a table with fields id, file, and description
        table_creation_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            differential_equation_type VARCHAR(255),
            solving_methodology TEXT
        )
        """

        cursor.execute(table_creation_query)
        print(f"Table {table_name} created successfully")
        # Insert data into the table
        pdf_documents = os.listdir(DATA_PATH)
        for pdf in pdf_documents:
            solving_methodology = read_pdf(os.path.join(DATA_PATH, pdf))
            differential_equation_type = get_eq_type(os.path.join(DATA_PATH, pdf))
            insert_query = f"INSERT INTO {table_name} (differential_equation_type, solving_methodology) VALUES (%s, %s)"
            data_to_insert = (differential_equation_type, solving_methodology)

            cursor.execute(insert_query, data_to_insert)
            print("Data inserted successfully")

        # Commit changes and close connection
        conn.commit()
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed")
