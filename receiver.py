# send POST request with jpg from opencv webcam image to http server,
# and then a GET request to the same server to get the image to display

import requests
import sys
import cv2
import numpy as np
import base64

#url = "http://34.106.72.196:80/dw1"
url = "http://localhost:8000/dw1"
s = requests.Session()
while True:
    # send Get request to the server, this will pop an item from the queue of a given key
    # the video sender will only upload the data if the queue is empty for a given key, saving bandwidth
    print("getting data from server.")
    r = s.get(url)
    # check if server response was successful
    print("server returned:", r.status_code)
    if r.status_code == 200:
        # convert binary data to numpy array
        img = np.frombuffer(r.content, dtype=np.uint8)
        # decode numpy array to opencv image
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        # display image
        cv2.imshow('image', img)
        # wait for key press
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
                break


