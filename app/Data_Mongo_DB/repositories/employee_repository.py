import re
from Data.models.models import Employee


def find_employees(search):
    query_str = re.compile(f'.{search}.', re.IGNORECASE)
    return Employee.find(**{'name': query_str})


def add_employee(e):
    store, name, phone, email, job_title = e
    new = Employee(
        {
            "name": name,
            "store": store,
            "phone": phone,
            "email": email,
            "job_title": job_title
         })
    new.save()
    return new


def remove_employee(chosen_employee):
    Employee.remove(_id=chosen_employee._id)


def save_changes(chosen_employee):
    chosen_employee.save()