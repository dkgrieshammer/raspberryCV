from picamera.array import PiRGBArray
from picamera import PiCamera
from numpy import interp
import time
import cv2

from ServoControl import servoControl

myres = [320,240]

camera = PiCamera()
camera.resolution = (myres[0],myres[1])
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(myres[0],myres[1]))
#load cascade file / haar(harharharr)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
time.sleep(0.1) #wait for camera to start
try:
    servo = servoControl()
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            lastSize = 0
            bigFacePos = 0
            image = frame.array
            image = cv2.flip(image,1)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.2, 5)
            #draw a rect around every face
            for(x,y,w,h) in faces:
                cv2.rectangle(image, (x,y),(x+w, y+h), (255,255,0),2)
                if w > lastSize:
                    lastSize = w
                    bigFacePos = x+(w/2)
    ##            roi_gray = gray[y:y+h, x:x+w]
    ##            roi_color = image[y:y+h, x:x+w]
                
    ##            eyes = eye_cascade.detectMultiScale(roi_gray)
    ##            for(ex,ey,ew,eh) in eyes:
    ##                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            if lastSize != 0:
                print(bigFacePos)
                fPos = interp(bigFacePos,[0,360],[1200,1800])
                fPos = round(fPos,0)
                servo.setPos(fPos)
            cv2.imshow("Frame", image)
            key = cv2.waitKey(1) & 0xFF
            
            rawCapture.truncate(0)
            
            if key == ord("q"):
                break
except:
    print("error")

finally:
    servo.kill()
