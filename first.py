students = {}

while True:
    print("\n📚 Student Marks Manager")
    print("1. Add student")
    print("2. Update marks")
    print("3. Delete student")
    print("4. View all students")
    print("5. Check student marks")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print(f"{name} added successfully ✅")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print(f"{name}'s marks updated ✅")
        else:
            print("Student not found ❌")

    elif choice == "3":
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print(f"{name} deleted ✅")
        else:
            print("Student not found ❌")

    elif choice == "4":
        if students:
            print("\n📖 All Students:")
            for name, marks in students.items():
                print(f"{name} : {marks}")
        else:
            print("No students found 🫠")

    elif choice == "5":
        name = input("Enter student name: ")
        if name in students:
            print(f"{name}'s marks: {students[name]}")
        else:
            print("Student not found ❌")

    elif choice == "6":
        print("Exiting program... 🫡")
        break

    else:
        print("Invalid choice. Please enter 1-6 😅")