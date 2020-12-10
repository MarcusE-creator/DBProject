from UI.Admin.menu import admin_menu
from UI.Customer_management.menu import customer_management_menu
from UI.tools import int_input


def main_menu():
    while True:
        print("      HUVUDMENY       ")
        print("----------------------")
        print("1. Admin")
        print("2. Kundhantering")
        print("3. Avsluta")

        selected = int_input("> ")
        if selected == 1:
            admin_menu()
        elif selected == 2:
            customer_management_menu()
        elif selected == 3:
            break
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")
