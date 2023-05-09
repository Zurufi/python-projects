import sys

"""
Ali Alzurufi

This program is designed to help users select seats on an airline flight.
The program displays a seating chart, allowing the user to view and select available seats.
Once a seat has been selected, it is marked as taken and cannot be selected again.
The program also keeps track of the number of seats available and taken, and displays this information to the user.

Date: 04/20/23

"""


class SeatSelection:
    def __init__(self, plane_seats: list):
        """Create a new SeatSelection object with the given list of plane seats.

        Args:
            plane_seats (list): A list of strings representing the seats on the plane.
        """
        self.plane_seats = plane_seats

    def business_class(self) -> bool:
        """Return True if there is at least one available business class seat, False otherwise."""
        return all(seat == "X" for seat in self.plane_seats[0:5])

    def economy_class(self) -> bool:
        """Return True if there is at least one available economy class seat, False otherwise."""
        return all(seat == "X" for seat in self.plane_seats[6:11])


def valid_business_class_seat_selection(user_input: int) -> bool:
    """Return True if user input is a valid economy class seat selection.

    Args:
        user_input (int): The user input to validate.

    Returns:
        bool: True if user input is a valid economy class seat selection, False otherwise.
    """
    try:
        return 1 <= int(user_input) <= 5
    except ValueError:
        return False


def valid_economy_class_seat_selection(user_input: int) -> bool:
    """Return True if user input is a valid economy class seat selection.

    Args:
        user_input (int): The user input to validate.

    Returns:
        bool: True if user input is a valid economy class seat selection, False otherwise.
    """
    try:
        return 6 <= int(user_input) <= 10
    except ValueError:
        return False


def valid_class_selection(user_input: int) -> bool:
    """Return True if user input is a valid row selection.

    Args:
        user_input (int): The user input to validate.

    Returns:
        bool: True if user input is a valid row selection, False otherwise.
    """
    try:
        return 1 <= int(user_input) <= 3
    except ValueError:
        return False


def menu():
    """Print the menu options for the user."""
    print("Menu")
    print("================================")
    print("{:<10}{}".format("1. Business Class", " (Seats 1 through 5)"))
    print("{:<10}{}".format("2. Economy Class", "  (Seats 6 through 10)"))
    print("3. Exit")
    print("================================")
    print()


def book_seats():
    """Run the main function for the seat booking program."""

    # Initialize the seating chart with all seats set to 'A'
    seating_chart = ["A" for seat in range(1, 11)]

    # Create a new SeatSelection object with the seating chart
    seats = SeatSelection(seating_chart)

    # Create a dictionary of available seat classes and corresponding functions
    seats_dict = {
        1: (seats.business_class, "Business Class"),
        2: (seats.economy_class, "Economy Class"),
        3: (sys.exit, None),
    }

    # Print the initial seating chart
    print(f"Seating Chart: {seating_chart}")
    print()

    # Loop until the user exits the program
    while True:
        # Display the menu and prompt the user for class selection
        menu()
        class_selection = input("Please select your class or press 3 to quit: ")
        if not valid_class_selection(class_selection):
            # Validate the user input
            print("Invalid class selection. Please try again.")
            continue
        class_selection = int(class_selection)

        # Check if there are available seats in the selected class
        seat_function, flight_class_name = seats_dict[class_selection]
        if seat_function():
            print(
                f"All {flight_class_name} seats are taken. Please choose another class."
            )
            continue

        # Determine which validation function to use based on the selected class
        if class_selection == 1:
            valid_seat_selection = valid_business_class_seat_selection
        else:
            valid_seat_selection = valid_economy_class_seat_selection

        # Loop until the user selects a valid seat in the selected class
        while True:
            # Prompt the user to select a seat
            seat_selection = input(f"Please select a seat in {flight_class_name}: ")
            if not valid_seat_selection(seat_selection):
                # Validate the user input
                print("Invalid selection. Please try again.")
                continue
            seat_selection = int(seat_selection) - 1

            # Check if the selected seat is already taken
            if seating_chart[seat_selection] == "X":
                print("This seat is taken. Please choose another seat.")
                continue

            # Book the selected seat and update the seating chart
            seating_chart[seat_selection] = "X"
            print("Seat booked!")
            break

        # Print the updated seating chart
        print(f"Seating Chart: {seating_chart}")


book_seats()
