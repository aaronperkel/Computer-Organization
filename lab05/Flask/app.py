from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

RED_PIN = 18
YELLOW_PIN = 15

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)

app = Flask(__name__)

@app.route("/led_on_r", methods=["POST"])
def led_on_r():
    print("LED on")
    GPIO.output(RED_PIN, GPIO.HIGH)
    return "ok"

@app.route("/led_off_r", methods=["POST"])
def led_off_r():
    print("LED off")
    GPIO.output(RED_PIN, GPIO.LOW)
    return "ok"

@app.route("/led_on_y", methods=["POST"])
def led_on_y():
    print("LED on")
    GPIO.output(YELLOW_PIN, GPIO.HIGH)
    return "ok"

@app.route("/led_off_y", methods=["POST"])
def led_off_y():
    print("LED off")
    GPIO.output(YELLOW_PIN, GPIO.LOW)
    return "ok"

@app.route("/blink_start", methods=["POST"])
def blink_start():
    print("blinking started")
    return "ok"

@app.route("/blink_stop", methods=["POST"])
def blink_stop():
    print("blinking stopped")
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return render_template("button.html", title="Button", name="Aaron Perkel")
