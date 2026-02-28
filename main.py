import mysql.connector
import database 
import crud
from colorama import Fore, Style, init

init(autoreset=True)


def menu():
    while True:
        print("\n" + Fore.CYAN + "="*70)
        print(Fore.CYAN + "          🎓 STUDENT MANAGEMENT SYSTEM 🎓")
        print(Fore.CYAN + "="*70)
        print(Fore.YELLOW + "1. ➕ ADD STUDENTS")
        print(Fore.YELLOW + "2. 👀 VIEW STUDENTS")
        print(Fore.YELLOW + "3. ✏️  UPDATE GRADES")
        print(Fore.YELLOW + "4. 🗑️  DELETE STUDENTS")
        print(Fore.YELLOW + "5. 🚪 EXIT")
        print(Fore.CYAN + "-"*70)

        choice = input(Fore.WHITE + "Enter choice: ")
    
        if choice == "1":
            print(Fore.CYAN + "\n--- Add New Student ---")
            name = input("Enter the Name: ")
            age = input("Enter the Age: ")
            grade = input("Enter the grade: ")
            email = input("Enter the email: ")

            result = crud.add_student(name, age, grade, email)

            if result == 0:
                print(Fore.RED + "✗ Insert Failed")
            else:
                print(Fore.GREEN + "✓ Student added Successfully")
        

        elif choice == "2":
            students = crud.view_student()

            if not students:
                print(Fore.YELLOW + "\n⚠ No students found in the database.")
                print(Fore.CYAN + "Automatically resetting ID counter to 1...")
                database.reset_auto_increment()
            else:
                print("\n" + Fore.CYAN + "="*70)
                print(Fore.CYAN + f"{'ID':<5} {'Name':<20} {'Age':<5} {'Grade':<7} {'Email':<30}")
                print(Fore.CYAN + "-"*70)

                for s in students:
                    print(Fore.WHITE + f"{s['id']:<5} {s['name']:<20} {s['age']:<5} {s['grade']:<7} {s['email']:<30}")

                print(Fore.CYAN + "="*70)
                print(Fore.GREEN + f"Total Students: {len(students)}")


        elif choice == "3":
            print(Fore.CYAN + "\n--- Update Student Grade ---")
            student_id = input("Enter Student ID: ")
            new_grade = input("Enter New Grade: ")
            
            result = crud.update_student_grade(new_grade, student_id)
            
            if result == 0:
                print(Fore.RED + "✗ Student with ID not found")
            else:
                print(Fore.GREEN + "✓ Grade updated Successfully.")        


        elif choice == "4":
            print(Fore.CYAN + "\n--- Delete Student ---")
            student_id = input("Enter Student ID: ")
            confirm = input(Fore.YELLOW + f"⚠ Do you want to delete STUDENT with ID: {student_id}? (YES or NO): ").lower()
            
            if confirm == "yes":
                result = crud.delete_student(student_id)
                if result == 0:
                    print(Fore.RED + "✗ Student with ID not found")
                else:
                    print(Fore.GREEN + "✓ Student Deleted Successfully.")

                    students = crud.view_student()
                    if not students:
                        print(Fore.YELLOW + "\n⚠ Table is now empty. Resetting ID counter...")
                        database.reset_auto_increment()
            else:
                print(Fore.YELLOW + "Delete operation cancelled.")


        elif choice == "5":
            print("\n" + Fore.CYAN + "="*70)
            print(Fore.GREEN + "Thank you for using Student Management System! 👋")
            print(Fore.CYAN + "Exiting...")
            print(Fore.CYAN + "="*70)
            break
        
        else:
            print(Fore.RED + "✗ Invalid choice. Please enter a number between 1-5.")


if __name__ == "__main__":
    try:
        database.create_table()
        menu()
    except Exception as e:
        print(Fore.RED + f"Fatal error: {e}")