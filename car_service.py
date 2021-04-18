from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os import abort

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://myuser:1111@localhost:3306/mydb'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer) 
    color = db.Column(db.String(10))
    volume = db.Column(db.Integer)
    standard_type = db.Column(db.String(20))
    engine_capacity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    fuel = db.Column(db.String(10))
    number_of_wheels = db.Column(db.Integer)


    def __init__(self, weight, color, volume, standard_type,
                 engine_capacity, price, fuel, number_of_wheels):
        self.weight = weight
        self.color = color
        self.volume = volume
        self.standard_type = standard_type
        self.engine_capacity = engine_capacity
        self.price = price
        self.fuel = fuel
        self.number_of_wheels = number_of_wheels


class CarsSchema(ma.Schema):
    class Meta:
        fields = ('weight', 'color', 'volume', 'standard_type', 'engine_capacity', 'price', 'fuel', 'number_of_wheels')


car_schema = CarsSchema()
cars_schema = CarsSchema(many=True)


@app.route("/cars", methods=["GET"])
def get_cars():
    cars = Car.query.all()
    result = cars_schema.dump(cars)
    return jsonify(result)


@app.route("/cars/<id>", methods=["GET"])
def get_car(id):
    car = Car.query.get(id)
    if car is None:
        abort(404)
    return car_schema.jsonify(car)


@app.route("/cars", methods=["POST"])
def add_car():
    data = CarsSchema().load(request.json)
    new_car = Car(**data)

    db.session.add(new_car)
    db.session.commit()

    return car_schema.jsonify(new_car)


@app.route("/cars/<id>", methods=["PUT"])
def update_car(id):
    car = Car.query.get(id)

    if car is None:
        abort(404)

    data = CarsSchema().load(request.json)

    for i in data:
        setattr(car, i, request.json[i])


    db.session.commit()
    return car_schema.jsonify(car)


@app.route("/cars/<id>", methods=["DELETE"])
def delete_car(id):
    car = Car.query.get(id)
    if car is None:
        abort(404)
    db.session.delete(car)
    db.session.commit()
    return car_schema.jsonify(car)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
