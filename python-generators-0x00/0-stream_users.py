import mysql.connector


def stream_users():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # Replace with your MySQL username
            password="96946765", # Replace with your MySQL password
            database="ALX_prodev"
        )
        
        cursor = connection.cursor(dictionary=True)  # Fetch results as dictionaries

        # Step 2: Execute the SQL query to fetch all users
        cursor.execute("SELECT * FROM user_data")

        # Step 3: Use a generator to yield each user row
        for user in cursor:
            yield user

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")