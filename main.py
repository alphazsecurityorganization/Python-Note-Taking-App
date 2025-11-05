#Note Taking App
File_name = "mynote.txt"

def main_menu():
    print("---- Note Taking App ----")
    print(f"1. Add a New Note")
    print(f"2. View All Note")
    print(f"3. Delete All Notes")
    print(f"4. Exit")

def Add_note():
    note = input("Enter Your Note: ")
    with open(File_name, "a") as File:
        File.write(note + "\n")
    print("Note Added SuccessFully")

def view_note():
    try:
        with open(File_name , "r") as File:
            contant = File.read()
            if contant:
                print("\n-----Your Notes-----")
                print(contant)
            else:
                print("I Dont Have Any Notes")
    except FileNotFoundError:
        print("No Notes Founds")



#main
while True:
    main_menu()
    user_input = int(input("Choice A Number (1 - 4): "))
    if user_input > 5 or user_input < 1:
        print("Invelid Number. Try Again")

    elif ( user_input == 1):
        Add_note()
    elif ( user_input == 2 ):
        view_note()
    elif ( user_input == 3 ):
        with open(File_name , "w") as File:
            File.write("")
        print("All Notes Deleted")
    elif (user_input == 4):
        break
    else:
        print("None")
