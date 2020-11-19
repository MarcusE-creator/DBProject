from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class CustomerCar(Base):
    __tablename__ = "customer_cars"

    regnr = Column(String(10), primary_key=True, autoincrement=False)
    car_model_id = Column(Integer, ForeignKey("car_models.id"), nullable=False, ondelete="Restrict", onupdate="Restrict")
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False, ondelete="Cascade", onupdate="Cascade")
    color = Column(String(15), nullable=False)

    customer = relationship("Customer", back_populate="customer_cars")
    car_model = relationship("CarModel", back_populate="cars")

    def __repr__(self):
        return f"Bilen med registreringsnummer {self.regnr} ägs av kund {self.customer}."
