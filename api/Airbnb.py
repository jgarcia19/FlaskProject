from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

Airbnb_api = Blueprint('airbnb_api', __name__)

load_dotenv()
database_url = os.getenv("DATABASE_URL")
client = MongoClient(database_url)