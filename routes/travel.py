from flask import Blueprint, jsonify
from models import TravelPackage

travel_bp = Blueprint("travel", __name__)

@travel_bp.route("/packages", methods=["GET"])
def get_packages():
    packages = TravelPackage.query.all()
    return jsonify([
        {
            "id": p.id,
            "destination": p.destination,
            "price": p.price,
            "seats": p.available_seats
        } for p in packages
    ])
