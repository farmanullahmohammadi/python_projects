from typing import TypeVar, Generic

T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def add(self, item: T):
        self.items.append(item)

    def get_all(self) -> list[T]:
        return self.items.copy()


class StudentManager:

    def __init__(self):
        self.students: dict[int, dict] = {}

    def add_student(self, sid, name):
        if sid not in self.students:
            self.students[sid] = {
                "name": name,
                "courses": set()
            }
            print("Student Added")
        else:
            print("ID already exists")

    def register_course(self, sid, course):
        if sid in self.students:
            self.students[sid]["courses"].add(course)

    def drop_course(self, sid, course):
        if sid in self.students:
            self.students[sid]["courses"].discard(course)

    def search_student(self, sid):
        return self.students.get(sid, "Student Not Found")

    def unique_courses(self):
        courses = set()

        for student in self.students.values():
            courses.update(student["courses"])

        return courses

    def students_by_course(self, course):
        return [
            student["name"]
            for student in self.students.values()
            if course in student["courses"]
        ]

    def display_sorted(self):
        for sid, student in sorted(
            self.students.items(),
            key=lambda x: x[1]["name"]
        ):
            print(sid, student)


# Create Manager
manager = StudentManager()

# Add Students
manager.add_student(101, "Ahmad")
manager.add_student(102, "Sara")
manager.add_student(103, "Ali")

# Register Courses
manager.register_course(101, "Python")
manager.register_course(101, "Java")

manager.register_course(102, "Python")
manager.register_course(102, "Database")

manager.register_course(103, "Java")

# Drop Course
manager.drop_course(101, "Java")

# Search
print("\nSearch Student:")
print(manager.search_student(101))

# Unique Courses
print("\nUnique Courses:")
print(manager.unique_courses())

# Students Sharing Course
print("\nStudents in Python:")
print(manager.students_by_course("Python"))

# Sort Students
print("\nSorted Students:")
manager.display_sorted()

# Generic Box Example
box = Box[str]()
box.add("Advanced Programming")
box.add("Python")

print("\nGeneric Box:")
print(box.get_all())