from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# DB model
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

# Login API (simple)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == 'admin' and data['password'] == 'admin':
        return jsonify({'success': True})
    return jsonify({'success': False}), 401

# Fetch items
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': i.id, 'name': i.name, 'value': i.value} for i in items])

if __name__ == '__main__':
    app.run(debug=True)
