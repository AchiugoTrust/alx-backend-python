import mysql.connector
from seed import connect_to_prodev

def stream_users(connection):
    try: 
        cursor = connection.cursor(dictionary=True)  # Fetch results as dictionaries

        cursor.execute("SELECT * FROM user_data")

        for user in cursor:
            yield user

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")