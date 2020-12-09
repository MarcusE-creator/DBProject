from bson import ObjectId
from Data.models.models import Store
import re


def store_changes(store):
    store.save()


def find_store(keyword):
    query_str = re.compile(f'.*{keyword}.*', re.IGNORECASE)
    return Store.find(**{'name': query_str})


def find_store_by_id(id):
    return Store.find(**{'_id': ObjectId(id)})


def find_store_by_id(keyword):
    return Store.find(**{'_id': ObjectId(keyword)})


def remove_store(store):
    Store.remove(_id=store._id)


def add_store(store):
    name, street_address, zip_code, city, phone, email = store
    store = Store({'name': name,
                   'street_address': street_address,
                   'zip_code': zip_code,
                   'city': city,
                   'phone': phone,
                   'email': email})
    store.save()
    return store



