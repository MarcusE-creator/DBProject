import Data.repositories.conctact_person_repository as cpr


def add_contact_person(contact_person, chosen_customer):
    contact_person = cpr.add_contact_person(contact_person, chosen_customer)
    return f"{contact_person} - Tillagd"
