import logging
import os
from flask import Flask
from flask_ask import Ask, request, session, question, statement
from subprocess import Popen
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)
 
STATUSON = ["join","start","on", "switch on", "enable", "power on", "activate", "turn on"] # all values that are defined as synonyms in type
STATUSOFF = ["end","off", "switch off", "disactivate", "turn off", "disable", "turn off"]
 
@ask.launch
def launch():
    speech_text = 'Welcome to the Raspberry Pi alexa automation.'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)
 
@ask.intent('LightIntent', mapping = {'status':'status'})
def Gpio_Intent(status,room):
    if status in STATUSON:
        p1 = Popen(["chromium-browser",'http://meet.jit.si/mirror_per_mai'])
        return statement('Joining meeting in ten seconds')
    elif status in STATUSOFF:
        os.system("killall chromium-browse")
        return statement('Ending meeting')
    else:
        return statement('Sorry, this command is not possible.')
 
@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)
 
 
@ask.session_ended
def session_ended():
    return "{}", 200
 
 
if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(port=6000,debug=True)
