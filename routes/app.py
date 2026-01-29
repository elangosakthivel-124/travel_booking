from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from routes.auth import auth_bp
from routes.travel import travel_bp
from routes.booking import booking_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(travel_bp, url_prefix="/travel")
app.register_blueprint(booking_bp, url_prefix="/booking")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
