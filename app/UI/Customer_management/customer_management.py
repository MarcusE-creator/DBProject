import Controllers.car_model_controller as cmc
import Controllers.contact_person_controller as cpc
import Controllers.customer_car_controller as ccc
import Controllers.customer_controller as cc
from UI.tools import int_input


def add_new_customer():
    print("----------------------")
    print("LÄGG TILL KUND")
    print("Besvara följande frågor:")

    name = input("Kundens namn: ")
    street_address = input("Gatuadress: ")
    zip_code = input("Postkod: ")
    city = input("Stad: ")
    phone = input("Telefonnummer: ")
    email = input("Email: ")

    customer_type_id = int_input("Kundtyp: ange 1 för privatkund och 2 för företagskund: ")
    if customer_type_id == 2:
        print("Fyll i följande uppgifter om kontaktpersonen:")
        cp_name = input("Kontaktpersonens namn: ")
        cp_phone = input("Kontaktpersonens telefonnummer: ")
        cp_email = input("Kontaktpersonens email:")
        contact_person = cp_name, cp_phone, cp_email

        customer = (name, street_address, zip_code, city, phone, email, customer_type_id)
        customer, info_string = cc.add_business(customer, contact_person)

    else:
        customer = (name, street_address, zip_code, city, phone, email, customer_type_id)
        customer, info_string = cc.add_private(customer)

    print(info_string)
    show_customer(customer)


def show_customer(chosen_customer):

    print("     KUNDBILD     ")
    print("------------------")
    print(f"Namn: {chosen_customer.name} ({str(chosen_customer.customer_type)})")

    if hasattr(chosen_customer, 'contact_person'):
        print(f"Kontaktperson {chosen_customer.contact_person}")

    print(f"Address: {chosen_customer.street_address}")
    print(f"Postkod: {chosen_customer.zip_code}")
    print(f"Email: {chosen_customer.email}")
    print(f"Telefonnummer: {chosen_customer.phone}")

    if len(chosen_customer.orders) != 0:
        print("------------------")
        print("Ordrar:")
        for order in chosen_customer.orders:
            print(order)

    if len(chosen_customer.customer_cars) != 0:
        print("------------------")
        print("Bilar:")
        for car in chosen_customer.customer_cars:
            print(car)

    show_customer_menu(chosen_customer)


def find_customer_menu():
    while True:
        print("----------------------")
        print("SÖK UPP BEFINTLIG KUND")
        print("1. Sök efter namn")
        print("2. Sök efter id")
        print("3. Sök efter telefonnummer")
        print("4. Avbryt")

        choice = int_input("> ")

        if choice == 1:
            keyword = input("Ange namn: ")
            customers = cc.find_customer_by_name(keyword)
            if customers:
                choose_customer(customers)
                break
            else:
                print("Det finns ingen kund som uppfyller sökkraven")

        elif choice == 2:
            keyword = input("Ange id: ")
            customers = cc.find_customer_by_id(keyword)
            if customers:
                choose_customer(customers)
                break
            else:
                print("Det finns ingen kund som uppfyller sökkraven.")

        elif choice == 3:
            keyword = input("Ange telefonnumer: ")
            customers = cc.find_customer_by_phone(keyword)
            if customers:
                choose_customer(customers)
                break
            else:
                print("Det finns ingen kund som uppfyller sökkraven.")

        elif choice == 4:
            break

        else:
            print("Felaktig inmatning.")


def choose_customer(customers):
    if customers:
        if len(customers) == 1:
            print(customers[0])
            show_customer(customers[0])

        else:
            print("Matchande sökningar:")
            for i, customer in enumerate(customers):
                print(f"{i + 1}. {customer}")

            while True:
                customer_choice = int_input("Vilken kund vill du visa?")
                if 1 <= customer_choice <= len(customers):
                    chosen_customer = customers[customer_choice - 1]
                    show_customer(chosen_customer)
                    break
                else:
                    print("Felaktig inmatning.")
    else:
        print("Det finns ingen kund som uppfyller sökkraven")


def show_customer_menu(chosen_customer):
    while True:
        print("------------------")
        print(f"Vad vill du göra med {chosen_customer}")
        print("1. Redigera kunden")
        print("2. Lägg till bil")
        print("3. Ta bort bil")
        print("4. Ta bort kunden")
        print("5. Avbryt")

        selected = int_input("> ")

        if selected == 1:
            edit_customer(chosen_customer)

        elif selected == 2:
            add_customer_car(chosen_customer)

        elif selected == 3:
            remove_car_menu(chosen_customer)

        elif selected == 4:
            remove_customer(chosen_customer)
            break

        elif selected == 5:
            break

        else:
            print("Felaktig inmatning")


