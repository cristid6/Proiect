"""Un client are nevoie de un soft pentru a gestiona mai usor reclamatiile clientilor.
Va trebuie sa implementezi un caiet de reclamatii digital.

Acest caiet are urmatoarele functionalitati:

- adaugare reclamatie
- vezi toate reclamatiile ne-rezolvate
- marcheaza o reclamatie ca "rezolvata"

NOTE:
1. fiecare reclamatie, pe langa reclamatia in sine, trebuie sa retina data la care a fost
creata si numele reclamatului.
2. fiecare reclamatie va primi un ID unic pentru a fi identificata."""

from complaints import Database


print("""COMPLAINTS DATABASE

Please use the following commmands:

add_complaint - use this command for adding a complaint (required first name, last name, title and description
select_complaint - use this command for searching a complaint by ID (requires complaint ID)
select_all - use this command for displaying all complaints
select_0 - use this command for displaying unresolved complaints (0=unresolved)
select_1 - use this command for displaying resolved complaints (1=resolved)
modify_status - use this command for changing complaint status (requires complaint ID)
help - use this command for displaying all commands
exit - use this command for exit software.\n""")

db = Database()

while True:
    if db.get_max_id() is None:
        print("Database is empty! Add a complaint.")
        command = input("Enter command:")
        if command == 'add_complaint':
            first_name = input("Enter first name:")
            last_name = input("Enter last name:")
            title = input("Enter complaint title:")
            description = input("Enter complaint description:")
            db.add_complaint(first_name, last_name, title, description)
        elif command == 'exit':
            print("Goodbye!")
            break
        else:
            print("Available commands: add_complaint, exit.")
    else:
        command = input("Enter command:")
        if command == 'add_complaint':
            db.add_complaint(input("Enter first name:"), input("Enter last name:"),
                             input("Enter complaint title:"), input("Enter complaint description:"))
        elif command == 'select_complaint':
            while True:
                try:
                    id_reg = int(input("Enter ID (integer number):"))
                    if id_reg > db.get_max_id() or id_reg == 0:
                        print("ID doesn't exist!")
                    else:
                        db.select_complaint(id_reg)
                        break
                except ValueError:
                    print("ID is not integer!")
        elif command == 'select_all':
            db.select_all()
        elif command == 'select_0':
            db.select_0()
        elif command == 'select_1':
            db.select_1()
        elif command == 'modify_status':
            status = None
            while True:
                if status is None:
                    try:
                        id_reg = int(input("Enter ID (integer number):"))
                        if 0 < id_reg <= db.get_max_id():
                            while True:
                                try:
                                    status = int(input("Enter status (0 or 1):"))
                                    if status not in [0, 1]:
                                        print("Status must be 0 or 1!")
                                    else:
                                        db.modify_status(id_reg, status)
                                        break
                                except ValueError:
                                    print("Enter only integer number!")
                        else:
                            print("ID doesn't exist!")
                    except ValueError:
                        print("Enter only integer number!")
                else:
                    break
        elif command == 'help':
            print("""Use one of the following commands:
            add_complaint
            select_complaint
            select_all
            select_0
            select_1
            modify_status
            help
            exit""")
        elif command == 'exit':
            print("Goodbye!")
            break
        else:
            print("Incorrect command!")
