import datetime


class Person:
    def __init__(self, name):
        self.name = name
        self.birthday = None

    def set_birthday(self, birthdate):
        self.birthday = birthdate

    def get_age_days(self):
        if self.birthday is None:
            raise ValueError("Birthday not set")
        return (datetime.date.today() - self.birthday).days

    def get_age_years(self):
        if self.birthday is None:
            raise ValueError("Birthday not set")
        return self.get_age_days() / 365

    def get_birthday(self):
        return self.birthday

    def get_name(self):
        return self.name


class Student(Person):
    def __init__(self, name, id_number, student_class):
        super().__init__(name)
        self.id_number = id_number
        self.student_class = student_class
        self.major = None
        self.grade_book = {}

    def set_major(self, major):
        self.major = major

    def add_assignment(self, assignment_name, score):
        if assignment_name in self.grade_book:
            raise ValueError("Assignment already exists.")
        self.grade_book[assignment_name] = score

    def print_general_info(self):
        try:
            age = self.get_age_years()
            age_str = f"{age:.2f} years"
        except ValueError:
            age_str = "Birthday not set"

        print(f"Name: {self.get_name()}")
        print(f"Age: {age_str}")
        print(f"ID Number: {self.id_number}")
        print(f"Class: {self.student_class}")
        print(f"Major: {self.major if self.major else 'Undeclared'}")

    def print_gradebook(self):
        """Prints all assignments and grades"""
        if not self.grade_book:
            print("No assignments in the gradebook.")
        else:
            print("Assignments and Grades:")
            for assignment, score in self.grade_book.items():
                print(f"{assignment}: {score}")


# Student 1
s1 = Student("Alice", "S123", "Freshman")
s1.set_birthday(datetime.date(2005, 6, 15))
s1.set_major("Computer Science")
s1.add_assignment("Math Test", 85)
s1.add_assignment("English Essay", 90)
s1.add_assignment("Science Project", 95)
s1.print_general_info()
s1.print_gradebook()

# Student 2
s2 = Student("Bob", "S456", "Sophomore")
s2.set_birthday(datetime.date(2004, 8, 22))
s2.set_major("Mathematics")
s2.add_assignment("Calculus Exam", 88)
s2.add_assignment("History Paper", 75)
s2.add_assignment("Physics Lab", 92)
s2.print_general_info()
s2.print_gradebook()

# Student 3
s3 = Student("Charlie", "S789", "Junior")
s3.set_birthday(datetime.date(2003, 1, 10))
s3.set_major("Engineering")
s3.add_assignment("Electronics Quiz", 80)
s3.add_assignment("Thermodynamics Homework", 85)
s3.add_assignment("Design Project", 78)
s3.print_general_info()
s3.print_gradebook()

# Student 4
s4 = Student("Diana", "S101", "Senior")
s4.set_birthday(datetime.date(2002, 3, 5))
s4.set_major("Biology")
s4.add_assignment("Genetics Exam", 91)
s4.add_assignment("Chemistry Lab", 88)
s4.add_assignment("Research Paper", 94)
s4.print_general_info()
s4.print_gradebook()
