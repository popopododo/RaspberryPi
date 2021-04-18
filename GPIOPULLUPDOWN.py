import RPi.GPIO as GPIO
import time

print(GPIO.VERSION)
GPIO.setmode(GPIO.BOARD)
PIN=18
# GPIO.setup(PIN,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(PIN,GPIO.IN,GPIO.PUD_DOWN)
while(True):
    time.sleep(0.5) # 0.5 sec sleep
    r = GPIO.input(PIN)
    print('r=',r)