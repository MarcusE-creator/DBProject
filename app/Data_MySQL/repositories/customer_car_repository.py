from Data.db import session
from Data.models.customer_car import CustomerCar


def add_customer_car(customer, c):
    regnr, car_model_id, color = c
    customer_id = customer.id
    new_car = CustomerCar(customer_id=customer_id, regnr=regnr, car_model_id=car_model_id, color=color)
    session.add(new_car)
    session.commit()
    return new_car


def find_customer_car(_, regnr):
    return session.query(CustomerCar).filter(CustomerCar.regnr.like(f'%{regnr}%')).first()


def remove_customer_car(_, car):
    session.delete(car)
    session.commit()
