# led_toggle_rising_edge.py
import RPi.GPIO as GPIO
import time


LED = 5 # GPIO5
SWITCH = 14 # GPIO14
state = GPIO.LOW # 초기 상태

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(SWITCH, GPIO.IN) # GPIO14를 스위치 입력 핀으로 사용
GPIO.setup(LED, GPIO.OUT) # GPIO5를 LED 출력 핀으로 사용

# state가 LOW이면 HIGH로 변환, HIGH이면 LOW로 변환

def rising_edge_callback(channel):
    print('RISING EDGE on Channel', channel)
    global state
    if (state == GPIO.LOW):
        GPIO.output(LED, GPIO.HIGH) # LED on
        state = GPIO.HIGH
    else:
        GPIO.output(LED, GPIO.LOW) # LED off
        state = GPIO.LOW
        
# GPIO14에서 RISING edge가 탐지되면 rising_edge_callback() 호출
GPIO.add_event_detect(SWITCH, GPIO.RISING,
    callback=rising_edge_callback, bouncetime=300)
try:
 # do something here
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('Exit ...')
finally:
    GPIO.cleanup()