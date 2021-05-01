# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:16:23 2021

@author: Neel
"""

import io
import os

from google.cloud import vision

client = vision.ImageAnnotatorClient()
file_name = os.path.abspath('efficiency.png')

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)
