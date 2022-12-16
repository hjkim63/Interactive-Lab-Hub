# Final Project

**Heuisu Kim, Sidarth Wadhwa**

## Ideation
- Urban gardening system (_final idea_)
- Object finder for dementia patients (_fall back plan_)
- Wellness checking interaction
- Forest fire detection

_Sketch 1: Wellness checking interaction_

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/finalProject/ideation1.jpg"  width=70% height=70% >

_Sketch 2: Object finder for dementia patients_
<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/finalProject/ideation_2.jpg"  width=70% height=70% >

_Sketch 3: Urban gardening system_

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/finalProject/ideation_3.jpg"  width=70% height=70% >


**Final Idea: Urban gardening system**

An automated garden maintenance system that looks after shared community gardens by 
1. tracking environmental indicators and 
2. providing personalized, remote care for plants
Main features: 1) temperature, sunlight, humidity, soil moisture content monitoring and 2) remote regulation based on monitored indicators (sprinklers, etc.)

## Pi, the Gardener

### A.Design Exploration

**Context/Problem:** There are numerous community gardens in urban areas for urban landscape, food access & agricultural, and educational purposes. While some gardnes are well kept by volunteers and programs, some are not and it is not always easy to tend them when there are many stakeholders leading to distributed responsibility and lack of expertise. Our device, "Pi, the Gardner" would enable easier involvement and maintenance of community gardens by giving volunteers and stakeholders a smarter signal to take care of and "interact" with the gardens when needed. This reduces the inconvenience of having to walk to the garden that might be out of the way or just even our tendencies to forget after committing to volunteering. The community garden that inspired this idea is  New York City's 91st Street Community Garden and it's volunteer group, [the Garden People](https://www.thegardenpeople.org/). Below are some images of the 91st Street Community Garden and Riverside Park Conservatory.

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/finalProject/setup_environment.png"  width=80% height=80% >


_Exploring interaction design_

**Scenario:** You're an urban dweller, and you're walking down a street in your new neighborhood and come across a community garden. You like the idea of being part of something in the community and contributing and sign up to a mobile app using the QR code on the sign. You think you'll come by the garden to check on the health of the soil, water the plans and so forth, but it's harder than you expected to make the time to simply roam about to the garden without a specific goal in mind. You also realize you don't know what is good temperature for these plants, what defines the range of air humidity for plany survival, or acceptable soil moisture levels. _what if you water the garden and the excessive water ends up killing the plants?_ 

A couple months in, you're feeling that signing up to volunteer was a bad idea or even worse, you've already forgotten about your prior commitment. Just then you get a notification on your mobile phone screen from __Pi, the Gardner__ telling you the soil mositure levels have been below the recommended threshold for seven consecutive days! With a clear problem to solve and direct enough solutions, you plan to walk over to the community garden with buckets of water with a friend the next day. 

The next day, you water the community garden and are able to check on the Pi, the Gardner app that the soil mositure levels have returns to recommended levels. You also see that you can see how the temperature and air humidty levels of the garden have been through the days and months. You realize that with the app, you can "check in" on the garden even from a distance.


Below are images of exploring the interaction design through a Verplank diagram and storyboards. 

_Interaction Diagram_

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/finalProject/design_exploration_3.jpg"  width=80% height=80% >

_Storyboard_

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/finalProject/storyboard.jpg"  width=80% height=80% >


_Detailed ideation: use of sensors, types of input, etc._

When further ideating, 

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/finalProject/design_exploration_1.jpg"  width=50% height=50% >

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/finalProject/design_exploration_2.jpg"  width=80% height=80% >


### B.Technical Implementation

#### B.1.Input: sensors

We used the following 3 sensors, and below is a functional demo video that shows our device set-up along with a demonstration. 
- Soil moisture sensor
- Temperature sensor
- Air humidity sensor

_setup_

https://user-images.githubusercontent.com/89815458/208196591-46710a2f-f334-4c67-b235-c21e23288434.mov

_functional demonstration_
Here we tested the soil moisture levels with something straightforward--just a glass of water--but later tested and demonstrated with a moist banana muffin on the day of the final presentation to mimic the texture and moisture levels of soil.

https://user-images.githubusercontent.com/89815458/208196905-f15e18db-d047-465c-ab3d-1b27ba1f0efc.mov


_Functional check-off feedback:_ The one feedback we had during the check-in was that the sensos are operating separately so that we should have it all within one system. This was implemented for our final version of code.

Furthermore, in our final version, we added in MQTT functionality and the ability to send push notifications to a user's smartphone when certain conditions arise.


_Technical Risks/contingencies:_
- Wifi connections in community gardens
- Diverse-background of users that are connected to this system
- Weather conditions → plan to costume!
- Diverse plant care needs 

#### B.2.Distributed system architecture

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/finalProject/system_arch.png"  width=70% height=70% >

#### B.3. Technical building process

We started off by hooking the sensors up to the Pi and testing their functionality. Since this was done using a breadboard (our sensors did not have the Qwiic connectors found on the sensors that we worked with in class), we had to cross-reference pinout diagrams and iterate over the connections a few times before we were able to actually get the sensors up and running. Once we had confirmed that the sensors were up and running, we moved on to building out the application features. We first worked on combining the two different scripts that we had for the sensors. Once that was done (and after some testing), we incorporated the MQTT and push notifiction aspects into the code in order to make our system more user friendly.

#### B.4. Output: alert signals 

There were two steps to the output: first detecting if we can detect when a criteria is met from the sensor input data, such as if the temperature above the garden has been above 85F or soil moisture level is below 50% for 7 consecutive days. Then we need to publish this message to observing nodes that are subscribed and sends notification to the subscribed devices. This message would be sent to anyone that had set up the "pi the gardener" mobile app.

To mimic this "pi the gardner" mobile app, we used the [Push Safer](https://www.pushsafer.com/) API to send out the messages to any of the garden stakeholders/volunteers.

Here are the codes for connecting to the devices and sending the ping notifications:
<!-- placeholder -->
<!-- * [notifcation.py](https://www.pushsafer.com/)  -->
<!-- * [Here](https://www.pushsafer.com/) -->


### C. Costuming



<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/finalProject/costume_sketch.jpg"  width=80% height=80% >

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/finalProject/costuming.png"  width=80% height=80% >


<!-- <video src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/finalProject/costuming.MOV"> -->


Costumed device in community garden

<img src="https://github.com/hjkim63/Interactive-Lab-Hub/blob/Fall2022/finalProject/device_in_context.JPG"  width=40% height=40% >


<!-- Placeholder for inside images with sensors secured inside with tape <img src=""  width=80% height=80% > -->


### D. Demo video

https://user-images.githubusercontent.com/89815458/208177486-0abdac1d-a52f-4382-bb64-d6c5b3dce1e3.mov


### E. Reflection

Upon delving deeper into the interaction design using the diagram that there are a lot more 

Through this process, we also got to be intimately familiar with what goes into the process of looking after a community garden. With this, came other ideas: a webcam that can keep an eye on the garden and use computeer vision to detect pests/intrusions, an information system that describes a plant and mentions the community member responsible for it, etc. The scope to expand our project in future iterations excites us, and we look forward to the possibility of exploring futher interactions in the future.

<!-- **Timeline**
- 11/21-22: test all sensors in real environment
- 11/29: present prototyped device
- 12/6: costumed device + demo presentation
- 12/16: final reporting 
 -->



**Risks/contingencies**
- Wifi connections in community gardens
- Diverse-background of users that are connected to this system
- Weather conditions → plan to costume!
- Diverse plant care needs 
