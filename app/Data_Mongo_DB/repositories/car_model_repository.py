from bson import ObjectId
from Data.models.models import CarModel


def find_car_model_by_id(id):
    return CarModel.find(**{'_id': ObjectId(id)})
