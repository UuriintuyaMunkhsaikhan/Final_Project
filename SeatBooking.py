import random
import string
# Define the booking_references set
booking_references = set()

# Seat-Booking Application
def generate_booking_reference():
    while True:
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        # Check if the generated reference is unique
        if reference not in booking_references():
            return reference
# Seat availability data structure
seats = {
    '1A': 'F', '2A': 'F', '3A': 'F', '4A': 'F', '78A': 'F', '77A': 'F', '79A': 'F', '80A': 'F',
    '1B': 'F', '2B': 'F', '3B': 'F', '4B': 'F', '78B': 'F', '77B': 'F', '79B': 'F', '80B': 'F',
    '1C': 'F', '2C': 'F', '3C': 'F', '4C': 'F', '78C': 'F', '79C': 'F', '80C': 'F',
    '1D': 'F', '2D': 'F', '3D': 'F', '4D': 'F', '79D': 'F', '80D': 'F',
    '1E': 'F', '2E': 'F', '3E': 'F', '4E': 'F', '79E': 'F', '80E': 'F',
    '1F': 'F', '2F': 'F', '3F': 'F', '4F': 'F', '79F': 'F', '80F': 'F'
}
# Function to check the availability of a seat
def check_seat_availability():
    seat = input("Enter seat number: ")
    if seat in seats:
        if seats[seat] == 'F':
            print("Seat is available.")
        else:
            print("Seat is already booked.")
    else:
        print("Invalid seat number.")


# Function to book a seat
def book_seat():
    seat = input("Enter seat number: ")
    if seat in seats:
        if seats[seat] == 'F':
            passenger_name = input("Enter passenger name: ")
            seats[seat] = 'B'
            print("Seat booked for", passenger_name)
        else:
            print("Seat is already booked.")
    else:
        print("Invalid seat number.")

# Function to free a seat
def free_seat():
    seat = input("Enter seat number: ")
    if seat in seats:
        if seats[seat] == 'B':
            seats[seat] = 'F'
            print("Seat freed.")
        else:
            print("Seat is already free.")
    else:
        print("Invalid seat number.")

# Function to show the booking state
def show_booking_state():
    for seat, status in seats.items():
        print("Seat:", seat, "Status:", "Booked" if status == 'B' else "Free")

# Main program
while True:
    print("Menu:")
    print("1. Check availability of seat")
    print("2. Book a seat")
    print("3. Free a seat")
    print("4. Show booking state")
    print("5. Exit program")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_seat_availability()
    elif choice == "2":
        book_seat()
    elif choice == "3":
        free_seat()
    elif choice == "4":
        show_booking_state()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")


# Example usage
new_reference = generate_booking_reference()
booking_references.add(new_reference)
print(new_reference)