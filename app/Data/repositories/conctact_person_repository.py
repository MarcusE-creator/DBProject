from Data.models.models import ContactPerson


def add_contact_person(contact_person, chosen_customer):
    name, phone, email = contact_person
    contact_person = ContactPerson({"name": name, "phone": phone, "email": email})
    chosen_customer.update_field2("contact_person", contact_person)
    return contact_person