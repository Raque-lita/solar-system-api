from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.Column(db.Integer)
    #rings = db.Column(db.Boolean)

    def planet_string(self):
        return f"{self.id} : {self.planet} Descriptions: {self.description}"

    
