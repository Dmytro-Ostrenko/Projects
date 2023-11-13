user = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner


@input_error
def add(*args):
    name, phone = args
    user[name] = phone
    return (f'New contact:{name} with phone:{phone} saved')
    


@input_error
def exit_handler():
    return exit()


@input_error
def hello_handler():
    return 'Hello, how can I help you?'

@input_error
def say_goodbye():
    return ('Good bye!')

@input_error
def phone(*args):
    if args:
        name = args[0]
        phone = user.get(name)
        if phone is not None:
            return f'Telefon number: {phone}'
        else:
            raise KeyError(f"No user with the name {name}")
    else:
        raise IndexError
    
    
        
    
        

@input_error
def show_all_contacts():
    if not user:
        return 'No contacts available'
    contacts_info = ""
    for name, phone in user.items():
        contacts_info += f"{name}: {phone}\n"
    return contacts_info.strip()

@input_error
def change(name, phone): 
    if name in user:
        user[name] = phone
        return f'Contact {name} with the phone {phone} changed'
    else:
        raise KeyError


def main():
    while True:
        command = input("Enter your command: ")
        command_lower = command.lower() #Робимо незалежні від регістру команди
        if command_lower == ".":
            exit_handler()
        elif command_lower in ["goodbye", "close", "exit"]:
            print(say_goodbye())
            break
        elif command_lower == "hello":
            print(hello_handler())
        elif command_lower.startswith("add"):
            list_add = command.split(' ') #розбиваємо та передаємо команди по слову
            print(add(*list_add[1:]))
        elif command_lower.startswith("phone"):
            list_phone = command.split(' ')
            print(phone(*list_phone[1:]))
        elif command_lower == "show all":
            print("All contacts:")
            print(show_all_contacts())
        elif command_lower.startswith("change"):
            list_change = command.split(' ')
            if len(list_change) == 3:
                print(change(*list_change[1:]))
            else:
                print('Give me name and phone please')
        else:
            print("Unknown command, please try again")


if __name__ == "__main__":
    main()
