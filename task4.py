# task4.py

def parse_input(user_input: str):
    """
    Розбиває введення на команду та аргументи.
    Повертає кортеж: (command, [args...])
    """
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args


def add_contact(args, contacts: dict) -> str:
    """add <name> <phone> — додає/перезаписує контакт"""
    if len(args) != 2:
        return "Помилка: використайте формат: add <ім'я> <телефон>."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts: dict) -> str:
    """change <name> <phone> — змінює телефон існуючого контакту"""
    if len(args) != 2:
        return "Помилка: використайте формат: change <ім'я> <новий_телефон>."
    name, phone = args
    if name not in contacts:
        return "Помилка: контакт не знайдено."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts: dict) -> str:
    """phone <name> — показує телефон контакту"""
    if len(args) != 1:
        return "Помилка: використайте формат: phone <ім'я>."
    name = args[0]
    if name not in contacts:
        return "Помилка: контакт не знайдено."
    return contacts[name]


def show_all(contacts: dict) -> str:
    """all — показує всі контакти"""
    if not contacts:
        return "Список контактів порожній."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        elif command == "":
            # порожній ввід — просто ігноруємо
            continue

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
