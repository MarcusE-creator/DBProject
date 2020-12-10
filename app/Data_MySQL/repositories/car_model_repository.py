from Data.db import session
from Data.models.car_models import CarModel


def find_car_model(search):
    print(search)

def add_car_model(c):
    print(c)

def find_car_model_by_id(id):
    return session.query(CarModel).filter(CarModel.id.like(f'%{id}%')).first()