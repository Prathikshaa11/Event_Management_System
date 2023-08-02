from database import insert_staff, get_staffs

class Staff:
    def __init__(self, event_name,staff_name, staff_role):
        self.event_name = event_name
        self.staff_name = staff_name
        self.staff_role = staff_role

    def to_list(self):
        return [self.event_name, self.staff_name, self.staff_role]

def add_staff(staffs):
    print("Add Staff to Event")
    event_name = input("Enter event name: ")
    staff_name = input("Enter staff name: ")
    staff_role = input("Enter staff role: ")

    staff = Staff(event_name, staff_name, staff_role)
    insert_staff(staff.event_name, staff.staff_name, staff.staff_role)
    staffs.append(staff.to_list())
    print("Staff added successfully!")

def view_staff(staffs):
    print("View Staff of an Event")
    event_name = input("Enter event name: ")

    for staff in staffs:
        if staff[0] == event_name:
            print(f"Staff Name: {staff[1]}")
            print(f"Staff Role: {staff[2]}")
            print()

if __name__ == "__main__":
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
