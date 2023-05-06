import socket
import sys

FORMAT = "utf-8"
HEADER = 1024
DISCONNECT_MSG = "exit0"
ipAddr = "192.168.56.1"
port = 1020

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ipAddr, port))
print(s.recv(HEADER).decode(FORMAT))

def send_sms(msg):
    msg_length = str(sys.getsizeof(msg))
    s.send(bytes(msg_length, FORMAT))
    s.send(bytes(msg, FORMAT))


def start_server():
    CONNECTED = True
    while CONNECTED:
        data = input("~/ ")
        send_sms(data)
        if(data == DISCONNECT_MSG):
            CONNECTED = False

if __name__ == "__main__":
    start_server()