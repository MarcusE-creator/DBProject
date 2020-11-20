from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, Integer, String


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)  #PRIMARY KEY

    name = Column(String(45), nullable=False)
    street_address = Column(String(100))
    zip_code = Column(String(10))
    city = Column(String(45))
    phone = Column(String(25), nullable=False)
    email = Column(String(100), nullable=False)

    employees = relationship('Employee', back_populates='stores')
    orders = relationship('Order', back_populates='stores')

    def __repr__(self):
        return f"Butik {self.name} ({self.id})"




