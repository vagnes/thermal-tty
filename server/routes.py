from server import app, api, printer
from flask import request
from flask_restful import Resource
import requests
import adafruit_thermal_printer as aft


class PrefixMiddleware(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):

        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]


app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api')


class Test(Resource):

    def get(self):
        return "WIRKLS"


class PrintText(Resource):

    def post(self):
        printer.warm_up()
        args = request.get_json()
        printer.print(args["user_input"])
        printer.feed(1)


class LFCR(Resource):

    def get(self):
        printer.feed(1)


class Format(Resource):

    def post(self):
        args = request.get_json()

        # bold
        if args["bold"] is True:
            printer.bold = True
        else:
            printer.bold = False

        # center
        if args["center"] is True:
            printer.justify = aft.JUSTIFY_CENTER
        else:
            printer.justify = aft.JUSTIFY_LEFT

        # double height
        if args["height2x"] is True:
            printer.size = aft.SIZE_LARGE
        else:
            printer.size = aft.SIZE_SMALL

        # double width
        if args["underline"] is True:
            printer.underline = aft.UNDERLINE_THIN
        else:
            printer.underline = None

# class Barcode(Resource):

#     def post(self):

#         args = request.get_json()

#         print(args["user_input"], args["barcode_type"])

#         barcode_type = "printer." + args["barcode_type"]
#         print(barcode_type)

#         printer.print_barcode(args["user_input"], eval(barcode_type))


api.add_resource(Test, "/test/")
api.add_resource(PrintText, "/print_text/")
api.add_resource(LFCR, "/lfcr/")
api.add_resource(Format, "/format/")
# api.add_resource(Barcode, "/print_barcode/")

if __name__ == "__main__":
    app.run(port=5001, debug=True)
