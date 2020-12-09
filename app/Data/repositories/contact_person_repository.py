from Data.db import session
from Data.models.contact_persons import ContactPerson


def add_contact_person_to_new_customer(contact_person, chosen_customer):
    name, phone, email = contact_person
    contact_person = ContactPerson(name=name, phone=phone, email=email)
    session.add(contact_person)
    session.commit()
    return contact_person


def add_contact_person(contact_person, chosen_customer):
    name, phone, email = contact_person
    contact_person = ContactPerson(name=name, phone=phone, email=email)
    session.add(contact_person)
    session.commit()
    chosen_customer.contact_id = contact_person.id
    session.commit()
    return contact_person