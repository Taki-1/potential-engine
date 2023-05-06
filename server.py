# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 6969))
# s.listen(5)

# while True:
#     clientsocket, address = s.accept()
#     print(f"Connection from {address} has been established!")
#     clientsocket.send(bytes("Welcome to the server!", "utf-8"))

import socket
import threading

HEADER = 64
disconnect_message = "!Disconnect"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)

s.bind((ipaddr, 2310))
s.listen(5)
print(f"Your ip&port: {ipaddr}:2310")


def handle_client(conn, address):
    print(f"[New Connection:] {address}")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode("utf-8")
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode("utf-8")
            if msg == disconnect_message:
                connected = False
            print(f"[{address}] {msg}")

    conn.close


while True:
    clientsocket, address = s.accept()
    print(f"Connection established from {address}")
    clientsocket.send(bytes("Connection Successful!", "utf-8"))
    thread = threading.Thread(target=handle_client, args=(clientsocket, address))
    thread.start()
    print(f"[Active Connections] {threading.activeCount() - 1}")
