import mysql.connector

def get_database_connection():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'prathi@123',
        'database': 'event_management',
    }

    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        print("Error: Unable to connect to the database.")
        print(err)
        return None

def insert_admin(username, password):
    connection = get_database_connection()

    if connection:
        try:
            with connection.cursor() as cursor:
                insert_query = "INSERT INTO admins (username, password) VALUES (%s, %s)"
                cursor.execute(insert_query, (username, password))
                connection.commit()
                print("Admin added successfully!")
        except mysql.connector.Error as err:
            print("Error: Unable to add the admin.")
            print(err)
        finally:
            connection.close()
    else:
        print("Error: Unable to connect to the database.")

def get_admin(username, password):
    connection = get_database_connection()

    if connection:
        try:
            with connection.cursor() as cursor:
                select_query = "SELECT * FROM admins WHERE username = %s AND password = %s"
                cursor.execute(select_query, (username, password))
                result = cursor.fetchone()
                return result
        except mysql.connector.Error as err:
            print("Error: Unable to retrieve admin from the database.")
            print(err)
        finally:
            connection.close()
    else:
        print("Error: Unable to connect to the database.")
def insert_event(event_name, event_date, event_location, artist=None, ticket_fare=None):
    connection = get_database_connection()

    if connection:
        try:
            with connection.cursor() as cursor:
                if artist:
                    insert_query = "INSERT INTO events (event_name, event_date, event_location, artist, ticket_fare) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(insert_query, (event_name, event_date, event_location, artist, ticket_fare))
                else:
                    insert_query = "INSERT INTO events (event_name, event_date, event_location, ticket_fare) VALUES (%s, %s, %s, %s)"
                    cursor.execute(insert_query, (event_name, event_date, event_location, ticket_fare))
                connection.commit()
                print("Event added successfully!")
        except mysql.connector.Error as err:
            print("Error: Unable to add the event.")
            print(err)
        finally:
            connection.close()
    else:
        print("Error: Unable to connect to the database.")

def get_events():
    connection = get_database_connection()

    if connection:
        try:
            with connection.cursor() as cursor:
                select_query = "SELECT * FROM events"
                cursor.execute(select_query)
                results = cursor.fetchall()
                return results
        except mysql.connector.Error as err:
            print("Error: Unable to retrieve events from the database.")
            print(err)
        finally:
            connection.close()
    else:
        print("Error: Unable to connect to the database.")

def insert_staff(event_name, staff_name, staff_role):
    connection = get_database_connection()

    if connection:
        try:
            with connection.cursor() as cursor:
                insert_query = "INSERT INTO staffs (event_name, staff_name, staff_role) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, (event_name, staff_name, staff_role))
                connection.commit()
                print("Staff added successfully!")
        except mysql.connector.Error as err:
            print("Error: Unable to add the staff.")
            print(err)
        finally:
            connection.close()
    else:
        print("Error: Unable to connect to the database.")

def get_staffs():
    connection = get_database_connection()

    if connection:
        try:
            with connection.cursor() as cursor:
                select_query = "SELECT * FROM staffs"
                cursor.execute(select_query)
                results = cursor.fetchall()
                return results
        except mysql.connector.Error as err:
            print("Error: Unable to retrieve staffs from the database.")
            print(err)
        finally:
            connection.close()
    else:
        print("Error: Unable to connect to the database.")
