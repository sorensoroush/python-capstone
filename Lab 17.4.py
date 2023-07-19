from datetime import datetime
import os
import pickle


def print_header():
    current_directory = os.getcwd()
    local_username = os.getlogin()
    now = datetime.now()
    formatted_now = now.strftime("%b %d, %Y @ %X")

    print(f"Current directory: {current_directory}")
    print(f"Local username: {local_username}")
    print(f"Lab 16.4: {formatted_now}\n")


def print_menu(username):
    print("\n" + "Menu")
    print("----------------------------------------")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit the program" + "\n")
    print()
    return input(f"{username}, enter your choice: ")


def run_choice(operation, data_dict):
    name = input("Enter a name: ")
    if operation == 'create':
        if name not in data_dict:
            data_dict[name] = input("Enter email address: ")
            print("Name and address have been added")
        elif name in data_dict:
            print("Name already exists")
    elif name in data_dict:
        match operation:
            case "read":
                print(f"Name: {name}")
                print(f"Email: {data_dict[name]}")
            case "update":
                data_dict[name] = input("Enter the new address: ")
                print("Information updated")
            case "delete":
                del data_dict[name]
                print("Information deleted")
    elif name not in data_dict:
        print("The specified name was not found")


def run_menu(choice, data_dict):
    match choice:
        case "1":
            run_choice("read", data_dict)
        case "2":
            run_choice("create", data_dict)
        case "3":
            run_choice("update", data_dict)
        case "4":
            run_choice("delete", data_dict)
        case "5":
            file = open("people_data.dat", "wb")
            pickle.dump(data_dict, file)
            print("Information saved")
            return False
    return True


def main():
    print_header()

    username = input("Enter your name: ")

    people_dict = {}
    if os.path.isfile("./people_data.dat"):
        file = open("people_data.dat", "rb+")
        people_dict = pickle.load(file)
        file.close()

    running_program = True
    while running_program:
        choice = print_menu(username)
        running_program = run_menu(choice, people_dict)


if __name__ == '__main__':
    main()
