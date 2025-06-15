from utils import *

cars = {
    "Honda Civic": {"available": True, "renter": None},
    "Toyota Corolla": {"available": True, "renter": None},
    "Suzuki Alto": {"available": True, "renter": None},
    "Hyundai Elantra": {"available": True, "renter": None},
    "Kia Sportage": {"available": True, "renter": None}
}

def view_available_cars():
    cls()
    available = [car for car in cars if cars[car]["available"]]
    if available:
        print("Available Cars:\n - " + "\n - ".join(available) + "\n")
    else:
        print("No cars available at the moment.\n")

def rent_car():
    cls()
    available = [car for car in cars if cars[car]["available"]]
    if not available:
        print("No cars available to rent.\n")
        return

    car = choice("Choose a car to rent", available)
    name = input("Enter your name: ")

    cars[car]["available"] = False
    cars[car]["renter"] = name
    cls()
    print(f"Car rented successfully to {name}\n")

def return_car():
    cls()
    rented = [car for car in cars if not cars[car]["available"]]
    if not rented:
        print("No rented cars to return.\n")
        return

    car = choice("Choose a car to return", rented)
    cars[car]["available"] = True
    cars[car]["renter"] = None
    cls()
    print("Car returned successfully!\n")

def view_rentals():
    cls()
    rented = [(car, cars[car]["renter"]) for car in cars if not cars[car]["available"]]
    if rented:
        print("Rented Cars:")
        for car, renter in rented:
            print(f"- {car} -> {renter}")
        print()
    else:
        print("No active rentals.\n")

while True:
    action = choice("Choose Option", [
        "View Available Cars",
        "Rent a Car",
        "Return a Car",
        "View All Rentals",
        "Exit"
    ])
    
    if action == "View Available Cars":
        view_available_cars()
    elif action == "Rent a Car":
        rent_car()
    elif action == "Return a Car":
        return_car()
    elif action == "View All Rentals":
        view_rentals()
    elif action == "Exit":
        cls()
        print("Thank you for using the Car Rental System!\n")
        break
