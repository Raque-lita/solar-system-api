from app import db
from flask import Blueprint
from flask import request
from flask import jsonify
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

@solar_system_bp.route("/<planet_id>", methods=["GET"], strict_slashes=False)
def get_single_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons 
        }, 200

@solar_system_bp.route("", methods=["GET"], strict_slashes=False)
def get_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons
        })
    return jsonify(planets_response, 200)





