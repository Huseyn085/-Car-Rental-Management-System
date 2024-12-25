from flask import Blueprint, request, jsonify
from models import db, Booking, Car

booking_routes = Blueprint('bookings', __name__)

@booking_routes.route('/', methods=['POST'])
def create_booking():
    data = request.json
    car = Car.query.get(data['car_id'])
    if not car or not car.availability:
        return jsonify({"message": "Car not available"}), 400

    booking = Booking(user_id=data['user_id'], car_id=data['car_id'], start_date=data['start_date'], end_date=data['end_date'])
    car.availability = False
    db.session.add(booking)
    db.session.commit()
    return jsonify({"message": "Booking created successfully"}), 201

@booking_routes.route('/', methods=['GET'])
def list_bookings():
    bookings = Booking.query.all()
    booking_list = [{"id": booking.id, "user_id": booking.user_id, "car_id": booking.car_id, "start_date": booking.start_date, "end_date": booking.end_date} for booking in bookings]
    return jsonify(booking_list), 200
