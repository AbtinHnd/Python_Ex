from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['Mongodb']
collection = db['student']


def add_student(student_id, name, age):
    collection.insert_one({"student_id": student_id, "name": name, "age": age})


def remove_student(student_id):
    collection.delete_one({"student_id": student_id})


def search_student(student_id):
    student = collection.find_one({"student_id": student_id})
    if student:
        print(student)
    else:
        print("Student not found.")


def display_student_details():
    for student in collection.find():
        print(student)


def main():
    while True:
        print("\nChoose one of these options:")
        print("1. Add student")
        print("2. Remove student")
        print("3. Search student")
        print("4. Display information")
        print("5. Exit")

        choose = input("Your choice: ")

        if choose == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            add_student(student_id, name, age)
        elif choose == "2":
            student_id = input("Enter student ID: ")
            remove_student(student_id)
        elif choose == "3":
            student_id = input("Enter student ID: ")
            search_student(student_id)
        elif choose == "4":
            display_student_details()
        elif choose == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
