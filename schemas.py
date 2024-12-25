from pydantic import BaseModel
from datetime import date

class CarBase(BaseModel):
    make: str
    model: str
    year: int
    available: int

class CarCreate(CarBase):
    pass

class Car(CarBase):
    id: int
    rentals: list

    class Config:
        from_attributes = True

class CustomerBase(BaseModel):
    name: str
    email: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    rentals: list

    class Config:
        from_attributes = True

class RentalBase(BaseModel):
    start_date: date
    end_date: date

class RentalCreate(RentalBase):
    car_id: int
    customer_id: int

class Rental(RentalBase):
    id: int
    car: Car
    customer: Customer

    class Config:
        from_attributes = True

