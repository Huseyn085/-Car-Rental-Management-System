from flask import Blueprint, request, jsonify
from models import db, Car

car_routes = Blueprint('cars', __name__)

@car_routes.route('/', methods=['POST'])
def add_car():
    data = request.json
    car = Car(make=data['make'], model=data['model'], year=data['year'])
    db.session.add(car)
    db.session.commit()
    return jsonify({"message": "Car added successfully"}), 201

@car_routes.route('/', methods=['GET'])
def list_cars():
    cars = Car.query.all()
    car_list = [{"id": car.id, "make": car.make, "model": car.model, "year": car.year, "availability": car.availability} for car in cars]
    return jsonify(car_list), 200
