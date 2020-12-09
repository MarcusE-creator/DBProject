import Controllers.employee_controller as ec
import Controllers.store_controller as sc
from Data.repositories.store_repository import find_store_by_id
from UI.tools import int_input


def edit_employee(chosen_employee):
    while True:
        print("------------------")
        print(f"REDIGERA ANSTÄLLD")
        print(f"1. Namn: {chosen_employee.name}")
        print(f"2. Butik: {chosen_employee.store}")
        print(f"3. Telefonnummer: {chosen_employee.phone}")
        print(f"4. Email: {chosen_employee.email}")
        print(f"5. Jobtitel: {chosen_employee.job_title}")
        print(f"6. Avbryt")
        print(f"Vilken rad vill du redigera?")
        selected = int_input("> ")

        if selected == 1:
            chosen_employee.name = input("Ange nytt namn: ")
            ec.save_changes(chosen_employee)
            changed_string = ec.save_changes(chosen_employee)
            print(changed_string)

        elif selected == 2:
            chosen_employee.store = input("Ange ny butik (Ange butikens id): ")
            ec.save_changes(chosen_employee)
            changed_string = ec.save_changes(chosen_employee)
            print(changed_string)

        elif selected == 3:
            chosen_employee.phone = input("Ange nytt telefonnummer: ")
            ec.save_changes(chosen_employee)
            changed_string = ec.save_changes(chosen_employee)
            print(changed_string)

        elif selected == 4:
            chosen_employee.email = input("Ange ny mail: ")
            ec.save_changes(chosen_employee)
            changed_string = ec.save_changes(chosen_employee)
            print(changed_string)

        elif selected == 5:
            chosen_employee.job_title = input("Ange ny jobtitel: ")
            ec.save_changes(chosen_employee)
            changed_string = ec.save_changes(chosen_employee)
            print(changed_string)

        elif selected == 6:
            break
        else:
            print("Felaktig inmatning")


def remove_employee(chosen_employee):
    while True:
        print("----------------")
        print("TA BORT ANSTÄLLD")
        print(f"Är du säker på att du vill ta bort {chosen_employee}")
        print("1. Ja")
        print("2. Nej")
        confirm = int_input("> ")
        if confirm == 1:
            removed_string = ec.remove_employee(chosen_employee)
            print(removed_string)
            break
        elif confirm == 2:
            print("Anställd har inte tagits bort")
            break
        else:
            print("Felaktig inmatning")


def add_employee():
    print("-------------------")
    print("LÄGGA TILL ANSTÄLLD")
    print("Ange uppgifter på den anställda du vill lägga till")
    while True:
        e_store = input("Butiks id: ")
        if len(sc.find_store_by_id(e_store)) == 0:
            print(f"Hittade ingen butik med id {e_store}")
        else:
            break
    e_name = input("Namn: ")
    e_phone = input("Telefon: ")
    e_email = input("Email: ")
    e_job_title = input("Job title: ")
    e = (e_store, e_name, e_phone, e_email, e_job_title)
    added_string = ec.add_employee(e)
    print(added_string)


def edit_remove_menu(chosen_employee):
    while True:
        print(f"Vad vill du göra med {chosen_employee}")
        print("1. Redigera")
        print("2. Ta bort")
        print("3. Avbryt")
        selected = int_input("> ")
        if selected == 1:
            edit_employee(chosen_employee)
        elif selected == 2:
            remove_employee(chosen_employee)
            break
        elif selected == 3:
            break
        else:
            print("Felaktig inmatning")


def find_employee():
    while True:
        search = input("Sök: ")
        matching_employees = ec.find_employees(search)
        if len(matching_employees) == 0:
            print("Hittade inga anställda som uppfyller sökkraven")
        else:
            print("Matchande sökningar: ")
            for i, employee in enumerate(matching_employees):
                print(f"{i + 1}: {employee}")
            while True:
                selected = int_input("> ")
                if 1 <= selected <= len(matching_employees):
                    chosen_employee = matching_employees[selected - 1]
                    break

                else:
                    print("Felaktig inmatning")
            edit_remove_menu(chosen_employee)
            break


def employees_menu():
    while True:
        print("    ANSTÄLLDA    ")
        print("-----------------")
        print("1. Redigera/ta bort")
        print("2. Lägg till")
        print("3. Gå tillbaka till adminmeny")

        selected = int_input("> ")
        if selected == 1:
            find_employee()

        elif selected == 2:
            add_employee()

        elif selected == 3:
            break
        else:
            print("Felaktig inmatning")


