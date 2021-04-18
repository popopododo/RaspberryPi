import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.IN) # GPIO14 is the input

try:
    while True:
        if(GPIO.input(14)== GPIO.HIGH):
            print('HIGH')
        else:
            print('LOW')
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("Exit...")
finally:
    GPIO.cleanup()
    