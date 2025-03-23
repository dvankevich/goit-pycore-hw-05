def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Please use: add [username] [phone]"
        
    contacts[name] = phone
    return "Contact added."

def list_contacts(contacts):
    result = ""
    for name, ph_number in contacts.items():
        result = result + f"{name}: {ph_number}\n"
    if not result:
        return "Contacts list is empty."
    return result

def print_phone(args, contacts):
    if len(args) != 1:
        return "Please use: [username]"

    name = args[0]
    result = contacts.get(name)
    if not result:
        return "Contact not found!"
    return result

def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Please use: change [username] [phone]"
    result = contacts.get(name)
    if not result:
        return "Contact not found!"
    contacts[name] = phone
    return "Contact updated."

def print_help():
    help_msg='''Commands:
    all - list all records
    add [name] [phone] - add record
    change [name] [phone] - change phone number for record with [name]
    phone [name] - show phone number for record with [name]
    close, exit - exit from programm
    hello - print welcome message
    help - this help message
    '''
    return help_msg

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "help" or command == "?":
            print(print_help())
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(print_phone(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(list_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


