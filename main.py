from fastapi import FastAPI
from routers import cars, customers, rentals

# Initialize the FastAPI app
app = FastAPI()

# Include Routers
app.include_router(cars.router, prefix="/cars", tags=["Cars"])
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(rentals.router, prefix="/rentals", tags=["Rentals"])

# Run the app
# To run this, save the file and use the command: uvicorn main:app --reload
