# Task 17: Bus Ticket Booking
# Topics: Branching, loops, dictionaries

import datetime

def create_bus(total_seats=20):
    seats = {}
    for i in range(1, total_seats + 1):
        seats[i] = {"status": "Available", "passenger": None, "booking_date": None}
    return seats

def show_available_seats(seats):
    available = [str(s) for s, info in seats.items() if info["status"] == "Available"]
    print(f"  Available Seats ({len(available)}): {', '.join(available)}")

def book_seat(seats, seat_no, passenger_name):
    if seat_no not in seats:
        return False, f"Seat {seat_no} does not exist."
    if seats[seat_no]["status"] == "Booked":
        return False, f"Seat {seat_no} is already booked."
    seats[seat_no]["status"]       = "Booked"
    seats[seat_no]["passenger"]    = passenger_name.strip()
    seats[seat_no]["booking_date"] = str(datetime.date.today())
    return True, f"Seat {seat_no} booked for {passenger_name}."

def print_ticket(seats, seat_no):
    if seat_no not in seats or seats[seat_no]["status"] != "Booked":
        print("  No ticket found for this seat.")
        return
    info = seats[seat_no]
    print("=" * 40)
    print("         BUS TICKET")
    print("=" * 40)
    print(f"  Passenger    : {info['passenger']}")
    print(f"  Seat Number  : {seat_no}")
    print(f"  Booking Date : {info['booking_date']}")
    print(f"  Status       : {info['status']}")
    print("=" * 40)

# Test Section
if __name__ == "__main__":
    bus = create_bus(20)

    # Test Case 1: Show available seats
    print("Test Case 1: Available Seats")
    show_available_seats(bus)
    print()

    # Test Case 2: Book seats
    print("Test Case 2: Book Seats")
    ok, msg = book_seat(bus, 5, "Vinod Miyani")
    print(f"  {msg}")
    ok, msg = book_seat(bus, 10, "Priya Sharma")
    print(f"  {msg}")
    ok, msg = book_seat(bus, 5, "Duplicate Attempt")
    print(f"  {msg}")
    print()

    # Test Case 3: Print ticket
    print("Test Case 3: Print Ticket for Seat 5")
    print_ticket(bus, 5)
