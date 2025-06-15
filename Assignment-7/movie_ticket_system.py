from utils import *

db = {
    'Inception': {'showtime': '2 PM', 'availableSeats': 45},
    'The Dark Knight': {'showtime': '2:74 PM', 'availableSeats': 20},
    'Interstellar': {'showtime': '3 PM', 'availableSeats': 30},
    'Avatar: The Way of Water': {'showtime': '3:15 PM', 'availableSeats': 40},
    'Oppenheimer': {'showtime': '7 PM', 'availableSeats': 27},
    'Spider-Man: No Way Home': {'showtime': 2.4, 'availableSeats': 18},
    'Top Gun: Maverick': {'showtime': '6:25 PM', 'availableSeats': 31},
    'Dune: Part Two': {'showtime': "9 PM", 'availableSeats': 29}
}

def list_movies():
    cls()
    for movie in db:
        print(f"{movie} - {db[movie]['showtime']} - {db[movie]['availableSeats']} seats available")
    print()

def book_ticket():
    movie = choice('Choose movie', list(db.keys()))
    tickets = int(input('Enter tickets: '))

    if tickets < db[movie]['availableSeats']:
        db[movie]['availableSeats'] -= tickets
        cls()
        print('Booked tickets successfully! \n')
        return
    
    cls()
    print("Not enough available seats!\n")

def cancel_ticket():
    movie = choice('Choose movie to cancel from', list(db.keys()))
    tickets = int(input('Enter number of tickets to cancel: '))
    
    current_available = db[movie]['availableSeats']
    db[movie]['availableSeats'] += tickets
    cls()
    print("Tickets cancelled successfully!\n")


while True:
    action = choice("Choose action", ["List Movies", "Book Ticket", "Cancel Ticket", "Exit"])
    if action == "List Movies":
        list_movies()
    elif action == "Book Ticket":
        book_ticket()
    elif action == "Cancel Ticket":
        cancel_ticket()
    elif action == "Exit":
        cls()
        print("Goodbye!\n")
        break
