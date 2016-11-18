from flask import Flask, json, jsonify, render_template
from flask_socketio import SocketIO


import getFeedsTEMP


app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    entities = []
    feed = getFeedsTEMP.get_feed()
    for entity in feed.entity:
        route_id = entity.trip_update.trip.route_id
        vehicle_id = entity.vehicle.trip.route_id
        if ((route_id != "" and route_id == "5") or
           (vehicle_id != "" and vehicle_id == "5")):
            entities.append(entity)

    return render_template("index.html", entities=entities)


@app.route('/map_json')
def map_json():
    # Documentation for shapes.json:
    #   route_id : {
    #       
    #       sequence: number of points,
    #       color: route color
    #       points: [[lon, lat],...,]}

    json_input = json.load(open("shapes.json", "r"))

    return jsonify(json_input)


@app.route('/stops_json')
def stops_json():
    # Documentation for stops.json:
    #   stopid : {
    #       lat : num,
    #       lon : num,
    #       name : string
    #   }
    json_input = json.load(open("stops.json", "r"))
    return jsonify(json_input)

if __name__ == "__main__":
    socketio.run(app, debug=True)
