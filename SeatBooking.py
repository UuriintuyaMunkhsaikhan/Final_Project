# Seat-Booking Application

# Function to check the availability of a seat
def check_seat_availability():
    # Implement the logic to check the availability of a seat
    pass

# Function to book a seat
def book_seat():
    # Implement the logic to book a seat
    pass

# Function to free a seat
def free_seat():
    # Implement the logic to free a seat
    pass

# Function to show the booking state
def show_booking_state():
    # Implement the logic to display the booking state
    pass

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