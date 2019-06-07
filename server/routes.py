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

class Format(Resource):

    def post(self):
        args = request.get_json()

        print(args)

        #bold
        if args["bold"] is True:
            printer.boldOn()
        else:
            printer.boldOff()

        #center
        if args["center"] is True:
            printer.justify("C")
        else:
            printer.justify("L")

        #double height
        if args["height2x"] is True:
            printer.doubleHeightOn()
        else:
            printer.doubleHeightOff()
        
        #double width
        if args["underline"] is True:
            printer.underlineOn()
        else:
            printer.underlineOff()


api.add_resource(Test, "/test/")
api.add_resource(PrintText, "/print_text/")
api.add_resource(Format, "/format/")

if __name__ == "__main__":
    app.run(port=5001, debug=True)