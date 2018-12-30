from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
import imutils
import numpy as np
import pygame


# Get user supplied values
cascPath = sys.argv[1]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)








# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (160, 120)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(160, 120))




# allow the camera to warmup
time.sleep(0.1)
lastTime = time.time()*1000.0


#Sets the person as not being in frame
User_first=0





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


    # Draw a rectangle around the faces
    for (x,y,w,h) in faces:
        img1=cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]


    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

            #The code below plays a sound after a face is found for the first time
    if User_first == 0 and len(faces) == 1:
        User_first=1
        pygame.mixer.init()
        pygame.mixer.music.load("unsure.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        pygame.mixer.init()
        pygame.mixer.music.load("unsure.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    
    #After have chaned User_first to one the program knows that the face has been seen 
    if User_first == 1 and len(faces) == 1:
        print("hi again")

    #the code below says that if the face has been seen before, but it cannot currently be found change the variable
    if User_first == 1 and len(faces) == 0:
        User_first=2
    
    if User_first == 2 and len(faces) == 0:
        while 1:
            faces1 = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE
            )
        for (x,y,w,h) in faces:
            img1=cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]


        # show the frame
            cv2.imshow("Frame", image)
            key = cv2.waitKey(1) & 0xFF
        pygame.mixer.init()
        pygame.mixer.music.load("unsure.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue
        if len(faces1) == 1:
            User_first=1
            continue
 
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
        
cap.release()
cv2.destroyAllWindows()
        

