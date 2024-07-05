import socket

HOST = 'server'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}")

    counter = int(s.recv(1024).decode())
    while counter < 10:
        print(f"Server sent: {counter}")
        counter += 1
        s.sendall(str(counter).encode())
        print(f"Client Sent Number: {counter}")
        counter = int(s.recv(1024).decode())


