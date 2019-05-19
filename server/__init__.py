from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from server.Adafruit_Thermal import *

app = Flask(__name__)
CORS(app)
api = Api(app)

printer = Adafruit_Thermal("/dev/ttyACM0", 19200, timeout=5)

from server import routes

