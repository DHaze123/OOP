# Part 1: Class Definition

class Student:
    # Constructor to initialize student attributes
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades

    # Method to add a new grade
    def add_grade(self, grade):
        self.grades.append(grade)

    # Method to calculate average grade
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    # Method to display student information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade():.2f}")
        print("-" * 40)

    # Part 4: Return grades as a tuple
    def grades_tuple(self):
        return tuple(self.grades)


# Part 2: Working with Objects

# Create 3 student objects
student1 = Student("Alice Johnson", "alice@example.com", [85, 90, 88])
student2 = Student("Bob Smith", "bob@example.com", [78, 82, 80])
student3 = Student("Charlie Brown", "charlie@example.com", [92, 95, 91])

# Add 2 new grades to each student
student1.add_grade(93)
student1.add_grade(87)

student2.add_grade(84)
student2.add_grade(79)

student3.add_grade(96)
student3.add_grade(94)

# Display student information
student1.display_info()
student2.display_info()
student3.display_info()


# Part 3: Dictionary & Set Integration

# Create dictionary mapping emails to Student objects
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

# Function to safely get student by email
def get_student_by_email(email):
    return student_dict.get(email, "Student not found")


# Example dictionary lookup
print(get_student_by_email("alice@example.com"))
print(get_student_by_email("unknown@example.com"))

# Create a set of all unique grades
unique_grades = set()

for student in student_dict.values():
    unique_grades.update(student.grades)

print("\nUnique Grades:", unique_grades)


# Part 4: Tuple Practice

# Convert grades to tuple
grades_tuple = student1.grades_tuple()
print("\nGrades Tuple:", grades_tuple)

# Demonstrate tuple immutability
try:
    grades_tuple[0] = 100
except TypeError as e:
    print("Tuples are immutable:", e)


# Part 5: List Operations

# Remove last grade from each student
student1.grades.pop()
student2.grades.pop()
student3.grades.pop()

# Print first and last grade, and number of grades
for student in [student1, student2, student3]:
    print(f"\n{student.name}")
    print("First Grade:", student.grades[0])
    print("Last Grade:", student.grades[-1])
    print("Number of Grades:", len(student.grades))