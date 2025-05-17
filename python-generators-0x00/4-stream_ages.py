import mysql.connector

def stream_user_ages():

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        
            password="96946765", 
            database="ALX_prodev"
        )
        
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("SELECT age FROM user_data")
        
        for (age,) in cursor:
            yield age

    except Exception as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")

def calculate_average_age():
   
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count == 0:
        print("No users found.")
    else:
        average_age = total_age / count
        print(f"Average age of users: {average_age:.2f}")


