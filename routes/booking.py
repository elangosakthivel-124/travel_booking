from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Booking, TravelPackage

booking_bp = Blueprint("booking", __name__)

@booking_bp.route("/book", methods=["POST"])
@jwt_required()
def book_trip():
    user_id = get_jwt_identity()
    package_id = request.json["package_id"]

    package = TravelPackage.query.get(package_id)
    if package.available_seats <= 0:
        return jsonify(error="No seats available"), 400

    booking = Booking(user_id=user_id, package_id=package_id)
    package.available_seats -= 1

    db.session.add(booking)
    db.session.commit()
    return jsonify(message="Booking confirmed")
