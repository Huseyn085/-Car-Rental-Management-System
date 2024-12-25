from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from car_rental import crud, models, schemas
from car_rental.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Rental])
def read_rentals(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    rentals = crud.get_rentals(db, skip=skip, limit=limit)
    return rentals[_{{{CITATION{{{_1{](https://github.com/sschuhmann/cr/tree/54cad53d5fccdffeb63e08bf2b5f71f856c075a2/mobility%2Fcrud.py)[_{{{CITATION{{{_2{](https://github.com/boA01/boA01.github.windows/tree/e8bcb761e3f3c23608b56207d39a2f059c7c0f52/pythonApp%2FfastapiApp%2Fapp%2Fmodels%2Fdatabase.py)[_{{{CITATION{{{_3{](https://github.com/shippokun/fastapi/tree/a2d69fd3b70e720dbe9839736b029c4d0bd7e450/sql%2Fdatabase.py)
