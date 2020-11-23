from UI.car_model_menu import car_model_menu
from UI.employee_menu import employees_menu
from UI.product_menu import products_menu


def admin_menu():
    while True:
        print("Admin")
        print("----------------------")
        print("1. Butiker")
        print("2. Anställda")
        print("3. Ordrar")
        print("4. Produkter")
        print("5. Bilmodeller")
        print("10. Huvudmeny")

        selected = input("> ")
        if selected == "1":
            pass
            #store_menu()
        elif selected == "2":
            employees_menu()
        elif selected == "3":
            pass
            #order_menu()
        elif selected == "4":
            products_menu()
        elif selected == "5":
            car_model_menu()
        elif selected == "10":
            pass
            #main_menu()
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")
