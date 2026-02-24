from manager import StudentManager

def main():
    sm = StudentManager()

    # Add students
    sm.add_student(1, "Alice Johnson", 20, "A")
    sm.add_student(2, "Bob Smith", 22, "B+")
    sm.add_student(3, "Charlie Brown", 21, "C")
    sm.add_student(4, "Diana Prince", 23, "A-")

    print("\n--- All Students ---")
    sm.list_all()

    print("\n--- Update Grade ---")
    student = sm.get_student(3)
    if student:
        student.update_grade("B")

    print("\n--- Top Students ---")
    for s in sm.top_students("B"):
        print(s)

    print("\n--- Remove Student ---")
    sm.remove_student(2)

    print("\n--- Final List ---")
    sm.list_all()
    
    print("\n--- Search Student ---")
    sm.search_by_name("alice")
if __name__ == "__main__":
    main()
