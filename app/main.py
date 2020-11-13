from .db import Base, engine, session
from .models.stores import Stores

def main():

    Base.metadata.create_all(engine)
    store = Stores()
    print(store)

if __name__ == '__main__':
    main()

# testar ny branch
