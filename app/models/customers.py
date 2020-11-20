from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db import Base


class Customer(Base):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    customer_type_id = Column(
        Integer,
        ForeignKey('customer_types.id', ondelete="Cascade", onupdate="Restrict"),
        nullable=False)
    contact_id = Column(
        Integer,
        ForeignKey('contact_persons.id', ondelete="Set Null", onupdate="Cascade")
        )
    name = Column(String(100), nullable=False)
    street_address = Column(String(45), nullable=False)
    zip_code = Column(String(10), nullable=False)
    city = Column(String(45), nullable=False)
    phone = Column(String(25), nullable=False)
    email = Column(String(100), nullable=False)

    orders = relationship('Order', back_populates='customers')
    customer_cars = relationship('CustomerCar', back_populates='customers')
    contact_person = relationship('ContactPerson', back_populates='customers')
    customer_type = relationship('CustomerType', back_populates='customers')

    def __repr__(self):
        pass
