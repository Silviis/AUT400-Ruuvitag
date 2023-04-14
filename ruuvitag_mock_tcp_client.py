import socket

host = socket.gethostname()
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
battery = 88
while True:
    temp = input("Enter temperature: ")
    msg = "{temp},{battery}".format(temp=temp, battery=battery)
    msg_bytes = bytes(msg, "utf-8")
    s.sendall(msg_bytes)