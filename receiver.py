# send POST request with jpg from opencv webcam image to http server,
# and then a GET request to the same server to get the image to display
import time

import sys
import cv2
import numpy as np
import base64
import websocket
import json

class ClientRequest:
    def __init__(self, method, timeout, key, size):
        self.method = method
        self.timeout = timeout
        self.key = key
        self.size = size

#url = "ws://34.106.72.196:80/dw1"
url = "ws://localhost:8000/dw1"
s = websocket.WebSocket()
frame_count = 1
start = time.time()
# connect to websocket server
s.connect(url)
while True:
    # read message from websocket server
    msg = "CLIENT"
    req = ClientRequest("GET", 10, "image", len(msg))
    req = json.dumps(req.__dict__)
    s.send(req + msg,websocket.ABNF.OPCODE_BINARY)
    msg = s.recv()
    #print(len(msg))
    #print(msg)
    if(msg == b"TIMEOUT" or msg == b"timeout"):
        print("TIMEOUT")
    else:
        # convert message to numpy array (bytes)
        img = np.frombuffer(msg, dtype=np.uint8)
        # # convert numpy array to opencv image
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        # # display image
        try:
            cv2.imshow('image', img)
        except:
            print("error")
        # # press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break
        # # print frame count and time per frame
        frame_count += 1




