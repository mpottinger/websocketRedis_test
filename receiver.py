# send POST request with jpg from opencv webcam image to http server,
# and then a GET request to the same server to get the image to display

import requests
import sys
import cv2
import numpy as np
import base64

url = "http://34.106.72.196:80/dw1"
#url = "http://localhost:8000/dw1"

while True:
    # send GET request to the server, receiving binary data
    r = requests.get(url)
    print("content type:", r.headers['Content-Type'])
    # convert binary data to numpy array
    img = np.frombuffer(r.content, dtype=np.uint8)
    #print(r.content)
    #print("Received content of size:", len(r.content))
    #print("np frombuffer shape: ", img.shape)
    # decode numpy array to opencv image
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    # display image
    cv2.imshow('image', img)
    # wait for key press
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


