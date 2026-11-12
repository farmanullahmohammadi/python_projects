import json
from pathlib import Path

FILE = Path("students.json")


def load_students():
    try:
        with open(FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Invalid JSON file")
        return []


def save_students(students):
    if FILE.exists():
        backup = FILE.with_name("students_backup.json")
        backup.write_text(FILE.read_text(encoding="utf-8"),
                          encoding="utf-8")

    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def add_student():
    students = load_students()

    sid = input("Student ID: ").strip()
    name = input("Name: ").strip()
    department = input("Department: ").strip()
    semester = input("Semester: ").strip()

    if not sid or not name or not department or not semester:
        print("All fields are required")
        return

    if any(s["id"] == sid for s in students):
        print("ID already exists")
        return

    students.append({
        "id": sid,
        "name": name,
        "department": department,
        "semester": semester
    })

    save_students(students)
    print("Student Added")


def list_students():
    for student in load_students():
        print(student)


def search_student():
    sid = input("Enter ID: ").strip()

    for student in load_students():
        if student["id"] == sid:
            print(student)
            return

    print("Student Not Found")


def update_student():
    students = load_students()
    sid = input("Enter ID: ").strip()

    for student in students:
        if student["id"] == sid:
            student["name"] = input("New Name: ").strip()
            student["department"] = input("New Department: ").strip()
            student["semester"] = input("New Semester: ").strip()

            save_students(students)
            print("Updated")
            return

    print("Student Not Found")


def delete_student():
    students = load_students()
    sid = input("Enter ID: ").strip()

    new_students = [s for s in students if s["id"] != sid]

    if len(new_students) == len(students):
        print("Student Not Found")
        return

    save_students(new_students)
    print("Deleted")


while True:
    print("\n1. Add Student")
    print("2. List Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        list_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        break
    else:
        print("Invalid Choice")