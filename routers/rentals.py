from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

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
    return rentals

@router.get("/{rental_id}", response_model=schemas.Rental)
def read_rental(rental_id: int, db: Session = Depends(get_db)):
    db_rental = crud.get_rental(db, rental_id=rental_id)
    if db_rental is None:
        raise HTTPException(status_code=404, detail="Rental not found")
    return db_rental

@router.post("/", response_model=schemas.Rental)
def create_rental(rental: schemas.RentalCreate, db: Session = Depends(get_db)):
    return crud.create_rental(db=db, rental=rental)

@router.delete("/{rental_id}")
def delete_rental(rental_id: int, db: Session = Depends(get_db)):
    crud.delete_rental(db, rental_id=rental_id)
    return {"message": "Rental deleted successfully"}
