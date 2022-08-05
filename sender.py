# send POST request with jpg from opencv webcam image converted to Base64 text to http server,
# and then a GET request to the same server to get the image to display
import time

import urllib3
import sys
import cv2
import numpy as np
import base64

#url = "http://34.106.72.196:80/dw1"
url = "http://localhost:8000/dw1"
content_type = 'image/jpeg'
#content_type = 'application/octet-stream'
# read image from webcam, set resolution to 640x480
cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)
http = urllib3.PoolManager()
while True:
    ret, frame = cap.read()
    # convert image to Base64 text and post to server
    ret, jpeg = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
    #jpeg_text = base64.b64encode(jpeg)
    jpeg_bytes = jpeg.tobytes()
    # send as binary data
    # check if there is unread data on the server, header sent to server will contain 'Exists', and server will return OK if there is unread data
    r = http.request('GET', url, body="", headers={'Exists': 'true'})
    # post the data if key is not found on the server
    if r.status == 404:
        # data wasn't found on the server, post it and print time stamp
        print("sending data at:", time.time())
        r = http.request('POST', url, body=jpeg_bytes, headers={'Content-Type': content_type})
        # print the status code of the response
    print('server returned:', r.status)


