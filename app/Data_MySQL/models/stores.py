from sqlalchemy.orm import relationship
from ..db import Base
from sqlalchemy import Column, Integer, String
import app.Data.models


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)  # PRIMARY KEY

    name = Column(String(45), nullable=False)
    street_address = Column(String(100))
    zip_code = Column(String(10))
    city = Column(String(45))
    phone = Column(String(25), nullable=False)
    email = Column(String(100), nullable=False)

    employees = relationship('Employee', post_update=True, back_populates='store')
    orders = relationship('Order', back_populates='store')

    def __repr__(self):
        return f"{self.name}"
