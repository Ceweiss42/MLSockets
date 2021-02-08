import socket
import pickle
import cv2
import time as t
from tensorflow.keras.models import load_model



model = load_model(r"C:\Users\cewei\Desktop\model.h5")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("#############", 6969))
data = b""

while True:
    packet = s.recv(4096)
    if len(packet) <= 0: break
    data += packet
    
p = pickle.loads(data)
turn = model.predict(p)
t = turn[0][0]
print(t)
s.send(bytes("hello", "utf-8"))


   

