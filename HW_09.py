def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please enter name and phone number separated by a space."
        except IndexError:
            return "Invalid input. Please enter name and phone number separated by a space."
    return inner

contacts = {}

@input_error
def add_contact(contact_info):
    name, phone = contact_info.split(' ')
    contacts[name] = phone
    return "Contact added successfully."

@input_error
def change_phone(contact_info):
    name, phone = contact_info.split(' ')
    contacts[name] = phone
    return "Phone number updated successfully."

@input_error
def show_phone(name):
    return contacts[name]

def show_all_contacts():
    if len(contacts) == 0:
        return "No contacts found."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def command_parser(command):
    command = command.strip()

    if command == "hello":
        return "How can I help you?"
    elif command.startswith("add"):
        contact_info = command[4:]
        return add_contact(contact_info)
    elif command.startswith("change"):
        contact_info = command[7:]
        return change_phone(contact_info)
    elif command.startswith("phone"):
        name = command[6:]
        return show_phone(name)
    elif command == "show all":
        return show_all_contacts()
    else:
        return "Invalid command. Please try again."

def process_command(command):
    if command in ["good bye", "close", "exit"]:
        print("Good bye!")
        return False

    result = command_parser(command)
    print(result)
    return True

def main():
    print("How can I help you?")
    
    while True:
        command = input("> ").lower()
        
        if not process_command(command):
            break

if __name__ == "__main__":
    main()

