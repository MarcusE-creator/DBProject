from Data.repositories import order_repository


def create(
    *,  # Disallow positional arguments
    customer_id,  # TODO: Search for and pass object?
    employee_id,
    store_id,
    status,  # TODO: Pass as argument or set default?
    comment='',
):
    return order_repository.create(
            customer_id=customer_id,
            employee_id=employee_id,
            store_id=store_id,
            status=status,
            comment=comment,
        )


def edit(order):
    return order_repository.edit(order)


def find(order_id: int):
    return order_repository.find(order_id)


def add_products(order, *products):
    added_products = []
    for product in products:
        try:
            added_product = order_repository.add_product(product, order)
            # TODO: Try add one product at the time, looping over amount
            #  range, rolling back or at least asking the customer to
            #  confirm a differing amount.
        except Exception:
            raise ValueError(
                f'Kunde inte lägga till {product[1]} av produkt {product[0]}')
        added_products.append(added_product)
    return added_products


def add_product(order, product):
    try:
        return order_repository.add_product(product, order)
    except Exception as e:
        raise ValueError(
            f'Kunde inte lägga till {product[1]} av produkt {product[0]}')


def remove(order) -> bool:
    try:
        order_repository.remove(order)
        return True
    except Exception as e:
        print(repr(e), e.__traceback__)
        return False
