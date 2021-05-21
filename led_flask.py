# led_flask.py
import RPi.GPIO as GPIO
from flask import Flask,render_template,Response

app = Flask(__name__)

LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

@app.route('/') # Decorator

def hello():
    return '<font size=10> HELLO, LED! </font>'

@app.route('/led')
def ledbutton():
    return render_template('index.html')

'''
@app.route('/led/on')
def led_on():
    GPIO.output(LED,GPIO.HIGH)
    return '<font size=10> LED{} ON! </font>'.format(LED)

@app.route('/led/off')
def led_off():
    GPIO.output(LED,GPIO.LOW)
    return '<font size=10> LED{} OFF! </font>'.format(LED)
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0')