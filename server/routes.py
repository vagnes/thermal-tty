from server import app, api, printer
from flask import request
from flask_restful import Resource
import requests

class Test(Resource):

    def get(self):
        return "WIRKLS"

class PrintText(Resource):

    def post(self):
        printer.begin(250)
        args = request.get_json()
        print(args["user_input"])
        printer.print(args["user_input"])
        printer.feed(1)

class LFCR(Resource):

    def get(self):
        printer.feed(1)

class Bold(Resource):

    def post(self):
        args = request.get_json()
        if args["bold"] is True:
            printer.boldOn()
        else:
            printer.boldOff()

api.add_resource(Test, "/test/")
api.add_resource(PrintText, "/print_text/")
api.add_resource(LFCR, "/lfcr/")
api.add_resource(Bold, "/bold/")

if __name__ == "__main__":
    app.run(port=5001, debug=True)
