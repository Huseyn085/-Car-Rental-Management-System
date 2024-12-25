from fastapi import FastAPI
import cars, customers, rentals  # Modules directly imported if all are in the same directory

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Car Rental Management System"}

app.include_router(cars.router, prefix="/cars", tags=["Cars"])
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(rentals.router, prefix="/rentals", tags=["Rentals"])
