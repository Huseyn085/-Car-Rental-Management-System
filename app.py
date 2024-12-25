from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import routes
from routes.users import user_routes
from routes.cars import car_routes
from routes.bookings import booking_routes

# Register routes
app.register_blueprint(user_routes, url_prefix='/users')
app.register_blueprint(car_routes, url_prefix='/cars')
app.register_blueprint(booking_routes, url_prefix='/bookings')

if __name__ == "__main__":
    db.create_all()  # Create database tables
    app.run(debug=True)
