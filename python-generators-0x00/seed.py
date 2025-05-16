import mysql.connector
import csv

def connect_db():
    """Connects to the MySQL database server."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # Replace with your MySQL username
            password="96946765" # Replace with your MySQL password
        )
        print("Connected to MySQL server.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
    
def create_database(connection):
    """Creates the database ALX_prodev if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev is ready.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # Replace with your MySQL username
            password="96946765", # Replace with your MySQL password
            database="ALX_prodev"
        )
        print("Connected to ALX_prodev database.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
    
def create_table(connection):
    """Creates the user_data table if it does not exist."""
    try:
        cursor = connection.cursor()
        create_table_query = """
        
        CREATE TABLE IF NOT EXISTS user_data (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            age DECIMAL NOT NULL,
            UNIQUE INDEX idx_user_id (user_id)
        )
        """
        cursor.execute(create_table_query)
        print("Table user_data is ready.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    
def insert_data(connection, data):
    """Inserts data in the database if it does not exist."""
    try:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO user_data (name, email, age)
        VALUES (%s, %s, %s)
        """
        cursor.executemany(insert_query, data)
        connection.commit()
        print(f"Inserted {cursor.rowcount} records into user_data table.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    
def read_csv(file_path):
    """Reads data from the CSV file."""
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header
        return [tuple(row) for row in csv_reader]


if __name__ == "__main__":
    # Step 1: Connect to MySQL server
    connection = connect_db()
    if not connection:
        exit()

    create_database(connection)
    connection.close()

    # Step 3: Connect to the ALX_prodev database
    db_connection = connect_to_prodev()
    if not db_connection:
        exit()
    
    create_table(db_connection)

    # Step 5: Read the data from CSV
    data = read_csv("user_data.csv")

    # Step 6: Insert data into the table
    insert_data(db_connection, data)

    db_connection.close()
    print("Database population complete.")
