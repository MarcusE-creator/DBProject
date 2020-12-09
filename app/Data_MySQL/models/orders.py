from sqlalchemy.sql import functions
from sqlalchemy.orm import relationship

from ..db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)  # PRIMARY KEY
    customer_id = Column(Integer, ForeignKey('customers.id', ondelete='Set Null', onupdate='Cascade'))  # FOREIGN KEY --> Customers
    employee_id = Column(Integer, ForeignKey('employees.id', ondelete='Set Null', onupdate='Cascade'))  # FOREIGN KEY --> Employees
    store_id = Column(Integer, ForeignKey('stores.id', ondelete='Set Null', onupdate='Cascade'))  # FOREIGN KEY --> Stores

    date_created = Column(DateTime(timezone=True), nullable=False, default=functions.now)
    status = Column(String(45), nullable=False)  # TODO: Use enum and default?
    comment = Column(String(150), default='')  # TODO: Use text?

    store = relationship('Store', back_populates='orders')
    employee = relationship('Employee')
    customer = relationship('Customer', back_populates='orders')
    products = relationship('Product', secondary='ordered_products')

    def __str__(self):
        return f'Ordernummer: {self.id} |' \
               f' Kund: {self.customer.name} |' \
               f' Anställd: {self.employee.name} |' \
               f' Butik: {self.store.name} |' \
               f' Skapad: {self.date_created} |' \
               f' Status: {self.status} |' \
               f'\nProdukter:\n\t{self.products_string}'

    @property
    def products_string(self) -> str:
        return '\n\t' + '\n\t'.join(
            str(product) for product in self.products)
