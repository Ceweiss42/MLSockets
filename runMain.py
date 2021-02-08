import cv2
import numpy as np
from tensorflow.keras.models import load_model
from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
import os
from datetime import datetime
import time
import pickle
import test as t

import socket

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("", 6969))
s.listen(5)


cap = cv2.VideoCapture(-1)

SCREEN_WIDTH = 240
SCREEN_HIGHT = 120
cap.set(3,SCREEN_WIDTH)
cap.set(4,SCREEN_HIGHT)

#######################################
model = load_model('/home/pi/Desktop/model.h5')
######################################

bw = back_wheels.Back_Wheels()
fw = front_wheels.Front_Wheels()
picar.setup()
run = True

fw.offset = 0

bw.speed = 0
fw.turn(90)

def preProcess(img):
    img = img[54:120, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img



while True:
    clientsocket, address = s.accept()
    print(f"Hello There, {address}")
    cap = t.getImg(False, size=[240, 120])
    cap = np.asarray(cap)
    cap = preProcess(cap)
    cap = np.array([cap])
    sendbytes = pickle.dumps(cap)
    clientsocket.send(sendbytes)
    clientsocket.close()
    
#     if steering < -0.5:
#         turn = -1
#     elif steering > 0.5:
#         turn = 1
#         
#     else:
#          turn = 0
#     if turn == 0:
#         fw.turn_straight()
#     elif turn == 1:
#         fw.turn_right()
#     else:
#         fw.turn_left()
    cv2.waitKey(1)
    bw.speed = 00
    
