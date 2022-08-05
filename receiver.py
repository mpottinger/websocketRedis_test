# send POST request with jpg from opencv webcam image to http server,
# and then a GET request to the same server to get the image to display

import urllib3
import sys
import cv2
import numpy as np
import base64

#url = "http://34.106.72.196:80/dw1"
url = "http://localhost:8000/dw1"

http = urllib3.PoolManager()
while True:
    # send POP request to the server, receiving binary data and deleting it from the server
    # the video sender will only upload the data if the key is not found on the server, saving bandwidth
    # "Wait" header is set to true, and the server will wait for the data to be uploaded before sending the next request
    # "Delete header is set to true, and the server will delete the data after it is downloaded
    r = http.request('GET', url, headers={'Wait': 'true', 'Delete': 'true'})
    # check if server response was successful
    if r.status == 200:
        #print("content type:", r.headers['Content-Type'])
        # convert binary data to numpy array
        img = np.frombuffer(r.data, dtype=np.uint8)
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
    else:
        print("server returned:", r.status)


