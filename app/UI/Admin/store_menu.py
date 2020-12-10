import Controllers.store_controller as cs
from UI.tools import int_input


def store_menu():
    while True:
        print("        BUTIKER       ")
        print("----------------------")
        print("1. Redigera/ta bort")
        print("2. Lägg till")
        print("3. Gå tillbaka till adminmeny")

        selected = input("> ")
        if selected == "1":
            search_and_choose()

        elif selected == "2":
            add_store()

        elif selected == "3":
            break

        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")


def search_and_choose():
    while True:
        keyword = input("Sök butik efter namn: ")
        stores = cs.find_store(keyword)

        if len(stores) == 0:
            print("Det finns ingen butik som upfyller sökkraven.")
        else:
            print("Matchande sökningar:")
            for i, store in enumerate(stores, start=1):
                print(f"{i}. {store}")

            while True:
                choice = int_input("Vilken butik vill du visa? ")
                if 1 <= choice < len(stores):
                    store = stores[choice]
                    break
                else:
                    print("Du har gjort ett ogiltigt val. Försök igen.")

            edit_remove_menu(store)
            break


def edit_remove_menu(store):
    while True:
        print(f"Vad vill du göra med butiken {store}")
        print("1. Redigera")
        print("2. Ta bort")
        print("3. Avbryt")

        action = input("> ")

        if action == "1":
            edit_store(store)
        elif action == "2":
            remove_store(store)
            break
        elif action == "3":
            break
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")


def edit_store(store):
    while True:
        print("----------------------")
        print("REDIGERA BUTIK")
        print(f"1. Namn: {store.name}")
        print(f"2. Gatuadress: {store.street_address}")
        print(f"3. Postkod: {store.zip_code}")
        print(f"4. Stad: {store.city}")
        print(f"5. Telefonnummer: {store.phone}")
        print(f"6. Email: {store.email}")
        print(f"7. Avbryt")
        print("Vilken rad vill du redigera?")

        edit_line = input("> ")

        if edit_line == "1":
            store.name = input("Ange nytt namn: ")
            print(cs.store_changes(store))

        elif edit_line == "2":
            store.street_address = input("Ange ny gatuadress: ")
            print(cs.store_changes(store))

        elif edit_line == "3":
            store.zip_code = input("Ange ny postkod: ")
            print(cs.store_changes(store))

        elif edit_line == "4":
            store.city = input("Ange ny stad: ")
            print(cs.store_changes(store))

        elif edit_line == "5":
            store.phone = input("Ange nytt telefonnummer: ")
            print(cs.store_changes(store))

        elif edit_line == "6":
            store.email = input("Ange ny email: ")
            print(cs.store_changes(store))

        elif edit_line == "7":
            break

        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")


def remove_store(store):
    while True:
        print("----------------------")
        print("TA BORT BUTIK")
        action = input(f"Är du säker på att du vill ta bort {store}? J/N > ")

        if action.lower() == "j":
            print(cs.remove_store(store))
            break

        elif action.lower() == "n":
            print("Butiken har inte tagits bort.")
            break

        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")


def add_store():
    print("----------------------")
    print("LÄGG TILL BUTIK")
    print("Besvara följande frågor:")
    name = input("Butikens namn: ")
    street_address = input("Gatuadress: ")
    zip_code = input("Postkod: ")
    city = input("Stad: ")
    phone = input("Telefonnummer: ")
    email = input("Emailadress: ")

    store = (name, street_address, zip_code, city, phone, email)
    print(cs.add_store(store))


def main():
    pass


if __name__ == "__main__":
    main()
