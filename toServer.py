import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.4.85", 6969))
msg = s.recv(4096)
print(msg.decode("utf-8"))
s.send(bytes("hello", "utf-8"))
