from flask import Flask, request, jsonify
from service import MembersService


app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/members", methods=["POST"])
def create_member():
    return jsonify(MembersService().create(request.get_json()))


@app.route("/members", methods=["GET"])
def list_member():
    return jsonify(MembersService().list())


if __name__ == "__main__":
    app.run(debug=True, port=8889)
