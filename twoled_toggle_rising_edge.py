import RPi.GPIO as GPIO
import time

LED1 = 5 # GPIO5
LED2 = 6 # GPIO6
SWITCH = 14 # GPIO14
state1 = GPIO.LOW # 초기 상태
state2 = GPIO.LOW # 초기 상태

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(SWITCH, GPIO.IN) # GPIO14를 스위치 입력 핀으로 사용
GPIO.setup(LED1, GPIO.OUT) # GPIO5를 LED1 출력 핀으로 사용
GPIO.setup(LED2, GPIO.OUT) # GPIO6를 LED2 출력 핀으로 사용

def rising_edge_callback(channel):
    print('RISING EDGE on Channel', channel)
    global state1,state2
    if (state1 == GPIO.LOW and state2 == GPIO.LOW):
        GPIO.output(LED1, GPIO.HIGH) # LED1 on
        state1 = GPIO.HIGH
    elif(state1 == GPIO.HIGH and state2 == GPIO.LOW):
        GPIO.output(LED2,GPIO.HIGH) # LED2 on
        state2 = GPIO.HIGH
    else:
        GPIO.output(LED1, GPIO.LOW) # LED1 off
        GPIO.output(LED2, GPIO.LOW) # LED2 off
        state1 = GPIO.LOW
        state2 = GPIO.LOW


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