# Observant Systems

<!-- **NAMES OF COLLABORATORS HERE** -->


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

## Prep

1. Spend about 10 Minutes doing the Listening exercise as described in [ListeningExercise.md](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2022/Lab%205/ListeningExercise.md)
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2022/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:
1. Pull the new Github Repo.(Please wait until thursday morning. There are still some incompatabilities to make the assignment work.)
1. Raspberry Pi
1. Webcam 

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show the filledout answers for the Contextual Interaction Design Tool.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

The following command is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

#### A.1 contours-detection
- Benefit/key application: any application of detecting surfaces or varied sizes/area or brightness might be useful
  - potential design: 1) detecting walls or surface areas for painting (interior design), 2) detecting changes in surface areas in medical images (disease detection)

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/contour_demo_1.png"  width=50% height=50% >
<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/contour_demo_2_.png"  width=50% height=50% >
<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/contour_demo_3.png"  width=50% height=50% >


#### A.2. face-detection
- Benefit/key application: applications for this algorithm could be at the individual level (detecting the face and features within) as well as scale up to detect and count many faces
  - potential design: 1) face recognition (learned algorithm from simple face detection) for access to phone, house, etc. 2) classification of photos in photo album (automated tagging after learned model), 3) class attendance, 4) room capacity check through face detection

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/face_detection_1.png"  width=50% height=50% >


#### A.3. flow-detection
- Benefit/key application: key benefit of this algorithm is movement, so any application where detection of movement, speed, and direction would be useful
  - potential design: 1) movement in cars on highway or pedestrians on walkway, 2) movement of machines/robotic devices in factory settings
- Issue: Extremely slow latency

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/opticalflow_demo_1.png"  width=50% height=50% >


#### A.4.object-detection
- Benefit/key application: any application of detecting objects from a consistent angle would be useful
  - potential design: 1) inventory management in warehouses or even on storefront shelves, 2) object detection for accessible tech devices, 3) detecting obstacles in walkway or autonomous vehicles (but movement might be critical here!) 
