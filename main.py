"""
Un client are nevoie de un soft pentru a gestiona mai usor reclamatiile clientilor.
Va trebuie sa implementezi un caiet de reclamatii digital.

Acest caiet are urmatoarele functionalitati:

- adaugare reclamatie
- vezi toate reclamatiile ne-rezolvate
- marcheaza o reclamatie ca "rezolvata"

NOTE:
1. fiecare reclamatie, pe langa reclamatia in sine, trebuie sa retina data la care a fost
creata si numele reclamatului.
2. fiecare reclamatie va primi un ID unic pentru a fi identificata.
"""

from complaints import Database


print("""COMPLAINTS DATABASE

Please use the following commmands:

add_complaint - use this command for adding a complaint (required first name, last name, title and description
select_complaint - use this command for searching a complaint by id (requires complaint id)
select_all - use this command for displaying all complaints
select_0 - use this command for displaying unresolved complaints (0=unresolved)
select_1 - use this command for displaying resolved complaints (1=resolved)
modify_status - use this command for changing complaint status (requires complaint id)
help - use this command for displaying all commands
exit - use this command for exit software.
""")

db = Database()

while True:
    status = None
    command = input("Enter command:")
    if command == 'add_complaint':
        db.add_complaint(input("Enter first name:"), input("Enter last name:"),
                         input("Enter complaint title:"), input("Enter complaint description:"))
    elif command == 'select_complaint':
        while True:
            try:
                id = int(input("Enter id (integer number):"))
                if id <= db.get_max_id():
                    db.select_complaint(id)
                    break
                else:
                    print("ID doesn't exist!")
            except ValueError:
                print("ID is not integer!")
    elif command == 'select_all':
        db.select_all()
    elif command == 'select_0':
        db.select_0()
    elif command == 'select_1':
        db.select_1()
    elif command == 'modify_status':
        while True:
            if status is not None:
                break
            try:
                id = int(input("Enter id (integer number):"))
                if id <= db.get_max_id():
                    while True:
                        try:
                            status = int(input("Enter status  (0 or 1):"))
                            if status in [0, 1]:
                                db.modify_status(id, status)
                                break
                            else:
                                print("Status must be 0 or 1!")
                        except ValueError:
                            print("Enter only integer number!")
                else:
                    print("ID doesn't exist!")
            except ValueError:
                print("Enter only integer number!")
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
