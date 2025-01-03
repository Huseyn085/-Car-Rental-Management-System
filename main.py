from fastapi import FastAPI
from routers import cars, customers, rentals  # Modulları doğru yoldan import etmək

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Car Rental Management System"}

app.include_router(cars.router, prefix="/cars", tags=["Cars"])
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(rentals.router, prefix="/rentals", tags=["Rentals"])