- Issue: 
  - overlapping objects or high quantity of objects might be more difficult to detect and discern
  - Objects further away might not be as effective (the model on the Raspberry Pi couldn't detect objects beyond the window across the street --as seen below)
  - Objects couldn't be accurately detected when the webcam angle was moving around quickly

[demo_vid]!(https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/objectdetection_demo_vid.mov)

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/obgdetection_demo_1.png"  width=50% height=50% >
<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/objdetection_demo_2_fail.png"  width=50% height=50% >




#### Filtering, FFTs, and Time Series data. 
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU or Microphone data stream could create a simple activity classifier between walking, running, and standing.

To get the microphone working we need to install two libraries. `PyAudio` to get the data from the microphone, `sciPy` to make data analysis easy, and the `numpy-ringbuffer` to keep track of the last ~1 second of audio. 
Pyaudio needs to be installed with the following comand:
``sudo apt install python3-pyaudio``
SciPy is installed with 
``sudo apt install python3-scipy`` 

Lastly we need numpy-ringbuffer, to make continues data anlysis easier.
``pip install numpy-ringbuffer``

Now try the audio processing example:
* Find what ID the micrpohone has with `python ListAvalibleAudioDevices.py`
    Look for a device name that includes `USB` in the name: USB Audio (hw: 1,0) 1,2
* Adjust the variable `DEVICE_INDEX` in the `ExampleAudioFFT.py` file.
    See if you are getting results printed out from the microphone. Try to understand how the code works.
    Then run the file by typing `python ExampleAudioFFT.py`



Using the microphone, try one of the following: 

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up a running averaging** Can you set up a running average over one of the variables that are being calculated.[moving average](https://en.wikipedia.org/wiki/Moving_average)

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

For technical references:

* Volume Calculation with [RootMeanSqare](https://en.wikipedia.org/wiki/Root_mean_square)
* [RingBuffer](https://en.wikipedia.org/wiki/Circular_buffer)
* [Frequency Analysis](https://en.wikipedia.org/wiki/Fast_Fourier_transform)


**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***

#### Setting a threshold

To set a threshold I added the following code in the `ExampleAudioFFT.py` file:
```
                #added threshold detection#
                threshold = False
                threshold_vol = 80
                if volumnneSlow >= threshold_vol: #set threshold
                    threshold = True #set variable for other use once threshold is detected
                    print("Detect volumne above threshold ",threshold_vol, "!")
```

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/audio_threshold_setting.png"  width=50% height=50% >



### (Optional Reading) Introducing Additional Concepts
The following sections ([MediaPipe](#mediapipe) and [Teachable Machines](#teachable-machines)) are included for your own optional learning. **The associated scripts will not work on Fall 2022's Pi Image, so you can move onto part B.** However, you are welcome to try it on your personal computer. If this functionality is desirable for your lab or final project, we can help you get a different image running the last OS and version of python to make the following code work.

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr25
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi3 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

~~\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\*~~

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

~~**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***~~


*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


### Part B
### Construct a simple interaction.

* Pick one of the models you have tried, and experiment with prototyping an interaction.
* This can be as simple as the boat detector showen in a previous lecture from Nikolas Matelaro.
* Try out different interaction outputs and inputs.
* Fill out the ``Contextual Interaction Design Tool`` sheet.[Found here.](ThinkingThroughContextandInteraction.png)

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

#### B.1.Ideation
<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/idea_brainstorming.png"  width=70% height=70% >


#### B.2.Context Interaction Design

Idea description: This device would be placed at the entrance, hallway, or resting area where employees visit and prompt greetings to spark some interaction in office spaces where remote work has become the norm and there is little to no interaction in office spaces. This device would have a webcam screen that is visible to the employee; when an employee approaches the device, it would detect the employee and display a greeting on the screen that could provide opportunities to break up a quiet, mundane workday. 

__Contextual Interaction__

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/contextual_interaction.png"  width=70% height=70% >

__Interaction sketch__

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/interaction_sketch.jpg"  width=70% height=70% >


#### B.3.Prototpying 

Ideation for experimenting with different inputs and outputs: 
- Input:
  - Input was consistently through the webcam 
  - Various potential inputs & design for next step interactions: 1) voice detection above a certain threshold can be used to detect whether the user sees the screen and seems to be interacting with the device (assuming they try to interact via speech rather than touching the screen), 2) Buttons for inputting the user's mood 

- Output (interaction signal):
  - Simply bounded box around the face/human detected
  - Display a greeting: "Hey there!" or similar greeting on screen
  - Display a question: "How are you doing today?", "How's your mood today?" (and other generic questions or words of encouragement could subsequently displayed assuming/predicting possible responses from the user)
  - Display image that could prompt a further interaction (images of moods or activities on the webcam screen that could jumpstart a conversation)

#### Trial 1.  

First, I assumed I could start with object detection, but this resulted in detecting all the "noise" in a given background that might not be a person. Ultimately I decided not to use object detection, but experimented with display text and images on the screen to signal interaction.
Code for this trial: `greeting_interaction_objdetect.py`

Trial 1.1 objection detection with text output dislayed on screen

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/demo_screenshot_v1(obj%2C%20text).png"  width=50% height=50% >

Trial 1.2 objection detection with text + image display on screen for additional interaction
* Noted that objected detection would pick up on non-human entities, even with a threshold for bounding box and categories (picked up too many objects in the background)
<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/demo_screenshot_v1(obj%2C%20add%20display).png"  width=50% height=50% >

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/demo_screenshot_v1(obj%2C%20too%20many%20objs).png"  width=50% height=50% >

#### Trial 2 

Next, I switched to using the openCV face detection model from Part B to focused on human detection (an employee that might be entering the building or passing a hallway). I implemented code from Trial 1 above to display 1) a bounding box around the detected face, 2) a greeting text on the webcam screen and 3) an image of varied moods to prompt an answer to the greeting shown on the webcam screen.
Code for this trial: `greeting_interaction_facedetect.py`

Trial 2.1. face detection with text + image output dislayed on screen

![trial2_demo_vid](https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/demo_vid_v2.mov)

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/demo_screenshot_v2(face).png"  width=50% height=50% >



### Part C Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
<!-- For example: -->

__screenshot from prototype test__

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/userTest_screenshot_2.png"  width=50% height=50% >

1. When does it what it is supposed to do?
   - The device successfully detects a face approaching the webcam, creates a bounding box around the approaching face, and displays the interaction
   - The interaction successfully was able to spark some notion the users that they were detected (not another object in the background) due to the bounding box around them and prompt some response because there was a quesiton (text + image) displayed once the user was detected.
 
3. When does it fail?
   - The device is not able to accurately detect faces that 1) are further away or cannot detect their eyes, 2) are approaching from different angles or the side of their face is showing
   - The interaction fails when the screen is too low or high so it is not able to detect face of users at different heights and the user needs to crowch down to get in the webcam angle.
   - Although this wasn't in the intial interaction design, it would be a failure if we thought about how this interaction would extend further to subsequent interactions. The question text continues to display on the screen even after a user has responded (either via voice, gesture, trying to touch the webcam screen on the monitor) 

