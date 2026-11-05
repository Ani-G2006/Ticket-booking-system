import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(filename):
    return os.path.join(BASE_DIR, filename)

FILE = get_path("seats.json")

def save_seats(seats):
    with open(FILE, "w") as f:
        json.dump(seats, f)

def load_seats():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def valid(seats, r, c):
    return len(seats) > 0 and 0 <= r < len(seats) and 0 <= c < len(seats[0])

def show_seats(seats):
    if not seats:
        print("No seats are available.")
        return
    print("  " + " ".join(str(j) for j in range(len(seats[0]))))
    for i in range(len(seats)):
        print(f"{i} " + " ".join("X" if seats[i][j] == 1 else "O" for j in range(len(seats[i]))))
    free = sum(row.count(0) for row in seats)
    print("O = free, X = booked |", free, "seats available")


choice = int(input("1 for official use\t2 customer use\nEnter any one: "))
match choice:
    case 1:
        while True:
            ch = int(input("1 create seats\t2 see seats\t3 delete all data\t4 stop\nEnter any one: "))
            match ch:
                case 1:
                    rows = int(input("Enter number of rows (n): "))
                    cols = int(input("Enter number of columns (m): "))
                    seats = [[0] * cols for _ in range(rows)]
                    save_seats(seats)
                    print("Seats created")
                case 2:
                    show_seats(load_seats())
                case 3:
                    save_seats([])
                    print("All data is deleted")
                case 4:
                    break
                case _:
                    print("Invalid choice")

    case 2:
        seats = load_seats()
        while True:
            ch = int(input("1 book seat\t2 see seats\t3 cancel ticket\t4 stop\nEnter any one: "))
            match ch:
                case 1:
                    show_seats(seats)
                    r = int(input("Enter row: "))
                    c = int(input("Enter column: "))
                    if not valid(seats, r, c):
                        print("Invalid seat")
                    elif seats[r][c] == 1:
                        print("Seat already booked")
                    else:
                        seats[r][c] = 1
                        save_seats(seats)
                        print("Seat", r, c, "booked")
                case 2:
                    show_seats(seats)
                case 3:
                    r = int(input("Enter row: "))
                    c = int(input("Enter column: "))
                    if not valid(seats, r, c):
                        print("Invalid seat")
                    elif seats[r][c] == 0:
                        print("This seat was not booked")
                    else:
                        seats[r][c] = 0
                        save_seats(seats)
                        print("Booking cancelled")
                case 4:
                    print("Thank You")
                    break
                case _:
                    print("Invalid choice")