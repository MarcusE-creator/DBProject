from db import Base, engine, session
from models.products import Product
from models.carmodels import CarModel
# from models.contactpersons import ContactPerson
# from models.customercar import CustomerCar
# from models.customers import Customer
# from models.customertypes import CustomerType
# from models.employees import Employee
# from models.orders import Order
# from models.partnertypes import PartnerType
# from models.partners import Partner
# from models.stores import Store
# from models.orderedproducts import OrderedProduct
from models.matchingparts import matching_products


def main():
    Base.metadata.create_all(engine)
    # contactperson = ContactPerson()
    # customercar = CustomerCar()
    # customers = Customer()
    # customertype = CustomerType()
    # employee = Employee()
    # order = Order()
    # orderedproduct = OrderedProduct()
    # store = Store()

if __name__ == '__main__':
    main()
