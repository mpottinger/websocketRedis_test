# send POST request with jpg from opencv webcam image converted to Base64 text to http server,
# and then a GET request to the same server to get the image to display
import time

import requests
import sys
import cv2
import numpy as np
import base64

#url = "http://34.106.72.196:80/dw1"
url = "http://localhost:8000/dw1"

content_type = 'image/jpeg'
# header for POST request
# initialize video capture
cap = cv2.VideoCapture(0)
s = requests.Session()

while True:
    # read image from webcam, set resolution to 640x480
    ret, frame = cap.read()
    # convert image to jpeg format
    img = cv2.imencode('.jpg', frame)[1]
    # convert jpeg image to raw byte array
    img = img.tobytes()
    r = s.put(url, data=img, headers={'Content-Type': content_type})

    # check if server response was successful
    print("server returned:", r.status_code, r.text)


