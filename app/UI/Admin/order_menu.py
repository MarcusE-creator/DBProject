from Controllers import order_controller


def order_menu():
    while True:
        print("Ordrar")
        print("-" * 12)
        print("1. Lägg till")
        print("2. Redigera/ta bort")
        print("3. Adminmeny")

        selected = input("> ")
        if selected == "1":
            create_order()
        elif selected == "2":
            edit_remove_order()
        elif selected == "3":
            break
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")


def create_order():
    print_title('Lägg till order')
    order_data = {}
    while True:
        order_data['customer_id'] = int(input('Kund-id: '))
        order_data['employee_id'] = int(input('Medarbetar-id: '))
        order_data['store_id'] = int(input('Butiks-id: '))
        order_data['status'] = 'active'  # TODO: Use enum and default?
        order_data['comment'] = input('Kommentar: ')
        order = order_controller.create(**order_data)
        if order:
            print_title('Lägg till produkter')
            while True:
                product_id = int(input('Produkt-id: '))
                product_amount_str = input('Antal (1 är förvalt): ').strip()
                product_amount = (1 if not product_amount_str.isdigit()
                                  else int(product_amount_str))
                try:
                    # Try to add product to order.
                    order_controller.add_product(order, (product_id, product_amount))
                except Exception as e:
                    print(e)
                # products.append((product_id, product_amount))  # TODO: Enable user to search products
                if input('Lägg till fler produkter? j/n ').lower() == 'j':
                    continue
                break
            break
        print('Kunde inte skapa order. Försök igen.')
    print('Ny order skapad: ')


def edit_remove_order():
    while True:
        print()
        print('Redigera/Ta bort')
        print("-" * 16)
        print("1. Redigera")
        print("2. Ta bort")
        print("3. Ordermeny")
        selected = input("> ")
        if selected == "1":
            edit_order()
        elif selected == "2":
            remove_order()
        elif selected == "3":
            break
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")


def find_order():
    order_id = int(input('\nAnge ordernummer: '))
    order = order_controller.find(order_id)
    if order:
        return order
    print(f'Kunde inte hitta order med ordernummer {order_id}')
    return None


def edit_order():
    while True:
        order = find_order()
        if order:
            # print(f'\n{order}\n')
            print(f'Redigera order #{order.id}')
            print(f'1. Kundnamn: {order.customer.name}')
            print(f'2. Namn på anställd: {order.employee.name}')
            print(f'3. Butik: {order.store.name}')
            print(f'4. Lagd: {order.date_created}')
            print(f'5. Status: {order.status}')
            print(f'6. Produkter: {order.products_string}')
            print('7. Avbryt')
            print('Vilken rad vill du redigera?')

            edit_line = input('> ')

            if edit_line == '1':
                order.customer.name = input("Ange nytt kundnamn: ")
                print(order_controller.edit(order))

            elif edit_line == '2':
                order.employee.name = input('Ange annan anställd: ')
                print(order_controller.edit(order))

            elif edit_line == '3':
                order.store.name = input('Ange ny butik: ')
                print(order_controller.edit(order))

            elif edit_line == '4':
                order.date_created = input('Ange nytt datum: ')
                print(order_controller.edit(order))

            elif edit_line == '5':
                order.status = input('Ange ny status: ')
                print(order_controller.edit(order))

            elif edit_line == '6':
                order.products = input('Ange ny produkt:')
                print(order_controller.edit(order))

            elif edit_line == '7':
                break

            else:
                print('Du har gjort ett ogiltigt val. Försök igen.')
        if input('Redigera annan order? j/n ').lower() != 'j':
            break


def remove_order():
    while True:
        order = find_order()
        if order:
            print(f'\n{order}\n')
            if input(f'Bekräfta borttagning av order? j/n ').lower() == 'j':
                order_id = order.id
                is_removed = order_controller.remove(order)
                if is_removed:
                    del order  # Should delete order object?
                    print(f'Order med ordernummer {order_id} har tagits bort.')
                else:
                    print(f'Kunde inte ta bort order med ordernummer {order_id}'
                          ', var god försök igen.')
            else:
                print('Åtgärden avbruten.')
        if input('\nTa bort annan order? j/n ').lower() != 'j':
            break


def print_order(order) -> None:

    order_data = '| ' + ' | '.join(
        str(value)
        for value in (order.id, order.customer.id, order.date_created)
    ) + ' |'
    border_width = len(order_data)
    border = '-' * border_width
    print(order.customer.name.center(border_width))
    print(border)
    print(order_data, end='\n\n')


def print_title(title: str) -> None:
    padded_title = title.center(len(title) + 4)
    border = '-' * len(padded_title)
    print(padded_title)
    print(border)
