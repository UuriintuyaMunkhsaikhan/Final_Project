import random
import string
# Define the booking_references set
booking_references = set()

# Function to generate a random booking reference
def generate_booking_reference():
    reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    while reference in booking_references:
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return reference

# Customer data structure to store information based on booking reference
customer_data = {}

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
            passport_number = input("Enter passport number: ")
            seat_row = seat[:-1]
            seat_column = seat[-1]
            reference = generate_booking_reference()  # Generate a unique booking reference
            seats[seat] = reference  # Update seat status to the booking reference
            customer_data[reference] = {
                'passenger_name': passenger_name,
                'passport_number': passport_number,
                'seat_row': seat_row,
                'seat_column': seat_column
            }  # Store customer information based on booking reference
            booking_references.add(reference)
            print("Seat booked for {} with reference {}".format(passenger_name, reference))
        else:
            print("Seat is already booked.")
    else:
        print("Invalid seat number.")

# Function to free a seat
def free_seat():
    seat = input("Enter seat number: ")
    if seat in seats:
        if seats[seat] != 'F':
            reference = seats[seat]   # Get the booking reference associated with the seat
            del customer_data[reference]  # Remove customer information based on booking reference
            seats[seat] = 'F'   # Update seat status to free
            booking_references.remove(reference)   # Remove booking reference from set of references
            print("Seat freed.")
        else:
            print("Seat is already free.")
    else:
        print("Invalid seat number.")

# Function to show the booking state
def show_booking_state():
    for seat, status in seats.items():
        if status == 'F':
            print("Seat:", seat, "Status: Free")
        elif status in booking_references:
            customer = customer_data[status]
            print("Seat:", seat, "Status: Booked")
            print("Passenger Name:", customer['passenger_name'])
            print("Passport Number:", customer['passport_number'])
            print("Seat Row:", customer['seat_row'])
            print("Seat Column:", customer['seat_column'])
        else:
            print("Seat:", seat, "Status: Invalid")

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
check_seat_availability()
book_seat("2A", "uuriintuya", "23")
free_seat()
show_booking_state()