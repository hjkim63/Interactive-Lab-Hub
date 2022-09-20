import digitalio
import board
import time
from time import strftime, sleep
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


while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # cmd = "hostname -I | cut -d' ' -f1"
    greeting_1 = "Sitting down?"
    greeting_2 = "Press me!"
    start_1 = "It's now " + str(strftime("%H:%M:%S"))
    start_2 = "I'll light up"
    start_3 = "when it's time to stetch"
        

    # Write four lines of text.
    y = top
    draw.text((x, y), greeting, font=font, fill="#FFFFFF")
    y += font.getsize(greeting_1)[1]
    draw.text((x, y), greeting_2, font=font, fill="#FFFF00")
    y += font.getsize(greeting_2)[1]
    # draw.text((x, y), greeting_3, font=font, fill="#0000FF")
    # y += font.getsize(greeting_3)[1]
    # draw.text((x, y), Temp, font=font, fill="#FF00FF")

    # Display image.
    disp.image(image, rotation)
    time.sleep(0.1)

# while True:
#     print (strftime("%m/%d/%Y %H:%M:%S"), end="", flush=True)
#     print("\r", end="", flush=True)
#     sleep(1)


# Main loop:
while True:
    if buttonA.value and buttonB.value:
        backlight.value = False  # turn off backlight
    else:
        backlight.value = True  # turn on backlight
    if buttonB.value and not buttonA.value:  # just button A pressed
        curr_time = strftime("%m/%d/%Y %H:%M:%S")
        
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        y = top
        draw.text((x, y), start_1, font=font, fill="#FFFFFF")
        y += font.getsize(start_1)[1]
        draw.text((x, y), start_2, font=font, fill="#FFFF00")
        y += font.getsize(start_2)[1]
        draw.text((x, y), start_3, font=font, fill="#0000FF")
        y += font.getsize(start_3)[1]

        # display.fill(screenColor) # set the screen to the users color
    if buttonA.value and not buttonB.value:  # just button B pressed
        display.fill(color565(255, 255, 255))  # set the screen to white
    if not buttonA.value and not buttonB.value:  # none pressed
        display.fill(color565(0, 255, 0))  # green