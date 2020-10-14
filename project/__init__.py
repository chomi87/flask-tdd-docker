from flask import Flask, jsonify
from flask_restx import Resource, Api
import os

#instantiate the app
app = Flask(__name__)
api = Api(app)

#set configuration
app_settings = os.getenv('APP_SETTINGS')  # new
app.config.from_object(app_settings)      # new

class Ping(Resource):
    def get(self):
        return {"status" :  "success",
                "message" : "pong!"}

api.add_resource(Ping, "/ping")