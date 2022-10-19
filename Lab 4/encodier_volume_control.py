#encoder_vol
# code to user the rotary encoder to process signals that adjust volume of audio on the Raspberry Pi

# Referenced the following codes:

# SPDX-FileCopyrightText: 2021 John Furcean
# SPDX-License-Identifier: MIT

# Sid's e-classroom: https://gist.github.com/shivasiddharth/6aba5fa187c8ce463259f18eb7171a1f

import board
from adafruit_seesaw import seesaw, rotaryio, digitalio
import alsaaudio
from time import sleep


seesaw = seesaw.Seesaw(board.I2C(), addr=0x36)

seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
print("Found product {}".format(seesaw_product))
if seesaw_product != 4991:
    print("Wrong firmware loaded?  Expected 4991")

seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
button = digitalio.DigitalIO(seesaw, 24)
button_held = False

encoder = rotaryio.IncrementalEncoder(seesaw)
last_position = None

#set audio device so volumne controls are implmented
m = alsaaudio.Mixer()

# Set minimum and maximum values
min = 0
max = 100

# Set volume change step size
volume_step_size=5

# Get current volume and mute settings
is_Muted = m.getmute()[0]
volume = m.getvolume()[0]

if is_Muted == 0:
    is_Muted=False
else:
    is_Muted=True
print("Mute State: " + str(is_Muted))
print("Volume: " + str(volume))
print("")   

while True:
    # negate the position to make clockwise rotation positive
    position = -encoder.position
    
    #increase volume if turned to right
    if position != last_position:
        volume += volume_step_size/2
        if volume > max:
            volume = max
    
    #decrease volumne if turned to left
    else:
        volume -= volume_step_size/2
                if volume < min:
            volume = min
    m.setvolume(int(volume))
        
        
    if is_Muted:
        is_Muted = False
        m.setmute(0)
        print("Mute State: " + str(is_Muted))
        print("Volume: " + str(int(volume)))
        print("")

        last_position = position
        print("Position: {}".format(position))

    else:
        is_Muted = True
        m.setmute(1)
        print("Mute State: " + str(is_Muted))
        print("Volume: " + str(int(volume)))
        print("")
    sleep(0.05)


#     if not button.value and not button_held:
#         button_held = True
#         print("Button pressed")

#     if button.value and button_held:
#         button_held = False
#         print("Button released")
