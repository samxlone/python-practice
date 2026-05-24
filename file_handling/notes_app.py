note = input("Enter your note: ")
def add_note():
    note = input("Enter your note: ")

    with open("file_handling/notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note saved successfully!")


def view_notes():
    print("\nYour Notes:\n")

    with open("file_handling/notes.txt", "r") as file:
        print(file.read())


while True:

    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")