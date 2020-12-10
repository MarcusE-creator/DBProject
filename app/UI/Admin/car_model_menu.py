from Controllers.car_model_controller import *
from UI.tools import int_input


def car_model_menu():
    while True:
        print("BILMODELLER".rjust(13))
        print("-----------------")
        print("1. Redigera/ta bort")
        print("2. Lägg till")
        print("3. Huvudmeny")

        selected = int_input("> ")
        if selected == 1:
            search = input("Sök: ")
            find_car_model(search)
        elif selected == 2:
            print("Ange information om den bilmodell du vill lägga till")
            c_manufacturer = input("Tillverkare: ")
            c_model = input("Modell: ")
            c_year_model = input("Årsmodell: ")
            c = (c_manufacturer, c_model, c_year_model)
            add_car_model(c)
        elif selected == 3:
            pass
            #main_menu()
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")

car_model_menu()