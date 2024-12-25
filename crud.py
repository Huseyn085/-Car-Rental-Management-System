from sqlalchemy.orm import Session
from car_rental import models, schemas

def get_cars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Car).offset(skip).limit(limit).all()

def get_car(db: Session, car_id: int):
    return db.query(models.Car).filter(models.Car.id == car_id).first()

def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(make=car.make, model=car.model, year=car.year, available=car.available)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def get_customers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(name=customer.name, email=customer.email)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_rentals(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Rental).offset(skip).limit(limit).all()

def get_rental(db: Session, rental_id: int):
    return db.query(models.Rental).filter(models.Rental.id == rental_id).first()

def create_rental(db: Session, rental: schemas.RentalCreate):
    db_rental = models.Rental(start_date=rental.start_date, end_date=rental.end_date, car_id=rental.car_id, customer_id=rental.customer_id)
    db.add(db_rental)
    db.commit()
    db.refresh(db_rental)
    return db_rental

def delete_rental(db: Session, rental_id: int):
    db.query(models.Rental).filter(models.Rental.id == rental_id).delete()
    db.commit()
