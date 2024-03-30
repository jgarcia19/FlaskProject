from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
database_url = os.getenv("DATABASE_URL")

client = MongoClient(database_url)
tasks = client.get_database('test').get_collection('tasks')

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/documents')
def documents(): 
   documents = tasks.find({})

   for document in documents:
      print(document)

   return "done"

if __name__ == '__main__':
   app.run()