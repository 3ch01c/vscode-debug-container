import sys
print(f'Your Python version is {sys.version}')

import os
#print(f'Your environment variables are {os.environ.items()}')
print(f'Your environment variables are {os.environ}')

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
HOST = s.getsockname()[0]
PORT = 54321
print(f'Your IP address is {HOST}')
s.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Accepting connections on port {PORT}')
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
