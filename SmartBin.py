# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:16:23 2021

@author: Neel
"""

import io
import os
from time import sleep
import serial
import cv2


def detect(img):
    from google.cloud import vision
    
    client = vision.ImageAnnotatorClient()
    file_name = os.path.abspath(img)
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels


transmitVar = "0"
ser = serial.Serial('COM5', 9600)
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('output.jpg', frame)
        labels = detect('output.jpg')
        for label in labels:
            print(label.description)
            if label.description == "Food" or label.description == "Plastic" or label.description == "Junk food":
                transmitVar = "1"
                break
            elif label.description == "Drinkware" or label.description == "Wood":
                transmitVar = "2"
                break
        break

print(transmitVar)
ser.write(bytes(transmitVar, 'utf-8'))
cap.release()
cv2.destroyAllWindows()
sleep(3)
ser.write(bytes("0", 'utf-8'))
ser.close()
