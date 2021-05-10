import pytest
from app import create_app
from app import db
from app.models.planet import Planet


@pytest.fixture
def saved_planet(app):
    #Arrange
    saturn_planet = Planet(name="Saturn",
                            description="gas giant",
                            moons= 82 )
    db.session.add_all([saturn_planet])

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()