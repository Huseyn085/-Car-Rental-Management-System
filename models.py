from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer, index=True)
    available = Column(Integer, default=1)

    rentals = relationship("Rental", back_populates="car")

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)

    rentals = relationship("Rental", back_populates="customer")

class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    start_date = Column(Date)
    end_date = Column(Date)

    car = relationship("Car", back_populates="rentals")
    customer = relationship("Customer", back_populates="rentals")
