import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import RPi.GPIO as GPIO

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

RST = None     
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)


disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
x=0

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding

font = ImageFont.load_default()

GPIO.setmode(GPIO.BCM)

TRIG = 21 
ECHO = 20

print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

try:
  while True:
    
    GPIO.output(TRIG, False)
    print ("Waiting..")
    time.sleep(1)
    
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print ("Measured Distance:",distance,"cm")
    result = str(distance)

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
   
    # Write two lines of text.
    draw.text((x,top),"Distance", font=font,fill=255)
    draw.text((x+45,top+10),"cm", font=font,fill=255)
    draw.text((x+10, top+10), result,  font=font, fill=255)
    
  
    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(.1)
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Measurement Stopped by User")
    disp.clear()
    disp.display()
    GPIO.cleanup()















