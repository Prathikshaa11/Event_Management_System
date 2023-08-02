from database import insert_event, get_events

class Event:
    def __init__(self, event_name, event_date, event_location):
        self.event_name = event_name
        self.event_date = event_date
        self.event_location = event_location

    def to_list(self):
        return [self.event_name, self.event_date, self.event_location]

class ConcertEvent(Event):
    def __init__(self, event_name, event_date, event_location, artist):
        super().__init__(event_name, event_date, event_location)
        self.artist = artist

    def to_list(self):
        event_list = super().to_list()
        event_list.append(self.artist)
        return event_list

def add_event(events):
    print("Add Event")
    event_name = input("Enter event name: ")
    event_date = input("Enter event date (YYYY-MM-DD): ")
    event_location = input("Enter event location: ")

    event_type = input("Enter event type (1. Regular Event, 2. Concert Event): ")
    if event_type == '1':
        event = Event(event_name, event_date, event_location)
    elif event_type == '2':
        artist = input("Enter artist name: ")
        event = ConcertEvent(event_name, event_date, event_location, artist)
    else:
        print("Invalid event type.")
        return

    insert_event(event.event_name, event.event_date, event.event_location, event.artist if event_type == '2' else None)
    events.append(event.to_list())
    print("Event added successfully!")

def view_events(events):
    print("View Events")

    for event in events:
        if len(event) == 3:
            print(f"Event Name: {event[0]}")
            print(f"Event Date: {event[1]}")
            print(f"Event Location: {event[2]}")
        elif len(event) == 4:
            print(f"Event Name: {event[0]}")
            print(f"Event Date: {event[1]}")
            print(f"Event Location: {event[2]}")
            print(f"Artist: {event[3]}")
        print()

def delete_event(events):
    print("Delete Event")
    event_name = input("Enter event name: ")

    deleted = False

    for event in events:
        if event[0] == event_name:
            events.remove(event)
            deleted = True
            break

    if deleted:
        print("Event deleted successfully!")
    else:
        print("Event not found.")

def set_ticket_fare(events):
    print("Set Ticket Fare")
    event_name = input("Enter event name: ")

    for event in events:
        if event[0] == event_name:
            ticket_fare = input("Enter ticket fare for the event: ")
            event.append(ticket_fare)
            print(f"Ticket fare set for {event_name}: {ticket_fare}")
            return

    print("Event not found.")

if __name__ == "__main__":
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
