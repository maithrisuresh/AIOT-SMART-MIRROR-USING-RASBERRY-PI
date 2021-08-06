# AIOT-SMART-MIRROR-USING-RASBERRY-PI
#Final year project at NMAMIT by Maithri Megha Kavya

The project proposes a system to act as a smart mirror that displays the date, time, weather update , news , calendar events that can be collected from the internet and displayed in that smart mirror. The smart mirror provides a near effortless experience that allow the user to just walk up and be greeted with information they would typically need another device to make.. The data is retrieved from the web through the Wi-Fi connectivity and is displayed on the smart mirror. Through facial recognition smart mirror can identify the user. Mirror provides Amazon Alexa Voice Service to interact with user. User can just ask alexa “ Ask Mirror to Start meeting “ and can join the Jitsi meet video Conferencing call with friends and family .
Our smart mirror can be connected to a camera near the door . Whenever the door is locked the smart mirror will be active . If at all the camera catches a person , smart mirror  checks if it knows the person else it will send an email  to the owner . In this project door lock is implemented using a website created using Flask.

SOFTWARE REQUIREMENTS:

•	OpenCV: OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. This software is mostly used for image processing and video analysis. With the help of this programming the computer processes and ultimately understands images and videos. 
•	Raspbian OS: Raspbian is a free operating system optimized for the Raspberry Pi hardware. Raspbian comes with over 35,000 packages, pre-defined functions which helps in easy installation on a Raspberry Pi computer. 
•	Python: Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax makes it an ideal language for scripting and rapid application development in many areas on most platforms.

HARDWARE REQUIREMENTS:

•	Raspberry Pi: A Raspberry Pi is a credit card-sized computer originally designed for education, inspired by the 1981 BBC Micro. Creator Eben Upton's goal was to create a low-cost device that would improve programming skills and hardware understanding at the pre-university level. But thanks to its small size and accessible price, it was quickly adopted by tinkerers, makers, and electronics enthusiasts for projects that require more than a basic microcontroller.
•	Speaker: Speaker is required to provide voice output.
•	Webcam: A webcam in this project is used to recognize user’s face and display tweets. Any type of webcam is compatible with Raspberry Pi.
•	Mirror: A special mirror known as a two way mirror or observation mirror is used in this project. Unlike a household mirror, the two way mirror is not painted with an opaque colour on the back, instead its left untouched. This gives the property of the mirror being reflective one side and transparent/translucent from the other.
•	Microphone: Microphone is required to provide voice input.
•	Mouse: Mouse is used to navigate.
•	Keyboard: Keyboard is used to give the input.


AMAZON ALEXA

We can set up the Alexa Voice Service (AVS) Device SDK on a Raspberry Pi with a script. Utilizing the Alexa Voice Service gives you the ability to do numerous different things such 
as unit conversions and checking sports scores just by using your voice. Following are the steps
1. Register an AVS device with the Amazon developer portal.
2. Install and configure AVS Device SDK dependencies on your  Raspberry Pi.
3. Build the AVS sample app and run it on your Raspberry Pi.
 
 
 JITSI MEET VIDEO CONFERENCING 

With our smart mirror video conferencing with friends and family is possible . Jitsi Meet is a part of Jitsi, which is a collection of open-source voice, video conferencing, and instant messaging services.The Jitsi Meet allows you to host group video calls, i.e. video conferencing in seconds. You don’t even need an account with them . Users can conduct or join a meeting from the web version without creating an account. There is no requirement or compulsion to download the application version of Jitsi Meet. This makes it easy to conduct multiple meetings in a day and manage the data for every session.User can just ask alexa “ Ask Mirror to Start meeting “ and can join the Jitsi meet video Conferencing call with friends and family . Ngrok was used for forwarding video conferencing adresss to raspberry pi 


FACE RECOGNITION

OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. [5]This software is mostly used for image processing and video analysis. With the help of this programming the computer processes and ultimately understands images and videos. We used OpenCV for recognising the face of the user .
First we need to train the LBPHFaceRecognizer model . We keep all the labelled images of the user ready in a folder and then train the model . After training recogniser can be used to sucessfully detect the faces. Name of the face detected is also displayed in https:192.168.43.173:5000/name for future use .


THIEF DETECTION

We can make use of smart mirror to send an email whenever camera captures the unknown person when a door is locked . We just implemented the idea. Using raspberry pi’s Localhost http://192.168.43.173:5000/door we created a page using Flask where a user can open or close the door.
When the door is open the email wont be sent .When the door is closed if at all the raspberry pi camera captures the unknown person an email will be quickly sent to user . Smart mirror camera will be very active when door is closed . 
In real world a switch and a camera can be placed in the door . This camera is connected to smart mirror . When door is locked switch is turned on , if at all any unknown person is detected an email will be sent using OpenCV library .








