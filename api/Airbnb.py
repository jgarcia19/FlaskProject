from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

airbnb_api = Blueprint('airbnb_api', __name__)

load_dotenv()
database_url = os.getenv("DATABASE_URL")
client = MongoClient(database_url)
airbnbs = client.get_database('sample_airbnb').get_collection('listingsAndReviews')


@airbnb_api.route('/airbnb')
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