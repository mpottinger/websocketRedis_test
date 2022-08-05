# send POST request with jpg from opencv webcam image to http server,
# and then a GET request to the same server to get the image to display

import requests
import sys
import cv2
import numpy as np
import base64

#url = "http://34.106.72.196:80/dw1"
url = "http://localhost:8000/dw1"
headers = {'Wait': 'true', 'Delete': 'true', 'Timeout': '10000'}
s = requests.Session()
while True:
    # send POP request to the server, receiving binary data and deleting it from the server
    # the video sender will only upload the data if the key is not found on the server, saving bandwidth
    # "Wait" header is set to true, and the server will wait for the data to be uploaded before sending the next request
    # "Delete header is set to true, and the server will delete the data after it is downloaded
    r = s.get(url, headers=headers)
    # check if server response was successful
    if r.status_code == 200:
        #print("content type:", r.headers['Content-Type'])
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
    else:
        pass
        #print("server returned:", r.status_code)


