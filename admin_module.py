from database import insert_admin, get_admin

def admin_registration():
    print("Admin Registration")
    username = input("Enter username: ")

    while True:
        password = input("Enter password: ")
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
        elif not any(char.isdigit() for char in password):
            print("Password must contain at least one digit.")
        elif not any(char.isalpha() for char in password):
            print("Password must contain at least one letter.")
        else:
            break

    insert_admin(username, password)
    print("Registration successful!")

def admin_login():
    print("Admin Login")
    username = input("Enter username: ")
    password = input("Enter password: ")

    admin = get_admin(username, password)

    if admin:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

if __name__ == "__main__":
    admin_login()
