#hh
import numpy as np
import cv2
import pickle
import sys
from flask import Flask, render_template, Response,request
import time
import threading
import requests
from mail import *
app = Flask(__name__)
sys.path.append("..")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
fullbody = cv2.CascadeClassifier("fullbody_recognition_model.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face-trainer.yml")
email_update_interval = 30
url = 'http://192.168.1.101:5000/doorstatus' #OPEN or CLOSE or _
frame=0
last_epoch = 0
doorval="OPEN"
labels = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)
def check_for_objects(): 
	global last_epoch
	global frame
	global name
	global email_update_interval
	name=""
	while(True):
		ret, frame = cap.read()
		gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		doorstat=requests.get(url)
		if(doorstat.content.decode('utf-8')=="OPEN"):
			faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
			name=""
			for (x, y, w, h) in faces:
				roi_gray = gray[y:y+h, x:x+w]
				roi_color = frame[y:y+h, x:x+w]
				id_, conf = recognizer.predict(roi_gray)
				if conf>=4 and conf <= 85:
					name = labels[id_]
					cv2.putText(frame, name, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
				cv2.rectangle(frame,(x,y),(x+w,y+h), (255,0,0), 2)
		else:
			bodies = fullbody.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
			for (x,y,w,h) in bodies:
				cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
			try:
				if len(bodies) and (time.time() - last_epoch) > email_update_interval:
					last_epoch = time.time()
					print ("Sending email...")
					sendEmail(frame)
					print("done!")
			except:
				print("Error sending email: ", sys.exc_info()[0]) 
		cv2.imshow('frame',frame)
		if cv2.waitKey(20) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

def gen():
    while True:
        ret, buffer = cv2.imencode('.jpg', frame)
        try:
            f = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + f + b'\r\n\r\n')
        except:
            print("web error")
@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/name')
def namelabel():
    return name
@app.route('/door',methods=["POST","GET"])
def door():
	global doorval
	if request.method=="POST":
		try:
			doorval=request.form["op"]
		except:
			doorval=request.form["cl"]
		return render_template('door.html',doorval = doorval)
	else:
		return render_template('door.html',doorval = doorval)
@app.route('/doorstatus')
def doorstatus():
	global doorval
	return doorval
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
	t = threading.Thread(target=check_for_objects, args=())
	t.daemon = True
	t.start()
	app.run(host='0.0.0.0', debug=False)