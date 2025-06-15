from utils import *

courses = {
    "Python": {"seats": 3, "students": []},
    "AI": {"seats": 2, "students": []},
    "Data Science": {"seats": 4, "students": []},
    "Web Development": {"seats": 5, "students": []}
}

def view_courses():
    cls()
    for course in courses:
        seats_left = courses[course]["seats"] - len(courses[course]["students"])
        print(f"{course} - Seats Left: {seats_left}")
    print()

def enroll_student():
    cls()
    available_courses = [course for course in courses if len(courses[course]["students"]) < courses[course]["seats"]]
    
    if not available_courses:
        print("No courses available for enrollment.\n")
        return

    course = choice("Choose course to enroll", available_courses)
    name = input("Enter student name: ")

    if len(courses[course]["students"]) < courses[course]["seats"]:
        courses[course]["students"].append(name)
        cls()
        print(f"{name} enrolled in {course}\n")
    else:
        cls()
        print("No seats available in that course.\n")

def drop_course():
    cls()
    enrolled_courses = [course for course in courses if courses[course]["students"]]
    
    if not enrolled_courses:
        print("No enrolled students to drop.\n")
        return

    course = choice("Choose course to drop from", enrolled_courses)
    students = courses[course]["students"]

    if not students:
        print("No students in this course.\n")
        return

    student = choice("Select student to remove", students)
    courses[course]["students"].remove(student)
    cls()
    print(f"{student} has been dropped from {course}\n")

def view_students():
    cls()
    for course in courses:
        students = courses[course]["students"]
        print(f"Enrolled Students in {course}: {students}")
    print()

while True:
    action = choice("Welcome to Online Courses", [
        "View Courses",
        "Enroll Student",
        "Drop Course",
        "View Enrolled Students",
        "Exit"
    ])

    if action == "View Courses":
        view_courses()
    elif action == "Enroll Student":
        enroll_student()
    elif action == "Drop Course":
        drop_course()
    elif action == "View Enrolled Students":
        view_students()
    elif action == "Exit":
        cls()
        print("Goodbye!\n")
        break