def add_customer_car(customer):
    print("-------------------")
    print("LÄGGA TILL BIL")
    print("Ange uppgifter på den bil du vill lägga till")

    regnr = input("Regnummer: ")

    while True:
        car_model_id = input("Bilmodel (id): ")
        if not cmc.find_car_model_by_id(car_model_id):
            print(f"Hittade ingen bilmodell med id {car_model_id}")
        else:
            break

    color = input("Bilfärg: ")
    c = (regnr, car_model_id, color)
    added_string, added_car = ccc.add_customer_car(customer, c)
    print(added_string)


def remove_car_menu(customer):

    print("Ange regnummret på den bil du vill ta bort")

    while True:
        regnr = input("> ")
        state, found_car = ccc.find_customer_car(customer, regnr)
        if state:
            print(f"Är du säker på att du vill ta bort denna bil?")
            print(f"Regnummer: {found_car} | Ägare: {customer}")
            print("1. Ja")
            print("2. Nej")
            selected = int_input("> ")

            if selected == 1:
                removed_string = ccc.remove_customer_car(customer, found_car)
                print(removed_string)
                break

            elif selected == 2:
                break

        else:
            print(f"Hittade ingen bil med registreringsnummer {regnr}")


def remove_customer(chosen_customer):
    while True:
        print("----------------")
        print("TA BORT KUND")
        print(f"Är du säker på att du vill ta bort denna kunden?")
        print(f"{chosen_customer}")
        print("1. Ja")
        print("2. Nej")

        selected = int_input("> ")

        if selected == 1:
            if hasattr(chosen_customer, 'customer_cars'):
                ccc.remove_all_customer_cars(chosen_customer)
            removed_string = cc.remove_customer(chosen_customer)
            print(removed_string)
            break

        elif selected == 2:
            break

        else:
            print("Felaktig inmatning")


def edit_contact_person(chosen_customer):
    """
    This function is not used because it requires contact_person to be an object, and in this function it is a
    dictionary. The contact_person object does exist, we did not manage to make it work in this function.
    """
    while True:
        print("-----------------------")
        print(f"REDIGERA KONTAKTPERSON")
        print(f"1. Namn {chosen_customer.contact_person.name}")
        print(f"2. Telefonnummer {chosen_customer.contact_person.phone}")
        print(f"3. Email {chosen_customer.contact_person.email}")
        print("4. Avbryt")
        print("Vilken rad vill du redigera?")
        selected = input("> ")

        if selected == "1":
            chosen_customer.contact_person.name = input("Ange nytt namn: ")
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == "2":
            chosen_customer.contact_person.phone = input("Ange nytt telefonnummer: ")
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == "3":
            chosen_customer.contact_person.email = input("Ange ny email: ")
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == "4":
            break

        else:
            print("Felaktig inmatning")


def add_contact_person(chosen_customer):
    print("LÄGGA TILL NY KONTAKTPERSON")
    print("---------------------------")
    print("Fyll i uppgifter för den nya kontaktpersonen:")
    cp_name = input("Kontaktpersonens namn: ")
    cp_phone = input("Kontaktpersonens telefonnummer: ")
    cp_email = input("Kontaktpersonens email:")
    contact_person = cp_name, cp_phone, cp_email
    added_string = cpc.add_contact_person(contact_person, chosen_customer)
    print(added_string)


def edit_customer(chosen_customer):
    while True:
        print("--------------")
        print(f"REDIGERA KUND")
        print(f"1. Namn: {chosen_customer.name}")
        print(f"2. Address: {chosen_customer.street_address}")
        print(f"3. Postkod: {chosen_customer.zip_code}")
        print(f"4. Email: {chosen_customer.email}")
        print(f"5. Telefonnummer: {chosen_customer.phone}")

        if hasattr(chosen_customer, 'contact_person'):
            print(f"6. Konkaktperson: {chosen_customer.contact_person}")
        print(f"7. Avbryt")
        print(f"Vilken rad vill du redigera?")
        selected = int_input("> ")

        if selected == 1:
            chosen_customer.name = input("Ange nytt namn: ")
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == 2:
            chosen_customer.street_address = input("Ange ny address): ")
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == 3:
            chosen_customer.zip_code = input("Ange ny postkod: ")
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == 4:
            chosen_customer.email = input("Ange ny mail: ")
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == 5:
            chosen_customer.phone = input("Ange nytt telefonnummer: ")
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == 6:
            add_contact_person(chosen_customer)

        elif selected == 7:
            break

        else:
            print("Felaktig inmatning")


def main():
    pass


if __name__ == "__main__":
    main()
