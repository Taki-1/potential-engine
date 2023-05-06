import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname(socket.gethostname())
port = 1020
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MSG = "exit0"

s.bind((ip,port))

print(f"SERVER STARTED AT {ip}:{port}")

def handle_client(conn, addr):

    print(f"[NEW CONNECTION] {addr}")

    conn.send(bytes("[!CONNECTION SUCCESS!]", FORMAT))

    
    connected = True
    while connected:
        msg_byte = int(conn.recv(HEADER).decode(FORMAT))
        if(msg_byte):
            msg = conn.recv(msg_byte).decode(FORMAT)
            if(msg == DISCONNECT_MSG):
                connected = False
            print(f"[{addr}] {msg}")

    conn.close()

def start():
    s.listen(5)
    while True:
        connO, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(connO, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")


if __name__ == "__main__":
    start()