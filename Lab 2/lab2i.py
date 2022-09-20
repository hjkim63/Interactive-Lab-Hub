import digitalio
import board
import time
from time import strftime, sleep
from datetime import datetime, timedelta
import subprocess

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import webcolors

from PIL import Image, ImageDraw, ImageFont



# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)


# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

#now = datetime.now()
stretch_time = 0
a = 0

while True:

    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    greeting_1 = "Sitting down?"
    greeting_2 = "< Press me!"

    # Write four lines of text.
    y = top
    draw.text((x, y), greeting_1, font=font, fill="#FFFFFF")
    y += font.getsize(greeting_1)[1]
    draw.text((x, y), greeting_2, font=font, fill="#FFFF00")
    y += font.getsize(greeting_2)[1]

    # Display image.
    disp.image(image, rotation)
    time.sleep(0.1)



    if buttonB.value and not buttonA.value:  # just button A pressed
        a += 1
        
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))

        curr_time = strftime("%H:%M:%S")
        stretch_time = datetime.strptime(curr_time, "%H:%M:%S") + timedelta(minutes=1)
        
        stretch_time = format(stretch_time, '%H:%M:%S')

        start_1 = "It's now " + str(strftime("%H:%M:%S"))
        start_2 = "I'll light up when"
        start_3 = "it's time to stetch"
        stretch_ = str(stretch_time)

        y = top
        draw.text((x, y), start_1, font=font, fill="#FFFFFF")
        y += font.getsize(start_1)[1]
        draw.text((x, y), start_2, font=font, fill="#FFFF00")
        y += font.getsize(start_2)[1]
        draw.text((x, y), start_3, font=font, fill="#0000FF")
        y += font.getsize(start_3)[1]
        draw.text((x, y), stretch_, font=font, fill="#0000FF")
        y += font.getsize(stretch_)[1]

        # Display image.
        disp.image(image, rotation)
        time.sleep(10)
    
    #sit_start = strftime("%H:%M:%S")
    #stretch_time = datetime.strptime(sit_start, "%H:%M:%S")  + timedelta(seconds=2)
    #stretch_time = stretch_time.time()
   
    # display.fill(screenColor) # set the screen to the users color
    # if buttonA.value and not buttonB.value:  # just button B pressed
        # disp.fill(color565(255, 255, 255))  # set the screen to white
        # display.fill(color565(0, 255, 0))  # green

        # Display image.
        # disp.image(image, rotation)
        # time.sleep(0.1)       

    if a >=1:
        
        stretch_time = datetime.strptime(stretch_, "%H:%M:%S")
        #print("now_min",str(now.minute))
        #print("stretch_time", str(stretch_time.minute))

        if datetime.now().hour == stretch_time.hour and datetime.now().minute == stretch_time.minute:
            
            draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))

            stretch_1 = "Let's stretch!"
            stretch_2 = "Busy right now?"
            stretch_3 = "Snooze for a hot sec!"

            y = top
            draw.text((x, y), stretch_1, font=font, fill="#FFFFFF")    
            y += font.getsize(stretch_1)[1]
            draw.text((x, y), stretch_2, font=font, fill="#FFFF00")
            y += font.getsize(stretch_2)[1]
            draw.text((x, y), stretch_3, font=font, fill="#0000FF")
            y += font.getsize(stretch_3)[1]

            # Display image.
            disp.image(image, rotation)
            time.sleep(30)   