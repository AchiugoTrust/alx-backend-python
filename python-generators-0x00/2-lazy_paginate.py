import mysql.connector

def paginate_users(page_size, offset):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        
            password="96946765", 
            database="ALX_prodev"
        )
        
        cursor = connection.cursor(dictionary=True)
        
        query = f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}"
        cursor.execute(query)

        users = cursor.fetchall()
        return users

    except Exception as err:
        print(f"Error: {err}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def lazypaginate(page_size):
    
    offset = 0 
    while True:
        users = paginate_users(page_size, offset)
        
        if not users:
            break
        
        yield users
        offset += page_size
