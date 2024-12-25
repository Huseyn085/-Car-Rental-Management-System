from pydantic import BaseModel
from typing import Optional

class Car(BaseModel):
    car_id: int
    make: str
    model: str
    year: int
    is_available: bool = True

class Customer(BaseModel):
    customer_id: int
    name: str
    contact: str

class Rental(BaseModel):
    rental_id: int
    car_id: int
    customer_id: int
    rental_date: str
    return_date: Optional[str] = None
