# indexes
reservations = []
NAME = 0
SEAT_NUM = 1
MOVIE_TITLE = 2

def view_reservations():
    print()
    print("=" * 30)
    print("Recorded Reservations:")
    for i in range(0, len(reservations), 1):
        print(f"{i+1}: Name: {reservations[i][NAME]}")
        print(f"- Seat Number: {reservations[i][SEAT_NUM]}")
        print(f"- Movie Title: {reservations[i][MOVIE_TITLE]}")
    print("=" * 30)
    print()

def get_num_reservations():
    while True:
        try:
            num_reservations = int(input("Enter number of reservations: "))
            return num_reservations
            break
        except ValueError as ve:
            print("Enter valid number.")

def add_reservations():
    print()
    print("=" * 30)
    print("Reservation Encoding:")
    print("=" * 30)

    num_reservations = get_num_reservations()

    reservation_valid = True
    seat_number_set = set()
    i = 0

    while i < num_reservations:

        input_name = input("Enter name: ").strip().capitalize()
        input_seat_number = int(input("Enter seat number: "))

        if input_seat_number not in seat_number_set:
            seat_number_set.add(input_seat_number)
            reservation_valid = True
        else:
            print("Seat is already taken. Disregarding previous attempt.")
            reservation_valid = False
            print()
            continue

        input_movie_title = input("Enter movie title: ").strip().capitalize()
        
        if reservation_valid:
            reservations.append((input_name, input_seat_number, input_movie_title))
            i += 1
    print()

def filter_reservations_by_movie(movie_name):
    print()
    print("=" * (30 + len(movie_name) * len(movie_name)))
    print("Recorded Reservations under the movie: ", movie_name)
    for i in range(0, len(reservations), 1):
        if reservations[i][MOVIE_TITLE] == movie_name:
            print(f"{i+1}: Name: {reservations[i][NAME]}")
            print(f"- Seat Number: {reservations[i][SEAT_NUM]}")
            print(f"- Movie Title: {reservations[i][MOVIE_TITLE]}")
    print("=" * (30 + len(movie_name) * len(movie_name)))
    print()

# MAIN:
print("=" * 40)
print("Theater Reservation Logging System")
print("=" * 40)

while True:
    print("1. View Reservations")
    print("2. Add Reservations")
    print("3. Filter Reservations by Movie")
    print("4. Exit Program")

    while True:
        try:
            user_choice = int(input("Enter Choice: "))
            break
        except ValueError as ve:
            print("Enter valid choice.")
            print()

    match (user_choice):
        case 1:
            view_reservations()
        case 2:
            add_reservations()
        case 3:
            filter_reservations_by_movie(input("Enter movie to filter: "))
        case 4:
            print("Code by Ned Markus S. Basilio | CS-201")
            break
        case _:
            print("Invalid Choice.")

#print(reservations)