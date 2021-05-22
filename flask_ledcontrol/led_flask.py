# led_flask.py
import RPi.GPIO as GPIO
from flask import Flask,render_template,Response

app = Flask(__name__)

LED = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

@app.route('/') # Decorator
def hello():
    return '<font size=10> HELLO, LED! </font>'

@app.route('/led/')
def led():
    return render_template("index.html")


@app.route('/led/on')
def led_on():
    GPIO.output(LED,GPIO.HIGH)
    return '<font size=10> HELLO, LED! </font>'


@app.route('/led/off')
def led_off():
    GPIO.output(LED,GPIO.LOW)
    return '<font size=10> GOOD BYE, LED! </font>'


'''


@app.route('/led/on')
def led_on():
    GPIO.output(LED,GPIO.HIGH)
    return '<font size=10> LED on </font>'
        

@app.route('/led/off', methods=['POST')
def led_off():
    GPIO.output(LED,GPIO.LOW)
    return '<font size=10> LED off </font>'
 '''   
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=False)