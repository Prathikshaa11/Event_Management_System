# Title      : Event Management System
#Author      : S Prathikshaa
#Created on  : 12/02/2023
#Reviewed by : Silpa M
#Reviewd on  : 25/02/2023



import mysql.connector
from admin_module import admin_login, admin_registration
from event_module import add_event, view_events, delete_event, set_ticket_fare
from staff_module import add_staff, view_staff

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

def main():
    print("------Welcome to Event Management Company-----")
    print("\nAdmin Registration/Login")
    print("1. Admin Login")
    print("2. Admin Registration")
    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        if admin_login():
            events = []
            while True:
                print("\nEvent Management")
                print("1. Add Event")
                print("2. View Events")
                print("3. Delete Event")
                print("4. Set Ticket Fare")
                print("5. Exit")

                event_choice = input("Enter your choice (1-5): ")

                if event_choice == '1':
                    add_event(events)
                elif event_choice == '2':
                    view_events(events)
                elif event_choice == '3':
                    delete_event(events)
                elif event_choice == '4':
                    set_ticket_fare(events)
                elif event_choice == '5':
                    break
                else:
                    print("Invalid choice. Please try again.")

    elif choice == '2':
        admin_registration()
        events = []
        while True:
            print("\nEvent Management")
            print("1. Add Event")
            print("2. View Events")
            print("3. Delete Event")
            print("4. Set Ticket Fare")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                add_event(events)
            elif choice == '2':
                view_events(events)
            elif choice == '3':
                delete_event(events)
            elif choice == '4':
                set_ticket_fare(events)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

        staff_module()  # Execute staff module after the event module

def staff_module():
    staffs = []
    while True:
        print("\nManaging Event Staffs")
        print("1. Add Staff to Event")
        print("2. View Staff of an Event")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_staff(staffs)
        elif choice == '2':
            view_staff(staffs)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
