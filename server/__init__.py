from server import routes
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import adafruit_thermal_printer
import serial

app = Flask(__name__)
CORS(app)
api = Api(app)

ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)

uart = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3000)

printer = ThermalPrinter(uart, auto_warm_up=False)
