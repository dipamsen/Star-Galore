from flask import Flask, jsonify, request
from data import data
from flask_cors import CORS

data_dict = {}
for sd in data:
  data_dict[sd['name']] = sd


app = Flask(__name__)
CORS(app)


@app.route("/")
def get_all():
  return jsonify({
      "status": "success",
      "data": data
  }), 200


@app.route("/star")
def get_star():
  try:
    name = request.args.get("name")
    return jsonify({
        "status": "success",
        "data": data_dict[name]
    }), 200
  except:
    return jsonify({
        "status": "error",
    }), 503


if(__name__ == "__main__"):
  app.run()
