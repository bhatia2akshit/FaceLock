import cv2,os

import numpy as np

from PIL import Image

import storeDictionary as save

#while True:

def checkFace():

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    try:

        recognizer.read('./trainer/trainer1.yml')

    except:
        return

    cascadePath = "./Classifiers/face.xml"

    faceCascade = cv2.CascadeClassifier(cascadePath);

    cam = cv2.VideoCapture(0)

    # font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) #Creates a font

    font = cv2.FONT_HERSHEY_SIMPLEX

    i = 0

    while(i<20):

        ret, im =cam.read()

        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        faces=faceCascade.detectMultiScale(im,scaleFactor=1.2, minNeighbors=2, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)

        #print faces
        for(x,y,w,h) in faces:

            cv2.putText(im, str(w), (x, y + h), font, 1, (255, 255, 255),

                        3)  # Draw the text

            if(w>200 and w<450):

                count=0

                cv2.putText(im, str('smile for camera'), (x + 100, y + h), font, 1, (255, 255, 255),

                            3)

                while(count<3000):

                    count+=1;

                nbr_predicted, conf = recognizer.predict(gray[y:y + h, x:x + w])
                print nbr_predicted, " employee code"
                cv2.rectangle(im, (x - 50, y - 50), (x + w + 50, y + h + 50), (225, 0, 0), 2)

                cv2.imshow('im', im)
                print str(conf)+" confidence"

                #cv2.putText(im, str(nbr_predicted) + "--" + str(conf), (x, y + h), font, 1, (255, 255, 255),3)  # Draw the text

                cv2.waitKey(1000)
                cam.release()
                cv2.destroyAllWindows()
                if(conf<=40):

                    return False

                else:

                    return True



