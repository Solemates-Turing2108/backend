#fix the model
#push it up to github
#json contract
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy #get the database sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #to connect the app to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    shoes = db.relationship('Shoe', backref='user')

    def __repr__(self):
        return f"{self.name} - {self.email}"

class Shoe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    side = db.Column(db.String(80), nullable=False)
    style = db.Column(db.String(80), nullable=False)
    brand = db.Column(db.String(80), nullable=False)
    size = db.Column(db.Integer)
    description = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):  # so we can grab stuff by doing .self  ???? this isn't working for some reason
        return f"{self.id} - {self.description}"

@app.route('/')
def index():
    return "Hello!"


@app.route('/shoes')
def get_shoes():
    shoes = Shoe.query.all()
    output = []
    for shoe in shoes:
        shoe_data = {
                        "id": shoe.id,
                        "side": shoe.side,
                        "style": shoe.style,
                        "size": shoe.size,
                        "description": shoe.description,
                        "brand": shoe.brand,
                        "user_id": shoe.user_id
                    }
        output.append(shoe_data)

    return {"shoes": output}

@app.route('/shoes/<id>')
def get_shoe(id):
    shoe = Shoe.query.get_or_404(id)
    shoe_data = {
                    "id": shoe.id,
                    "side": shoe.side,
                    "style": shoe.style,
                    "size": shoe.size,
                    "description": shoe.description,
                    "brand": shoe.brand,
                    "user_id": shoe.user_id
                }
    return (shoe_data)

@app.route('/shoes', methods=['POST'])
def add_shoe():
    shoe = Shoe(side=request.json["side"], style=request.json["style"], size=request.json["size"], description=request.json["description"], user_id=request.json["user_id"])
    db.session.add(shoe)
    db.session.commit()
    return  {'id': shoe.id}

@app.route('/shoes/<id>', methods=['DELETE'])
def delete_shoe(id):
    shoe = Shoe.query.get(id)
    if shoe is None:
        return {"error": "not found"}

    db.session.delete(shoe)
    db.session.commit()

    return {"message": "the shoe " + f"{shoe.id}" + " has been deleted!"}

# @app.route('/shoes/search')
# def filter_shoe_by_side():
#     query_side = request.json["side"]
#     shoes = Shoe.query.filter_by(side=query_side).all()
#     output = []
#
#     for shoe in shoes:
#         shoe_data = {
#                         "id": shoe.id,
#                         "side": shoe.side,
#                         "style": shoe.style,
#                         "size": shoe.size,
#                         "description": shoe.description,
#                         "brand": shoe.brand,
#                         "user_id": shoe.user_id
#                     }
#         output.append(shoe_data)
#
#     return {"shoes": output}
