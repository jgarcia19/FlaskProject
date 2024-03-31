from flask import Flask, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import api.Tasks
import os

app = Flask(__name__)

app.register_blueprint(api.Tasks.tasks_api)

@app.route('/')
def hello_world():

   hw = "Hello World"

   response = jsonify(hw)
   response.status_code = 200

   return response


if __name__ == '__main__':
   app.run()