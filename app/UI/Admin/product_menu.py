from Controllers.product_controller import *


def products_menu():
    while True:
        print("PRODUKTER".rjust(13))
        print("-----------------")
        print("1. Redigera/ta bort")
        print("2. Lägg till")
        print("3. Huvudmeny")

        selected = input("> ")
        if selected == "1":
            search = input("Sök: ")
            find_product(search)
        elif selected == "2":
            print("Produkt information: ")

            p_name = input("Namn: ")
            p_description = input("Beskrivning: ")
            p_inventory_id = input("Lagerplats: ")
            p_stock = input("Lagersaldo: ")
            p_price_in = input("Inpris: ")
            p_price_out = input("Utpris: ")
            p_lowest_amount = input("lowest_amount: ")
            p_automatic_order_number = input("automatic_order_number: ")
            p_expected_delivery_date = input("Förväntad leverans: ")
            p = (p_name, p_description, p_inventory_id, p_stock, p_price_in, p_price_out, p_lowest_amount, p_automatic_order_number, p_expected_delivery_date)
            add_product(p)
        elif selected == "3":
            pass
            #main_menu()
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")

