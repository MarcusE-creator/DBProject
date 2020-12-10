import Data.repositories.customer_car_repository as ccr


def add_customer_car(customer, c):
    added_car = ccr.add_customer_car(customer, c)
    return f"{added_car} - tillagd", added_car


def find_customer_car(customer, regnr):
    car_obj = ccr.find_customer_car(customer, regnr)
    return car_obj


def remove_customer_car(customer, car):
    ccr.remove_customer_car(customer, car)
    return f"{car} - borttagen"


def remove_all_customer_cars(customer):
    customer_cars = customer.customer_cars
    for car in customer_cars:
        ccr.remove_customer_car(customer, car)