5. When it fails, why does it fail?
   - The user does not notice the device either because it is too far away or they are passing by it too quickly (but as long as they notice the screen and see themselves in it, it sparks some curiosity in the user)
   - In this sense, there might not be enough of an output to signal to the user that they have indirectly given input into the system and prompts further interaction (possible solutions could be audio output or costuming to provide more physical presence)

7. Based on the behavior you have seen, what other scenarios could cause problems?
   - Difference in height across users and the effectiveness of the device to pick up faces of these users
   - If multiple users come into the frame at once, each user might be confused at how to react/interact. (example scenario: if multiple employees are heading back into the office after having lunch together)
   - If the user continues to be in the frame and are waiting for further developments in the interactions but are only met with the same initial interaction (question text + image)


**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
   - User might not know who is prompting this interaction (i.e. "who's greeting me and asking how my day is going? Is it someone in authority? Am I being recorded?"
   - User might not be an employee since this algorithm is simply a face detection model rather than filtering out and only detecting employee faces.
   - User might not be detected even though they are facing toward the camera because of lack of diversity in the training input data (not detecting employees of darker skin color, less distinct facial features, hats or glasses, etc.) 

3. How bad would they be impacted by a miss classification?
   - There wouldn't be any severe consequences from the user (employee) by missclassification but they might feel the interaction is less inclusive or engaging, which it the opposite of the type of interaction that was intended

5. How could change your interactive system to address this?
   - The face detection algorithm would be trained on additional input data to fit the demographics of the company (using employee ID pictures or pictures some company events to crop faces and generate input data in different lighting and angles. This would address the face detection algorithm to be more inclusive

7. Are there optimizations you can try to do on your sense-making algorithm.
   - Regarding the face detection algorithm, we could create a physical space in front of the device so that it signals users to stand directly facing and closely to the device. This might enable input data to be easier to detect. 
   - The computation energy as a whole could be optimized while working around the potential missclassification errors could be to simply change the mode of input to be audio or motion. Compared to face detection which might be more vulnerable to lighting and training data biases, voice or motion detection would be less prone to training data biases and less computation heavy.


<!-- <img src=""  width=50% height=50% > -->

### Part D Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:

* What can you use X for?
  - Individualized interactive experiences for human users --the interaction could be varied but be initiated by a detected face (specific or general)
  - For example, this could be user for interactive greetings in an elevator, library, apartment building entryway, common spaces, etc. 

* What is a good environment for X?
  - Environments where human users are not frequently appearing or noisy backgrounds so face detection is made easier
  - Environments where it might be easier to grab the attention of users or where users have more attention to spare (entry way at office rather than busy museum). This is because the system/device would be stationary and only outputing through visual displays on the screen.
  - Environemnts where users can put a little more effort into getting into the frame of the webcam for face detection
* What is a bad environment for X?
  - Environment where there are many faces (human users) in the webcam frame at once
  - Environment where many users might be passing by quickly (hallway, pathway)

* When will X break? When it breaks how will X break?
  - When/if there are too many faces in the frame at once
  - When frame is changing too quickly (when testing, one user got really excited and was moving side to side to see if the webcam would detect them. this slowed down the system and eventually broke)
  - When if breaks, the webcam screen simply closes out on the phsycaily monitor screen as of now. It would be useful for the user if the system could notify to the user that it is broken and troubleshooting is in process. Even a default image that appears when the system breaks would be a better way to end the interaction than an abrupt window closing.

* What are other properties/behaviors of X?
  - Real-time feedback is a big behavioral component of the system. Thee screen acts as the medium through which the user knows the system is working in real-time.
  - The system could be built out to incorporate many other inputs to not only output visual interactions through the display but also converse with the use through speech or get the user's attention through sound.

* How does X feel?
  - The device might feel highly individualized and engaging because the user's face is being detected and there's an automatic output that asked for more reaction
  - The constant display of the webcam screen, while it provides feedback, could also make users feel like they're being projected on a medium they didn't want to be or question where this footage is shared/stored.

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

<!-- **\*\*\*Include a short video demonstrating the finished result.\*\*\*** -->
![interaction_test_vid](https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/user_test_vido.mp4)

__screenshots from the demo video__ 
- shows the user initially noticing device
- User realized the device was detecting them through the appearance of the bounded box
- User reacted through gesture (assumed user would try to touch the screen or answer via voice)


<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/userTest_screenshot_1.png"  width=50% height=50% >
<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/Lab%205/userTest_screenshot_3.png"  width=50% height=50% >

