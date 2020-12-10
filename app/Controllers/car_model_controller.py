import Data.repositories.car_model_repository as cmr


def find_car_model(search):
    cmr.find_car_model(search)


def add_car_model(c):
    cmr.add_car_model(c)


def find_car_model_by_id(id):
    return cmr.find_car_model_by_id(id)