from app import db
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from .models.planet import Planet
from flask import render_template

solar_system_bp = Blueprint("planets", __name__, url_prefix="/planets")
#templates
@solar_system_bp.route("/html")
def template_example():
    planets = Planet.query.all()
    return render_template('template.html', planets=planets)

@solar_system_bp.route("", methods=["POST"])
def create_planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        moons=request_body["moons"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} successfully created.", 201))

@solar_system_bp.route("/<planet_id>", methods=["GET"], strict_slashes=False)
def get_single_planet(planet_id):
    planet = Planet.query.get(planet_id)
    
    if planet is None:
        return make_response('none', 404)
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

@solar_system_bp.route("/<planet_id>", methods=["DELETE"], strict_slashes= False)
def delete_planet(planet_id):
    planet = Planet.query.get(planet_id) #what is .query.get returning
    db.session.delete(planet)
    db.session.commit()
    return make_response(jsonify(f"Planet {planet.id} successfully deleted.", 201))


@solar_system_bp.route("/<planet_id>", methods=["PUT"], strict_slashes= False)
def update_planet(planet_id):
    planet = Planet.query.get(planet_id)
    form_data = request.get_json()

    planet.name = form_data["name"]
    planet.description = form_data["description"]
    planet.moons = form_data["moons"]

    db.session.commit()
    return make_response(f"Planet #{planet.id} successfully updated")




