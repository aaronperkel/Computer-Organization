from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("binaryconverter.html")

@app.route("/convert_binary", methods=["GET"])
def convert_binary():
    binary_string = request.values["binary_string"]
    return json.dumps(to_decimal(binary_string))

def to_decimal(binary_string):
	power = 0
	base_ten = 0
	
	for digit in reversed(binary_string):
		if digit == '1':
			base_ten += 2 ** power
		power += 1
	return base_ten
