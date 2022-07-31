# send POST request with jpg from opencv webcam image converted to Base64 text to http server,
# and then a GET request to the same server to get the image to display

import requests
import sys
import cv2
import numpy as np
import base64

url = "http://75.155.9.70:8000/dw1"

# read image from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # convert image to Base64 text and post to server
    ret, jpeg = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
    jpeg_text = base64.b64encode(jpeg)
    r = requests.post(url, data=jpeg_text)


