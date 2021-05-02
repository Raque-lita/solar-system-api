from app import db
from flask import Blueprint
from flask import request
from .models.planet import Planet

solar_system_bp = Blueprint("planets", __name__, url_prefix="/planets")

@solar_system_bp.route("", methods=["POST"])

def create_planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        moons=request_body["moons"])
    
    db.session.add(new_planet)
    db.session.commit()

    return f"Planet {new_planet.name} successfully created.", 201





