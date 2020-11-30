from sqlalchemy.sql import functions
from sqlalchemy.orm import relationship

from ..db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)  # PRIMARY KEY
    customer_id = Column(Integer, ForeignKey('customers.id', ondelete="Set Null", onupdate="Cascade"))  # FOREIGN KEY --> Customers
    employee_id = Column(Integer, ForeignKey('employees.id', ondelete="Set Null", onupdate="Cascade"))  # FOREIGN KEY --> Employees
    store_id = Column(Integer, ForeignKey('stores.id', ondelete="Set Null", onupdate="Cascade"))  # FOREIGN KEY --> Stores

    date_created = Column(DateTime(timezone=True), nullable=False, default=functions.now)
    status = Column(String(45), nullable=False)  # TODO: Use enum and default?
    comment = Column(String(150), default='')  # TODO: Use text?

    store = relationship('Store', back_populates='orders')
    employee = relationship('Employee')
    customer = relationship('Customer', back_populates='orders')
    products = relationship('Product', secondary='ordered_products')

    def __repr__(self):
        pass
