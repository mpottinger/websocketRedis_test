# send POST request with jpg from opencv webcam image converted to Base64 text to http server,
# and then a GET request to the same server to get the image to display

import requests
import sys
import cv2
import numpy as np
import base64

url = "http://75.152.195.28:8000/dw1"

# read image from webcam, set resolution to 640x480
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    # convert image to Base64 text and post to server
    ret, jpeg = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
    jpeg_text = base64.b64encode(jpeg)
    r = requests.post(url, data=jpeg_text)


