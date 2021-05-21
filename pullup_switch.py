# pullup_switch.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14, GPIO.IN) # GPIO14를 입력 핀으로 사용한다.

def rising_edge_callback(channel):
    print('UP on Channel', channel)
    
GPIO.add_event_detect(14, GPIO.RISING,
    callback=rising_edge_callback, bouncetime=300)