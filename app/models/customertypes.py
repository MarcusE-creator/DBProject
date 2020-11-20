from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base


class CustomerType(Base):

    __tablename__ = 'customer_types'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)

    customers = relationship('Customer', back_populates='customer_type')

    def __repr__(self):
        pass
