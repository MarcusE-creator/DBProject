from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, Integer, String


class CarModel(Base):
    __tablename__ = "car_models"

    id = Column(Integer, primary_key=True)
    manufacturer = Column(String(45), nullable=False)
    model = Column(String(45), nullable=False)
    year_model = Column(String(4), nullable=False)

    products = relationship("Products", secondary="matching_parts")
    cars = relationship("CustomerCar", back_populates="car_model")

    def __repr__(self):
        return f"{self.manufacturer} {self.model} ({self.year_model})"
