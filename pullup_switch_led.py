import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.IN)
GPIO.setup(5,GPIO.OUT)

try:
    while True:
        if (GPIO.input(14) == GPIO.HIGH):
            print('HIGH')
            GPIO.output(5,GPIO.LOW)
        else:
            print('LOW')
            GPIO.output(5,GPIO.HIGH)
            
    time.sleep(0.1)
    
except KeyboardInterrupt:
    print('Exit ...')
finally:
    GPIO.cleanup()