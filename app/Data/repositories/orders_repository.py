def create(**kwargs):
    pass


def edit(order: Order) -> Optional[Order]:
    pass


def find(order_id: int) -> Optional[Order]:
    pass


def add_products(*products, order: Order):
    pass


def add_product(product, order: Order) -> OrderedProduct:
    pass


def remove(order: Order):
    pass
