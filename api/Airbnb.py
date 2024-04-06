from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import re

airbnb_api = Blueprint('airbnb_api', __name__)

load_dotenv()
database_url = os.getenv("DATABASE_URL")
client = MongoClient(database_url)
airbnbs = client.get_database('sample_airbnb').get_collection('listingsAndReviews')


@airbnb_api.route('/airbnb', methods=['GET'])
def documents():
    documents = airbnbs.find({})

    data = []

    i = 0
    for document in documents:
        if i == 100:
            break
        airbnb = {}
        airbnb["name"] = document["name"]
        airbnb["summary"] = document["summary"]
        airbnb["space"] = document["space"]
        airbnb["description"] = document["description"]
        data.append(airbnb)

        i += 1
        

    response = jsonify(data)

    response.status_code = 200

    return response


@airbnb_api.route('/airbnb/search', methods=['GET'])
def search_by_name_regex():

    pattern = request.args.get('search')

    if pattern == None:
        return jsonify({"error": "Please Enter a Query in the URL!"}), 400
    
    regex = re.compile(pattern)

    documents = airbnbs.find({"name": {"$regex": regex}})

    data = []

    i = 0
    for document in documents:
        if i == 100:
            break
        airbnb = {}
        airbnb["name"] = document["name"]
        airbnb["summary"] = document["summary"]
        airbnb["space"] = document["space"]
        airbnb["description"] = document["description"]
        data.append(airbnb)
        i += 1
        

    response = jsonify(data)

    response.status_code = 200

    return response

@airbnb_api.route('/airbnb/search/propertyType/<property_type>', methods=['GET'])
def search_by_property_type(property_type):
    documents = airbnbs.find({"property_type": property_type})

    data = []

    i = 0
    for document in documents:
        if i == 100:
            break
        airbnb = {}
        airbnb["name"] = document["name"]
        airbnb["summary"] = document["summary"]
        airbnb["space"] = document["space"]
        airbnb["description"] = document["description"]
        data.append(airbnb)
        i += 1

    response = jsonify(data), 200

    return response

@airbnb_api.route('/airbnb/search/all')
def search_by_filters():
    pass
        