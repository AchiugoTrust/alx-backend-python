import mysql.connector


def stream_users_in_batches(batch_size):
   
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        
            password="96946765", 
            database="ALX_prodev"
        )
        
        cursor = connection.cursor(dictionary=True)  

        cursor.execute("SELECT * FROM user_data")
        
        batch = []
        for user in cursor:  
            batch.append(user)
            if len(batch) == batch_size:
                yield batch
                batch = []

        if batch:
            yield batch

    except Exception as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):  
        filtered_batch = [user for user in batch if user['age'] > 25] 
        yield filtered_batch


