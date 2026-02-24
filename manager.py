from ast import keyword

from student import Student

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print(f"Student {student_id} already exists.")
            return
        self.students[student_id] = Student(student_id, name, age, grade)
        print(f"Added: {self.students[student_id]}")

    def remove_student(self, student_id):
        if student_id in self.students:
            print(f"Removed: {self.students[student_id]}")
            del self.students[student_id]
        else:
            print(f"Student {student_id} not found.")

    def get_student(self, student_id):
        return self.students.get(student_id, None)

    def list_all(self):
        if not self.students:
            print("No students found.")
            return
        for s in self.students.values():
            print(s)

    def top_students(self, passing_grade="B"):
        grades = ["A+", "A", "A-", "B+", "B"]
        top = [s for s in self.students.values() if s.grade in grades[:grades.index(passing_grade)+1]]
        return top
    
    def search_by_name(self, keyword):
        results = [s for s in self.students.values() if keyword.lower() in s.name.lower()]
        if not results:
            print(f"No students found with keyword: '{keyword}'")
        else:
            print(f"\n--- Search Results for '{keyword}' ---")
            for s in results:
                print(s)
        return results