# send POST request with jpg from opencv webcam image to http server,
# and then a GET request to the same server to get the image to display

import requests
import sys
import cv2
import numpy as np
import base64

#url = "http://75.152.195.28:8000/dw1"
url = "http://localhost:8000/dw1"

while True:
    # send GET request to the server
    r = requests.get(url)
    # decode Base64 text to image
    #jpeg_decoded = base64.b64decode(r.text)
    jpeg_decoded = r.content
    # add html image tag to the decoded text
    # convert image to numpy array
    jpeg_decoded = np.frombuffer(jpeg_decoded, dtype=np.uint8)
    # convert numpy array to image
    jpeg_decoded = cv2.imdecode(jpeg_decoded, cv2.IMREAD_COLOR)
    # display image
    cv2.imshow('frame', jpeg_decoded)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



