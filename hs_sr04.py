# hs_sr04.py
import RPi.GPIO as GPIO
import time

class HCSR04:
    def __init__(self, trigger, echo):
        # set GPIO Pins
        self.GPIO_TRIGGER = trigger # trigger pin
        self.GPIO_ECHO = echo
    
        # set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
    
    def distance(self):
        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)
        
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)
        
        # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()
            
        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()
            
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        
        return distance
    
if __name__ == '__main__':
    
    GPIO.setmode(GPIO.BCM)
    sr04 = HCSR04(trigger=20, echo=21) # 초음파 센서 객체 생성
    
    try:
        while True:
            dist = sr04.distance()
            print ('Measured Distance = %.1f cm' % dist)
            time.sleep(1)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print('Measurement stopped by User')
        del sr04
        GPIO.cleanup()
    
    
    