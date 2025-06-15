from utils import *
from collections import defaultdict

expenses = defaultdict(list)

def add_expense():
    cls()
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    try:
        amount = int(input("Enter amount: "))
    except ValueError:
        cls()
        print("Invalid amount. Please enter a number.\n")
        return

    expenses[date].append({"category": category, "amount": amount})
    cls()
    print("Expense added\n")

def view_all_expenses():
    cls()
    if not expenses:
        print("No expenses recorded.\n")
        return

    for date in expenses:
        print(f"{date}:")
        for item in expenses[date]:
            print(f"  - {item['category']}: Rs. {item['amount']}")
    print()

def view_by_category():
    cls()
    category = input("Enter category: ")
    total = 0
    for date in expenses:
        for item in expenses[date]:
            if item["category"].lower() == category.lower():
                total += item["amount"]
    print(f"Total spent on {category}: Rs. {total}\n")

def view_by_date():
    cls()
    date = input("Enter date (YYYY-MM-DD): ")
    if date not in expenses:
        print("No expenses found for this date.\n")
        return

    print(f"Expenses on {date}:")
    for item in expenses[date]:
        print(f"  - {item['category']}: Rs. {item['amount']}")
    print()

while True:
    action = choice("Daily Expense Tracker", [
        "Add Expense",
        "View All Expenses",
        "View by Category",
        "View by Date",
        "Exit"
    ])

    if action == "Add Expense":
        add_expense()
    elif action == "View All Expenses":
        view_all_expenses()
    elif action == "View by Category":
        view_by_category()
    elif action == "View by Date":
        view_by_date()
    elif action == "Exit":
        cls()
        print("Goodbye!\n")
        break
