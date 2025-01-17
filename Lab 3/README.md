# Chatterboxes
**NAMES OF COLLABORATORS HERE**
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Web Camera If You Don't Have One

Students who have not already received a web camera will receive their [IMISES web cameras](https://www.amazon.com/Microphone-Speaker-Balance-Conference-Streaming/dp/B0B7B7SYSY/ref=sr_1_3?keywords=webcam%2Bwith%2Bmicrophone%2Band%2Bspeaker&qid=1663090960&s=electronics&sprefix=webcam%2Bwith%2Bmicrophone%2Band%2Bsp%2Celectronics%2C123&sr=1-3&th=1) on Thursday at the beginning of lab. If you cannot make it to class on Thursday, please contact the TAs to ensure you get your web camera. 

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. There are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2022Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.

### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using the microphone and speaker on your webcamera. In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. 
Now, we need to find out where your webcam's audio device is connected to the Pi. Use `arecord -l` to get the card and device number:
```
pi@ixe00:~/speech2text $ arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: Device [Usb Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```
The example above shows a scenario where the audio device is at card 1, device 0. Now, use `nano vosk_demo_mic.sh` and change the `hw` parameter. In the case as shown above, change it to `hw:1,0`, which stands for card 1, device 0.  

Now, look at which camera you have. Do you have the cylinder camera (likely the case if you received it when we first handed out kits), change the `-r 16000` parameter to `-r 44100`. If you have the IMISES camera, check if your rate parameter says `-r 16000`. Save the file using Write Out and press enter.

Then try `./vosk_demo_mic.sh`

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

## Device: Focus

### Storyboard

**Context**

From children, students, young professionals to older adults, many individuals have a multitude of tasks to complete throughout the day but often struggle to finish these tasks or finish them in the wrong order (finish the trivial, easier tasks first, but procrastinate the more important but harder tasks). People struggle to scope and prioritize their daily to-dos.  

**Device & Interaction**

This device "Focus" aims to create focus for users. The device uses dialogue to ask about a user's expected tasks and continues a dialogue to ask for the top 3 tasks, which task to start with, and how long the user expects it to take so that the device can check back to see if the task is finished. This last function is borrowed from my Lab 2 Clock of Pi project !["Bending time clock"](https://github.com/hjkim63/Interactive-Lab-Hub/blob/0fe1215f7cce4ac32dab34fbfd0b45e2433bda32/Lab%202/README.md) where the Raspberry Pi reminds the user when they should get up and stretch after sitting at their desk for extended periods of time.

_Below is the storyboard of the use case of this device:_

![storyboard_v1](https://github.com/hjkim63/Interactive-Lab-Hub/blob/37fe33f119a139ae5c8720ed1cc3dad7c7be3da2/Lab%203/focus_storyboard_1.png)


<!-- Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.)  -->

<!-- \*\***Post your storyboard and diagram here.**\*\* -->

<!-- Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses.  -->

<!-- \*\***Please describe and document your process.**\*\* -->
Below is the initial dialogue board:

In the initial trial of the dialogue, I tried to anticipate time lags in the voice interaction so that the design of the dialogue could add to a more realistic conversation without the device being programmed to actually understand everyhing the user is saying. For example, I anticipated that when you first ask someone what they're going to finish, they might need a few seconds to think; I also assumed that peopple will most likely list out too many tasks they won't be able to finish so added a follow up question to "trim down" the list of tasks to top 3 priorities.

<!-- ![dialogue_v1](https://github.com/hjkim63/Interactive-Lab-Hub/blob/021ef687ef2e0eceb6817c17916abf2bb31502f8/Lab%203/dialogue_script_part1.png) -->

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/021ef687ef2e0eceb6817c17916abf2bb31502f8/Lab%203/dialogue_script_part1.png" width=50% height=50%>



### Acting out the dialogue

(partner: non-Cornell Tech friend)
*Without sharing the script*, I tried out the initially design dialogue, where I acted as the device and the friend was the user. I designed the acting out exercise to that the user was looking at a smartphone screeen with a random app with a face to see how the user would reply and react to the conversation knowing they were talking to a device, rather than a person (if my physical presence was on the screen). 

Here is the recording of the interaction: ![dialogue_act_out](https://github.com/hjkim63/Interactive-Lab-Hub/blob/100082caeedd46f8426b3721bebb18ecfd05c2a0/Lab%203/dialogue_act_out.mp4)

Differences: expectations vs. act out: 
- Users might be confused and rather ask the question back when prompted with "Let's set your focus for today!" For example, the user in the act out exercise asked "what *is* my focus?," whereas I expected them to be silent and wait for the next line from the device.
  - Users might be confused why they're being ask this question depending on what time of day it is or what they were in the middle of doing
- When asked what their tasks for the day were, the user said something entirely vague (i.e. "doing work") rather than state too many tasks planned which was what I had initially assumed. I realized that users could not have any tasks to do a given day as well. This alternative dialogue path should be added
- User knew that it was the end of the dialogue when the device said "I'll check back in 45 minutes," so this was a good enough signal. However, the user stated afterwards they were confused about the purpose of checking back ( "is the device checking back to see how much I finished? or ...?"
- Users might want more time to work on a task when the device "checks back." An alternative dialogue path on checking back and a case in which the user wants to continue working on a task could be added. 
- There was some confusion with pauses (generally 5-10 seconds in between each question)
- Regarding the tone of the voice, depending on the user, they might find the tone not as encouraging to set intentions/focus for the day but rather be intimidated.

Suggestions and possible improvements from dialogue act out:
- Interaction initiation could be designed to be more smooth or personable to reduce confusion. Or I could also keep it as is because the user was quickly able to figure out from the next question what they were being asked.
- Ask more general questions about their plan for the day and ask about tasks if they seem to be "busy."
- Adjust pauses in between questions depending on expected answers, or add active listening cues through other sensors to show they device is listening.
- (Could be beyond the scope of this lab) Anticipate some tasks they could do (smart recommendation or not) in the mean time if the user is unsure what to do. For example, if there is too long of a pause or the user says "I'm not sure where to start," the device could say "Not sure where to start? Here are some things you’ve been working on, or X, Y, Z outstanding tasks"
- More input that the user can provide at the point of "task check in:" "what percentage of the task did you finish?" Depending on this input, the device could ask if the user wants to move on to another task or try to finish the incomplete task for another round of x minutes.


<!-- \*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\* -->

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

<!-- \*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\* -->

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
    - *Predict input timing* to preempt dialogue timing and code device dialogue instead of using additional signals that could add more room for error
    - *Anticipate misunderstandings and pauses* to reduce anxiety of the user to immediately answer and provide input (for example, for more complex questions that the device wants an answer for, the device could ask the question, pause for a short time period, and then say "It's okay, take your time to give a more thoughtful answer" 
    - *Adapt wording* to the stylistic conversation to the user (probably too complex for the scope of this lab, but important consideration for users' diverse cultural backgrounds with varied vernacular behaviors


3. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
    - Visual interaction: some type of visual signals (lighting, text, image, etc.) to show the status and accuracy of the interaction with the device. For example, lighting to signal that the device will initiate the interaction or that it's listening to the user's speech input; text on screen to show that the device understood the user's input (rather than dialogue "I understand what you mean" or "I got it"
    - Vibration: vibration to signal the status of the device changes, similar to how smartphones vibrate with a new message (i.e. vibrate when the device is ready to speak)



3. Make a new storyboard, diagram and/or script based on these reflections.

![storyboard_v2](https://github.com/hjkim63/Interactive-Lab-Hub/blob/e59ec3ab93507d89720890d49d3061aa40a081f8/Lab%203/focus_storyboard_2.png)


## Prototype your system

The system includes:
- the Raspberry Pi
- accelerometer
- Webcam as the mic (voice intereaction)
- Adafruit RGB display as the screen (visual interaction --for future variations)

### How the system works
- The speakers are costumed in a personafied box with name of the device and a facial expression.
- The device initiates the dialogue when the device notices a vibration --signaling the user has sat down at a desk, moved around some objects, and ultimately is present in front of the device.
- The device "speaks" to the user through the controller with pre-assumed pause intervals 

<!-- The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it.  -->
*Below are screencaptures of the system set up and device costumed:*
<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%203/device_costume.PNG" width=50% height=50%>


<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%203/system_prototype.JPG" width=50% height=50%>

<!-- ![costume](https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%203/device_costume.PNG) -->
<!-- ![system set up](https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%203/system_prototype.JPG) -->
<!-- *Document how the system works* -->

*Below is a demo video and screencapture of the accelerometer data collected:* ![demo_vid](https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%203/demo_vid.mp4)

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%203/demo_screen.png" width=50% height=50%>
<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%203/sensor_accelormeter_data.png" width=50% height=50%>


## Test the system

I was able to test the device interaction with two people (not from the IDD lab) and below were my reflections from testing the system. It was, as expected, a bit hard to hide the fact that the prototype was being wizarded, but I did not explicitly tell the test participants beforehand.
<!-- Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.) -->

<!-- Answer the following: -->

### What worked well about the system and what didn't?

<!-- \*\**your answer here*\*\* -->
- Initial speech of the dialogue was easy and worked well
- Designing the timing and intonations of conversations depending on the input from the user was difficult. Especially the pre-assumed pause intervals  didn't work out so well when the use rambled or took their time to think. The user could think that the device cut them off.

### What worked well about the controller and what didn't?

<!-- \*\**your answer here*\*\* -->
- The controller wasn't as useful in controlling for pauses in between the dialogue which made it difficult for the device to carry out/lead the conversation and engage the user.
- Having the different sensors line up (text on screen to line up with the speech from device --not documented in this report) and the accelerometer  was too sentitive that it would need to start the conversation multiple times if changes in the vigration 

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

<!-- \*\**your answer here*\*\* -->
- Other sensors could be more effectively used to show the status of the device to the user as they would when conversing with a person. For example a blinking light could reflect "nodding" that the device is listening and understanding. 
- Various sensors can also be used to understand the state of the world, so 1) choosing sensors that are less prone to errors and 2) having multiple sensors for inputing data to the device (i.e. in addition to speech to "say" a piece of information for input, having a button or keyboard, or camera) so there are alternative ways of input.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

<!-- \*\**your answer here*\*\* -->
- This system could create a rich dataset of the different tasks the users set out to do, which they perceive to be "priorities," and their behaviors around completing these tasks to possibly predict and encourage more productive and healthy task completion habits.
- The device could make use of different sensing modalities like motion to see if and how the user is focusing on their task, and using either sound/voice or even visual (computer vision models to detect facial expressions) to understand how the user is feeling.
