from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

tasks_api = Blueprint('tasks_api', __name__)

load_dotenv()
database_url = os.getenv("DATABASE_URL")
client = MongoClient(database_url)
tasks = client.get_database('test').get_collection('tasks')

@tasks_api.route('/tasks')
def documents(): 
   documents = tasks.find({})

   data = []

   for document in documents:
      task = {}
      task["task"] = document["task"]
      data.append(task)

   response = jsonify(data)

   response.status_code = 200

   return response

@tasks_api.route('/tasks/add', methods=['POST'])
def add_task():
   data = request.json

   print(data)

   tasks.insert_one(data)


   message = "Task Successfully Added"
   response = jsonify(message)
   response.status_code = 200
   return response
