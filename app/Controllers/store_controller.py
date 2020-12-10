import Data.repositories.store_repository as sr


def store_changes(store):
    sr.store_changes(store)
    return f"Butiken {store} har uppdaterats."


def find_store(keyword):
    return sr.find_store(keyword)


def find_store_by_id(id):
    return sr.find_store_by_id(id)


def remove_store(store):
    return sr.remove_store(store)


def add_store(store):
    store = sr.add_store(store)
    return f"{store} - Tillagd"


def main():
    pass


if __name__ == "__main__":
    main()
