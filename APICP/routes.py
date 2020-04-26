from flask import jsonify, request
from flask import current_app as app
from .models import db, Users, Trips, Vehicles
import requests


@app.route('/')
def hello_world():

    return 'Hello World!'


@app.route('/user', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        username = request.form['username']
        existing_user = Users.query.filter_by(username=username).first()
        if existing_user:
            return jsonify(message='A user with this username already exists'), 409

        else:
            pwd = request.form['password']
            email = request.form['emailid']
            new_user = Users(username=username, pwd=pwd, email=email)
            db.session.add(new_user)  # Add new User record to database
            db.session.commit()
            return jsonify(message='A user has been created'), 201

    if request.method == 'GET':
        user_id = request.args.get('user_id')
        result = Trips.query.filter_by(user_id=user_id)


@app.route('/login', methods=['POST'])
def login():
    username = request.args.get('username')
    pwd = request.args.get('pwd')
    if username and pwd:
        result = Users.query.filter_by(username=username, pwd=pwd).first()
        if result:
            return jsonify(message='The user is successfully logged in'), 200
        else:
            return jsonify(message='wrong username or password entered'), 404
    else:
        return jsonify(message='Please enter the required parameters'), 404


@app.route('/trip', methods=['POST', 'GET'])
def trips():
    if request.method == 'POST':
        user_id = request.args.get('user_id')
        startloc = request.args.get('startloc')
        endloc = request.args.get('endloc')
        vehicle_id = request.args.get('vehicle_id')

        if user_id and startloc and endloc and vehicle_id:
            user = Users.query.filter_by(user_id=user_id).first()
            if user:
                output = requests.get('https://www.distance24.org/route.json?stops={}|{}'.format(startloc, endloc))
                dist = output.json()
                distance = dist['distance']
                entry = Vehicles.query.filter_by(vehicle_id=vehicle_id)
                mileage = entry.mileage
                cb = distance/mileage
                trip = Trips(user_id=user_id, startloc=startloc, endloc=endloc, vehicle_id=vehicle_id, cbfootprint=cb)
                db.session.add(trip)
                db.session.commit()
                return jsonify(message='A trip has been added'), 201

            else:
                return jsonify(message='The user does not exist'), 404
        else:
            return jsonify(message='Please pass all the required parameters')


@app.route('/vehicle', methods=['POST', 'GET'])
def vehicles():
    if request.method == 'POST':
        user_id = request.args.get('user_id')
        vehicle_type = request.args.get('vehicle_type')
        mileage = request.args.get('mileage')

        if user_id and mileage and vehicle_type:
            user = Users.query.filter_by(user_id=user_id).first()
            if user:
                vehicle = Vehicles(user_id=user_id, vehicle_type=vehicle_type, mileage=mileage)
                db.session.add(vehicle)
                db.session.commit()
                return jsonify(message='The vehicle has been added'), 201
            else:
                return jsonify(message='The user does not exist'), 404
        else:
            return jsonify(message='Please pass all the required parameters')