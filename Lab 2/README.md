# Interactive Prototyping: The Clock of Pi
**NAMES OF COLLABORATORS HERE**

Does it feel like time is moving strangely during this semester?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

**Please indicate anyone you collaborated with on this Lab here.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

## Prep

Lab Prep is extra long this week. Make sure to start this early for lab on Thursday.

1. ### Set up your Lab 2 Github

Before the start of lab Thursday, [pull changes from the Interactive Lab Hub](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md#to-pull-lab-updates) so that you have your own copy of Lab 2 on your own lab hub.


  If you are organizing your Lab Hub through folder in local machine, go to terminal, cd into your Interactive-Lab-Hub folder and run:

  ```
  Interactive-Lab-Hub $ git remote add upstream https://github.com/FAR-Lab/Interactive-Lab-Hub.git
  Interactive-Lab-Hub $ git pull upstream Fall2022
  ```
  
  The reason why we are adding a upstream with **course lab-hub** instead of yours is because the local Interactive-Lab-Hub folder is linked with your own git repo already. Try typing ``git remote -v`` and you should see there is the origin branch with your own git repo. We here add the upstream to get latest updates from the teaching team by pulling the **course lab-hub** to your local machine. After your local folder got the latest updates, push them to your remote git repo by running:
  
  ```
  Interactive-Lab-Hub $ git add .
  Interactive-Lab-Hub $ git commit -m "message"
  Interactive-Lab-Hub $ git push
  ```
  Your local and remote should now be up to date with the most recent files.


2. ### Get Kit and Inventory Parts
Prior to the lab session on Thursday, taken inventory of the kit parts that you have, and note anything that is missing:

***Update your [parts list inventory](partslist.md)***

3. ### Prepare your Pi for lab this week
[Follow these instructions](prep.md) to download and burn the image for your Raspberry Pi before lab Thursday.




## Overview
For this assignment, you are going to 

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the \*\*\***stars**\*\*\*. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. 
### Connect to your Pi
Just like you did in the lab prep, ssh on to your pi. Once you get there, create a Python environment by typing the following commands.

```
ssh pi@<your Pi's IP address>
...
pi@ixe00:~ $ virtualenv circuitpython
pi@ixe00:~ $ source circuitpython/bin/activate
(circuitpython) pi@ixe00:~ $ 

```
### Setup Personal Access Tokens on GitHub
The support for password authentication of GitHub was removed on August 13, 2021. That is, in order to link and sync your own lab-hub repo with your Pi, you will have to set up a "Personal Access Tokens" to act as the password for your GitHub account on your Pi when using git command, such as `git clone` and `git push`.

Following the steps listed [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) from GitHub to set up a token. Depends on your preference, you can set up and select the scopes, or permissions, you would like to grant the token. This token will act as your GitHub password later when you use the terminal on your Pi to sync files with your lab-hub repo.


## Part B. 
### Try out the Command Line Clock
Clone your own lab-hub repo for this assignment to your Pi and change the directory to Lab 2 folder (remember to replace the following command line with your own GitHub ID):

```
(circuitpython) pi@ixe00:~$ git clone https://github.com/<YOURGITID>/Interactive-Lab-Hub.git
(circuitpython) pi@ixe00:~$ cd Interactive-Lab-Hub/Lab\ 2/
```
Depends on the setting, you might be asked to provide your GitHub user name and password. Remember to use the "Personal Access Tokens" you just set up as the password instead of your account one!


Install the packages from the requirements.txt and run the example script `cli_clock.py`:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ pip install -r requirements.txt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python cli_clock.py 
02/24/2021 11:20:49
```

The terminal should show the time, you can press `ctrl-c` to exit the script.
If you are unfamiliar with the Python code in `cli_clock.py`, have a look at [this Python refresher](https://hackernoon.com/intermediate-python-refresher-tutorial-project-ideas-and-tips-i28s320p). If you are still concerned, please reach out to the teaching staff!


## Part C. 
### Set up your RGB Display
We have asked you to equip the [Adafruit MiniPiTFT](https://www.adafruit.com/product/4393) on your Pi in the Lab 2 prep already. Here, we will introduce you to the MiniPiTFT and Python scripts on the Pi with more details.

<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="200" />

The Raspberry Pi 3 has a variety of interfacing options. When you plug the pi in the red power LED turns on. Any time the SD card is accessed the green LED flashes. It has standard USB ports and HDMI ports. Less familiar it has a set of 20x2 pin headers that allow you to connect a various peripherals.

<img src="https://maker.pro/storage/g9KLAxU/g9KLAxUiJb9e4Zp1xcxrMhbCDyc3QWPdSunYAoew.png" height="400" />

To learn more about any individual pin and what it is for go to [pinout.xyz](https://pinout.xyz/pinout/3v3_power) and click on the pin. Some terms may be unfamiliar but we will go over the relevant ones as they come up.

### Hardware (you have done this in the prep)

From your kit take out the display and the [Raspberry Pi 3](https://cdn-shop.adafruit.com/970x728/3775-07.jpg)

Line up the screen and press it on the headers. The hole in the screen should match up with the hole on the raspberry pi.

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/087/539/medium640/adafruit_products_4393_quarter_ORIG_2019_10.jpg?1579991932" height="200" />
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png" height="200">
</p>

### Testing your Screen

The display uses a communication protocol called [SPI](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/) to speak with the raspberry pi. We won't go in depth in this course over how SPI works. The port on the bottom of the display connects to the SDA and SCL pins used for the I2C communication protocol which we will cover later. GPIO (General Purpose Input/Output) pins 23 and 24 are connected to the two buttons on the left. GPIO 22 controls the display backlight.

We can test it by typing 
```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python 
.py
```

You can type the name of a color then press either of the buttons on the MiniPiTFT to see what happens on the display! You can press `ctrl-c` to exit the script. Take a look at the code with
```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ cat screen_test.py
```


Below is a short recording of testing the `screen_test.py` where I input a color (red) and use the button to initiate color display on the raspberry pi:

![color_screen_test_video](https://github.com/hjkim63/Interactive-Lab-Hub/blob/0f21f89561c14820b4b935dfce506496b66ae069/Lab%202/screen_test_color.mov)

#### Displaying Info with Texts
You can look in `stats.py` for how to display text on the screen!

Below is an image of the raspberry pi display running the `stats.py` and simply adding a text to test text screen modification:

![stats_test_display](https://github.com/hjkim63/Interactive-Lab-Hub/blob/0f21f89561c14820b4b935dfce506496b66ae069/Lab%202/stats_test.png)

#### Displaying an image

You can look in `image.py` for an example of how to display an image on the screen. Can you make it switch to another image when you push one of the buttons?



## Part D. 
### Set up the Display Clock Demo
Work on `screen_clock.py`, try to show the time by filling in the while loop (at the bottom of the script where we noted "TODO" for you). You can use the code in `cli_clock.py` and `stats.py` to figure this out.

### How to Edit Scripts on Pi
Option 1. One of the ways for you to edit scripts on Pi through terminal is using [`nano`](https://linuxize.com/post/how-to-use-nano-text-editor/) command. You can go into the `screen_clock.py` by typing the follow command line:
```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
```
You can make changes to the script this way, remember to save the changes by pressing `ctrl-o` and press enter again. You can press `ctrl-x` to exit the nano mode. There are more options listed down in the terminal you can use in nano.

Option 2. Another way for you to edit scripts is to use VNC on your laptop to remotely connect your Pi. Try to open the files directly like what you will do with your laptop and edit them. Since the default OS we have for you does not come up a python programmer, you will have to install one yourself otherwise you will have to edit the codes with text editor. [Thonny IDE](https://thonny.org/) is a good option for you to install, try run the following command lines in your Pi's ternimal:

  ```
  pi@ixe00:~ $ sudo apt install thonny
  pi@ixe00:~ $ sudo apt update && sudo apt upgrade -y
  ```

Now you should be able to edit python scripts with Thonny on your Pi.


## Part E.
### Modify the barebones clock to make it your own

Does time have to be linear?  How do you measure a year? [In daylights? In midnights? In cups of coffee?](https://www.youtube.com/watch?v=wsj15wPpjLY) Can you make time interactive? You can look in `screen_test.py` for examples for how to use the buttons.
Please sketch/diagram your clock idea. (Try using a [Verplank digram](http://www.billverplank.com/IxDSketchBook.pdf)!

For my Clock of Pi project, I wanted to think about different ways to measure time as well as focus the brainstorming on 1)the different modes of input/output and 2)the interactions. Some ideas of input began with thinking about the various devices we could connect to the rasberry pi, such as the webcam, joystick, and buttons and outputs mainly through the screen, but varied from text to color. In terms of the interaction, I thought about passive vs. active interactions when thinking about the input a person could give (i.e. passive as in sitting in front of a webcam for "inputting" image for object dection vs. active as in pressing a button when the person is "inputting" data for time measurement, such as pressing the button everytime they drink water). 

Ultimately, I wanted to build a "Time to Stretch Clock" that would sit on a desk and measure how long someone has been standing in front of desk. Based on object dectection of a person using a webcam and the opencv library, the clock would show varied texts depending on how long the person has been in front of the desk clock, such as "Time to stretch" when the person has been at the desk for 45-50 consecutive minutes or "Time for a walk!" when the persons cumulative time at their desk has been 4+ hours. I was not able to implement this idea yet for Lab 2i. Below is a sketch of my idea concept brainstorming:

![brainstorming_sketch](https://github.com/hjkim63/Interactive-Lab-Hub/blob/b05afc90cd7091da67808edf5f877743761f5992/Lab%202/clock_brainstorming_sketch.png)

\*\*\***A copy of your code should be in your Lab 2 Github repo.**\*\*\*

After you edit and work on the scripts for Lab 2, the files should be upload back to your own GitHub repo! You can push to your personal github repo by adding the files here, commiting and pushing.

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git add .
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git commit -m 'your commit message here'
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ git push
```

After that, Git will ask you to login to your GitHub account to push the updates online, you will be asked to provide your GitHub user name and password. Remember to use the "Personal Access Tokens" you set up in Part A as the password instead of your account one! Go on your GitHub repo with your laptop, you should be able to see the updated files from your Pi!



## Part F. 

To start with, I simply experimented using the buttons to display the current time (code in `screen_clock.py` file):

![simple clock display](https://github.com/hjkim63/Interactive-Lab-Hub/blob/0f21f89561c14820b4b935dfce506496b66ae069/Lab%202/simple_clock_display.png)

<!-- ## Make a short video of your modified barebones PiClock -->

<!-- \*\*\***Take a video of your PiClock.**\*\*\* -->


## Part G. 

Below are sketches of storboards to better understand the context of the device and the user's interactions as well as additional features to build out (either within or beyond this lab).

![storyboard_brainstorm_a](https://github.com/hjkim63/Interactive-Lab-Hub/blob/93fba073ec64c11d02469ea91644b78b45ce32c3/Lab%202/storyboard_A.jpg)

![storyboard_brainstorm_b](https://github.com/hjkim63/Interactive-Lab-Hub/blob/93fba073ec64c11d02469ea91644b78b45ce32c3/Lab%202/storyboard_b.jpg)

# Prep for Part 2

1. Pick up remaining parts for kit on Thursday lab class. 
<!-- 2. Check the updated  and let the TA know if there is any part missing. -->

Picked up missing parts: Red LED light [parts list inventory](partslist.md)
  

2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)

### Feedback from Michael Kelleher, Sidarth Wadhwa

Positives
- Thinking about differentiated added value from alternative devices: While there are other wearable devices, like the Apple Watch, that has similar functionalities, this device would still provide some functionality without having to wear the device the entire day.

Some design considerations:
- Edge cases & counting "sitting down time":
- Privacy: How does the user feel about having a camera on the entire time? Where is the object detection being done?
- Notification process: would the user be notifed using sound, display (color display or image display, text display) or other sensory alarms (vibration)? Would the user still be notifed when they are during a meeting or in a super productive work flow? What is the range of activities to take a break --stretching, walk? 
- Turning off the alarm: how does the user ignore or snooze the alarm?


# Lab 2 Part 2

The updated code for Lab 2 Part 2  is in the file `lab2i.py`.

<!-- Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required. -->

Taking the input from peers and revisiting previous brainstorming sessions, I made the following changes to the interaction and system design: 
- Instead of using a webcam to be constantly running in the background, leading to heavy computation loads and user privacy concerns ("user might feel uncomfortable and monitored with a webcam constantly running"), I decided to use the buttons on the display to log the user's sitting times
- However, this still comes with caveats that the user might notice or remember to press the button to log sitting time. I tried adding a white blinking screen as the default screen so that the user notices the device, but this felt distracting. Future design iterations could experiment with this initial interaction --how to initiate while not being too invasive or distracting.
- Provide options to snooze the stretch reminder, in case the user is during a remote meeting or lecture. A next step or additional feature for this functionality could be to connect the device to the user's digital calenda (Google Calendar API) to automatically snooze or only give a "gentle nudge" during busy, occupied meeting times. 
- Going beyond simple text displays, for example using different images to provide users with possible ideas for stretching and additional movement. 

Below is a product introduction and demo video (and screenshots from the demo video):

![product_intro_demo_video](https://github.com/hjkim63/Interactive-Lab-Hub/blob/63c6b226137032fe824c7dd5e8009d43031ae5e5/Lab%202/demo.mp4)

_For purposes of testing and the demo video, the threshold for "stretching time" was only 1 minute, but in reality, would likely be 45 min - 1hr_

![demo_screenshots](https://github.com/hjkim63/Interactive-Lab-Hub/blob/35ab06f027b625ddedb4ba980e356122d22fcc01/Lab%202/demo_screenshots.png)
<!-- As always, make sure you document contributions and ideas from others explicitly in your writeup. -->

<!-- You are permitted (but not required) to work in groups and share a turn in; you are expected to make equal contribution on any group work you do, and N people's group project should look like N times the work of a single person's lab. What each person did should be explicitly documented. Make sure the page for the group turn in is linked to your Interactive Lab Hub page.  -->


