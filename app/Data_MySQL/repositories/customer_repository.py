from Data.db import session
from Data.models.customers import Customer
import Data.repositories.contact_person_repository as cpr


def save_changes(_):
    session.commit()
    
    
def find_customer_by_name(keyword):
    return session.query(Customer).filter(Customer.name.like(f'%{keyword}%')).all()


def find_customer_by_id(keyword):
    return session.query(Customer).filter(Customer.id == keyword).all()


def find_customer_by_phone(keyword):
    return session.query(Customer).filter(Customer.phone.like(f'%{keyword}%')).all()


def add_business(customer, contact_person):
    name, street_address, zip_code, city, phone, email, customer_type = customer
    contact_person = cpr.add_contact_person_to_new_customer(contact_person)
    contact_id = contact_person.id
    customer = Customer(name=name, street_address=street_address, zip_code=zip_code, city=city, phone=phone,
                        email=email, customer_type_id=customer_type, contact_id=contact_id)
    session.add(customer)
    session.commit()
    return customer


def add_private(customer):
    name, street_address, zip_code, city, phone, email, customer_type = customer
    customer = Customer(name=name, street_address=street_address, zip_code=zip_code, city=city, phone=phone,
                        email=email, customer_type_id=customer_type)
    session.add(customer)
    session.commit()
    return customer


def remove_customer(chosen_customer):
    session.delete(chosen_customer)
    session.commit()

