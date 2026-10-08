class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.honor_roll = False

    def add_grade(self, grade):
        if not isinstance(grade, (int, float)):
            print("Error: The grade must be a number.")
            return

        if grade < 0 or grade > 100:
            print("Error: The grade must be between 0 and 100.")
            return

        self.grades.append(grade)

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0

        total = 0

        for grade in self.grades:
            total += grade

        return total / len(self.grades)

    def get_letter_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def check_passed(self):
        return self.calculate_average() >= 60

    def check_honor_roll(self):
        self.honor_roll = self.calculate_average() >= 90

    def remove_grade_by_value(self, grade):
        if grade in self.grades:
            self.grades.remove(grade)
            print("Grade removed successfully.")
        else:
            print("Error: The grade does not exist.")

    def remove_grade_by_index(self, index):
        if index >= 0 and index < len(self.grades):
            del self.grades[index]
            print("Grade removed successfully.")
        else:
            print("Error: The grade index is out of bounds.")

    def report(self):
        average = self.calculate_average()
        letter_grade = self.get_letter_grade()
        passed = self.check_passed()
        self.check_honor_roll()

        if passed:
            pass_status = "Passed"
        else:
            pass_status = "Failed"

        if self.honor_roll:
            honor_status = "True"
        else:
            honor_status = "False"

        print("Student ID: " + str(self.student_id))
        print("Student Name: " + self.name)
        print("Number of Grades: " + str(len(self.grades)))
        print("Average Grade: " + str(average))
        print("Letter Grade: " + letter_grade)
        print("Pass/Fail: " + pass_status)
        print("Honor Roll: " + honor_status)


def create_student(student_id, name):
    if student_id == "":
        print("Error: Student ID cannot be empty.")
        return None

    if name == "":
        print("Error: Student name cannot be empty.")
        return None

    return Student(student_id, name)


def start_run():
    student = create_student("001", "Henry")

    if student is not None:
        student.add_grade(100)
        student.add_grade(50)

        student.report()


start_run()
