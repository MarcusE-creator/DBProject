from bson import ObjectId
import re
from Data.models.models import Customer


def save_changes(customer):
    customer.save()
    
    
def find_customer_by_name(keyword):
    query_str = re.compile(f'.*{keyword}.*', re.IGNORECASE)
    return Customer.find(**{'name': query_str})


def find_customer_by_id(keyword):
    return Customer.find(**{'_id': ObjectId(keyword)})


def find_customer_by_phone(keyword):
    query_str = re.compile(f'.*{keyword}.*', re.IGNORECASE)
    return Customer.find(**{'phone': query_str})


def add_business(customer, contact_person):
    name, street_address, zip_code, city, phone, email, customer_type_id = customer
    customer_type = 'Företag'
    cp_name, cp_phone, cp_email = contact_person
    customer = Customer({'name': name,
                         'street_address': street_address,
                         'zip_code': zip_code,
                         'city': city,
                         'phone': phone,
                         'email': email,
                         'customer_type': customer_type,
                         'contact_person': {'name': cp_name,
                                            'phone': cp_phone,
                                            'mail': cp_email},
                        'cars': []})
    customer.save()
    return customer


def add_private(customer):
    name, street_address, zip_code, city, phone, email, customer_type_id = customer
    customer_type = 'Privat'
    customer = Customer({'name': name,
                         'street_address': street_address,
                         'zip_code': zip_code,
                         'city': city,
                         'phone': phone,
                         'email': email,
                         'customer_type': customer_type,
                        'cars': []})
    customer.save()
    return customer


def remove_customer(customer):
    Customer.remove(_id=customer._id)


