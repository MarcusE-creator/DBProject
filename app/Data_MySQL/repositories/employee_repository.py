from Data.models.employees import Employee
from Data.db import session


def find_employees(search):
    return session.query(Employee).filter(Employee.name.like(f'%{search}%')).all()


def add_employee(e):
    store_id, name, phone, email, job_title = e
    new_employee = Employee(store_id=store_id, name=name, phone=phone, email=email, job_title=job_title)
    session.add(new_employee)
    session.commit()


def remove_employee(chosen_employee):
    session.delete(chosen_employee)
    session.commit()


def save_changes(_):
    session.commit()