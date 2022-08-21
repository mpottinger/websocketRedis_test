# send POST request with jpg from opencv webcam image converted to Base64 text to http server,
# and then a GET request to the same server to get the image to display
import time

import websocket
import sys
import cv2
import numpy as np
import json

#url = "ws://34.106.72.196:80/dw1"
url = "ws://localhost:8000/dw1"

# initialize video capture
cap = cv2.VideoCapture(0)

# web socket with binary data enabled.
s = websocket.WebSocket(skip_utf8_validation=True)
# connect to websocket server
s.connect(url)

# this C# class is defined on the server, here we implement the same class
#public record ClientRequest
#    {
#        // structured almost like a http request
#        public string Method { get; set; }
#        public int Timeout { get; set; }
#        public string Key { get; set; }
#        public int Size { get; set; }
#    }

class ClientRequest:
    def __init__(self, method, timeout, key, size):
        self.method = method
        self.timeout = timeout
        self.key = key
        self.size = size

while True:
    # read image from webcam, set resolution to 640x480
    ret, frame = cap.read()
    # convert image to jpeg format
    img = cv2.imencode('.jpg', frame)[1]
    # convert jpeg image to raw byte array
    img = img.tobytes()
    # create ClientRequest object
    req = ClientRequest("PUT", 10, "image", len(img))
    # convert ClientRequest object to json text
    req = json.dumps(req.__dict__)
    req_bytes = bytes(req, 'utf-8')
    # concatenate json text and jpeg image
    msg = req_bytes + img
    # send message to websocket server OPCODE_BINARY
    s.send(msg, websocket.ABNF.OPCODE_BINARY)


    # s.send("test")
    # check if message says timeout
    msg = s.recv()
    print(msg)
    if msg == "timeout":
        print("timeout")



