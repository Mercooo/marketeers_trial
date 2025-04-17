from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'your-super-secret-key'  # Change this in production
db = SQLAlchemy(app)
jwt = JWTManager(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    value = db.Column(db.Float)

@app.before_request
def create_tables():
    db.create_all()
    if Item.query.count() == 0:
        db.session.add(Item(name="Sample A", value=100))
        db.session.add(Item(name="Sample B", value=200))
        db.session.commit()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == 'admin' and data['password'] == 'admin':
        token = create_access_token(identity=data['username'])
        return jsonify({'token': token})
    return jsonify({'msg': 'Invalid credentials'}), 401

@app.route('/items', methods=['GET'])
@jwt_required()
def get_items():
    current_user = get_jwt_identity()
    print(f"Authenticated user: {current_user}")
    items = Item.query.all()
    return jsonify([{'id': i.id, 'name': i.name, 'value': i.value} for i in items])

if __name__ == '__main__':
    app.run(debug=True)
