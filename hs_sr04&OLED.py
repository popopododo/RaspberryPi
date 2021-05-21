import RPi.GPIO as GPIO
import time
import Adafruit_SSD1306
from PIL import Image,ImageDraw,ImageFont


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
    
    TOP = -2
    PADDING = 2
    RST = None
    disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
    disp.begin()
    
    WIDTH = disp.width
    HEIGHT = disp.height
    frame = Image.new('1',(WIDTH,HEIGHT))
    
    draw = ImageDraw.Draw(frame)
    font = ImageFont.load_default()
    disp.clear()
    
    try:
        while True:
            dist = sr04.distance()
            draw.text((PADDING,TOP),'Distance = %.1f cm'%dist,font=font,fill=255)
            disp.image(frame)
            disp.display()
            time.sleep(1)
    except KeyboardInterrupt:
        print('Measurement stopped by User')
        disp.clear()
        disp.display()
        del sr04
        GPIO.cleanup()