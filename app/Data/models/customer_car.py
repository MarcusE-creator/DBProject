from sqlalchemy.orm import relationship
from ..db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class CustomerCar(Base):
    __tablename__ = "customer_cars"

    regnr = Column(String(10), primary_key=True, autoincrement=False)
    car_model_id = Column(Integer, ForeignKey("car_models.id", ondelete="Restrict", onupdate="Restrict"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id", ondelete="Cascade", onupdate="Cascade"), nullable=False)
    color = Column(String(15), nullable=False)

    customer = relationship("Customer", back_populates="customer_cars")
    car_model = relationship("CarModel", back_populates="cars")

    def __repr__(self):
        return f"Bilen med registreringsnummer {self.regnr} ägs av kund {self.customer}."
