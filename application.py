#fix the model
#push it up to github
#json contract
from flask import Flask, request
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy #get the database sqlalchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #to connect the app to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'haewon208@gmail.com'
app.config['MAIL_PASSWORD'] = ''
# app.config['MAIL_DEBUG'] = True  #this and below wasn't there for https://mailtrap.io/blog/flask-email-sending/  if this is true, it will give you some error messages when it doesn't work
# app.config['DEBUG'] = True  #this and below wasn't there for https://mailtrap.io/blog/flask-email-sending/  if this is true, it will give you some error messages when it doesn't work
# app.config['TESTING'] = False #this one and the below together will make sure the emails aren't actually sent for testing
app.config['MAIL_DEFAULT_SENDER'] = 'haewon208@gmail.com'  #if you don't specify the sender, this will be sent
# or you can also add:
# app.config['MAIL_DEFAULT_SENDER'] = ('Haewon from the Solemates', 'anthony@prettyprinted.com')
app.config['MAIL_MAX_EMAILS'] = 10 #just for preventing accidents when you are testing. None by default
# app.config['MAIL_SUPPRESS_SEND'] = False #then if testing is true, the suppress_send is true too.
app.config['MAIL_ASCII_ATTACHMENTS'] = False #convert

mail = Mail(app)

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
        # msg = Message('Hey There', sender='email_address', ...)  Hey there=title, we don't need sender because we configed it, then recipients
    msg = Message('Hey There', recipients=['haewonito@gmail.com'])
    msg.body = 'This is the third test email sent from Haewon\'s app. You don\'t have to reply.'

    mail.send(msg)

    return 'Message has been sent!' # so that we can know and the fucntion has some return value

if __name__ == '__main__':
    app.run()

# do python application.py and the email will be sent
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
