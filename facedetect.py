from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
import imutils
import numpy as np
import pygame
from time import sleep
import os
L=2

time.sleep(15)

# Get user supplied values
cascPath = sys.argv[1]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)






# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (480, 320)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(480, 320))




# allow the camera to warmup
time.sleep(0.1)
lastTime = time.time()*1000.0


#Sets the person as not being in frame
User_first=2
L=2
T=0
e=0



# capture frames from the camera

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    #Sets the face as first being Recognized
    if User_first == 2 and len(faces) == 1:
	User_first=1
        print("Face Recognized")
	pygame.mixer.init()
	pygame.mixer.music.load("slow-spring-board.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
    	    continue
    # show the frame
    cv2.imshow("Frame", image)


    if User_first == 0 and len(faces) == 1:
        print("Face Found")
        User_first=1

    # show the frame
    cv2.imshow("Frame", image)


    if User_first == 1 and len(faces) == 1:
        print("Looking at the road")
        L=0


    # show the frame
    cv2.imshow("Frame", image)


    if User_first == 1 and len(faces) == 0:
        cv2.imshow("Frame", image)

    	cv2.imshow("Frame", image)
    	time.sleep(2)
    	cv2.imshow("Frame", image)

	if User_first == 1 and len(faces) == 0:
		User_first=0
        	print("Face Lost")
		pygame.mixer.init()
		pygame.mixer.music.load("open-ended.mp3")
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
    		    continue


    # show the frame
    cv2.imshow("Frame", image)


    if User_first == 0 and len(faces) == 0:
        print("Face Not Found, Please Look at road:" + str(L))

	pygame.mixer.init()
	pygame.mixer.music.load("to-the-point.mp3")
	pygame.mixer.music.play()
        L=L+1
	while pygame.mixer.music.get_busy() == True:
    	    continue


    if L>5:
        os.system('python Sendemail.py')


    if L>2:
        T=T+1


    if T>4:
        os.system('python Sendemail.py')
        T=0

    # show the frame
    cv2.imshow("Frame", image)




    # Draw a rectangle around the faces
    for (x,y,w,h) in faces:
        img1=cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]


    # show the frame
    cv2.imshow("Frame", image)



    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
	camera.stop_preview()


cv2.destroyAllWindows()
