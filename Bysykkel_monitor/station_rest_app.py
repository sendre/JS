from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)

class Station(Resource):
    def __init__(self):
        self.json_file = 'stations_data.json'
        with open(self.json_file) as f:
            self.data = json.load(f)

    def write_json_to_file(self, data):
        """Opens the json data file and overwrites with new data

        data - json data to write to file"""
        with open(self.json_file, 'w') as outfile:
            json.dump(data, outfile)

    def get(self, station_name):
        """Fetches station data

        station_name - name of station to fetch"""

        for station in self.data:
            if station_name == station["Stasjon"]:
                return station, 200
        return "Station not found", 404

    def post(self, station_name):
        """Creates new station if not existing

        station_name - name of station to create"""

        parser = reqparse.RequestParser()
        parser.add_argument("Ledige sykler")
        parser.add_argument("Ledige låser")
        args = parser.parse_args()

        #check if station already exist
        for station in self.data:
            if station_name == station["Stasjon"]:
                return "Station {} already exists".format(station_name), 400

        new_station = {
            "Stasjon": station_name,
            "Ledige sykler": args["Ledige sykler"],
            "Ledige låser": args["Ledige låser"]
        }
        self.data.append(new_station)
        self.write_json_to_file(self.data)
        return new_station, 201

    def put(self, station_name):
        """Updates existing station. If station does not exist, create new

        station_name - name of station to update"""

        parser = reqparse.RequestParser()
        parser.add_argument("Ledige sykler")
        parser.add_argument("Ledige låser")
        args = parser.parse_args()

        for station in self.data:
            if station_name == station["Stasjon"]:
                station["Ledige sykler"] = args["Ledige sykler"]
                station["Ledige låser"] = args["Ledige låser"]
                self.write_json_to_file(self.data)
                return station, 200

        new_station = {
            "Stasjon": station_name,
            "Ledige sykler": args["Ledige sykler"],
            "Ledige låser": args["Ledige låser"]
        }
        self.data.append(new_station)
        self.write_json_to_file(self.data)
        return new_station, 201

    def delete(self, station_name):
        """Deletes existing station

        station_name - name of station to delete"""
        
        self.data = [station for station in self.data if station["Stasjon"] != station_name]
        self.write_json_to_file(self.data)
        return "{} have been deleted.".format(station_name), 200



if __name__=='__main__':
    api.add_resource(Station, "/station/<string:station_name>")
    app.run(debug=True)
