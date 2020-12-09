from Data.db import session
from Data.models.stores import Store


def store_changes(_):
    session.commit()


def find_store(keyword):
    return session.query(Store).filter(Store.name.like(f'%{keyword}%')).all()


def find_store_by_id(id):
    return session.query(Store).filter(Store.id == id).first()


def remove_store(store):
    if not store.employees:
        session.delete(store)
        session.commit()
        return f"Butiken {store} har tagits bort."
    else:
        return (f"Du får inte ta bort butiken {store} eftersom det finns tillhörande anställda. "
                f"Ta bort eller flytta dessa innan du försöker igen.")


def add_store(store):
    name, street_address, zip_code, city, phone, email = store
    store = Store(name=name, street_address=street_address, zip_code=zip_code, city=city, phone=phone, email=email)
    session.add(store)
    session.commit()
    return store

