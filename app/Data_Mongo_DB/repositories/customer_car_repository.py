from Data.models.models import CustomerCar


def add_customer_car(customer, car):  #TODO fungerar ej
    regnr, car_model_id, color = car
    new = CustomerCar({'regnr': regnr, 'car_model_id': car_model_id, 'color': color})
    customer.insert_into_array('customer_cars', new)
    return(new)


def find_customer_car(customer, regnr):
    for car in customer.customer_cars:
        car_obj = CustomerCar(car)
        if car_obj.regnr == regnr:
            return True, car_obj
        else:
            continue
    return None


def remove_customer_car(customer, car):
    customer.remove_from_array('customer_cars', car)
