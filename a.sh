#!/bin/bash
cd /home/pi/sdk-folder/sdk-build
lxterminal -e "PA_ALSA_PLUGHW=1 ./SampleApp/src/SampleApp ./Integration/AlexaClientSDKConfig.json ../third-party/alexa-rpi/models" 

