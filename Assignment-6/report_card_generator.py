from utils import *
from prettytable import PrettyTable

students = {}

subjects = ["Math", "Physics", "Chemistry", "English", "History"]

def grade_from_average(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def print_line(char='-', length=50):
    print(char * length)

def print_centered(text, length=50):
    print(f"|{text:^{length-2}}|")

def add_student():
    print_with_clear("\033[1;31mAdd Student\033[0m")
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    marks = []
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter marks for {subject}: "))
                if 0 <= mark <= 100:
                    break
            except ValueError:
                pass
            print("Enter valid marks between 0 and 100.")
        marks.append(mark)
    students[name] = {"roll": roll, "marks": marks}
    print(f"Added student {name}.")

def generate_report_card():
    print_with_clear("\033[1;31mStudent Report Cards\033[0m")
    if not students:
        print("No students entered.")
        return

    for name, info in students.items():
        total = sum(info["marks"])
        avg = total / len(info["marks"])
        grade = grade_from_average(avg)

        table = PrettyTable()
        table.title = f"Report Card: {name} (Roll No: {info['roll']})"
        table.field_names = ["Subject", "Marks", "Grade"]
        for subject, mark in zip(subjects, info["marks"]):
            table.add_row([subject, mark, grade_from_average(mark)])
        table.add_row(["-"*7, "-"*5, "-"*5])
        table.add_row(["Total", total, ""])
        table.add_row(["Average", f"{avg:.2f}", grade])
        print(table)
        print()

    input("Press Enter to continue...")

def generate_report_card_plain():
    print("\033[1;31mStudent Report Cards\033[0m")
    if not students:
        print("No students entered.")
        return
    for name, info in students.items():
        total = sum(info["marks"])
        avg = total / len(info["marks"])
        grade = grade_from_average(avg)
        print(f"Name: {name}")
        print(f"Roll Number: {info['roll']}")
        print(f"Marks: {info['marks']}")
        print(f"Total: {total}")
        print(f"Average: {avg:.2f}")
        print(f"Grade: {grade}")
        print("-" * 20)

while True:
    option = choose_option("Student Report Card Generator", ["Add Student", "Generate Report Cards", "Exit"], "Choose an option: ")
    if option == "Add Student":
        add_student()
    elif option == "Generate Report Cards":
        generate_report_card()
    elif option == "Exit":
        break
    else:
        print("Invalid input")
