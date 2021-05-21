from gpiozero import LED
import time

red=LED(2)
yellow=LED(3)
green=LED(4)

count=0
while True:
    red.on()
    yellow.off()
    green.off()
    time.sleep(0.3)
    
    red.off()
    yellow.on()
    green.off()
    time.sleep(0.3)
    
    red.off()
    yellow.off()
    green.on()
    time.sleep(0.3)
    
    red.off()
    yellow.on()
    green.on()
    time.sleep(0.3)
    
    red.on()
    yellow.off()
    green.on()
    time.sleep(0.3)
    
    red.on()
    yellow.on()
    green.off()
    time.sleep(0.3)

    