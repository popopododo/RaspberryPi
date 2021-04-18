import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

for x in range(100):
    print('LED ON')
    GPIO.output(18,1) # 18 PIN print 1 (3.3v)
    time.sleep(0.1)
    
    print('LED OFF')
    GPIO.output(18,0) # PIN 18 print 0
    time.sleep(0.1)
    
GPIO.cleanup()
print('End of LED demo')