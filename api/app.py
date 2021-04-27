from flask import Flask, jsonify, request
from data import data

data_dict = {}
for sd in data:
  data_dict[sd['name']] = sd


app = Flask(__name__)


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


app.run()
