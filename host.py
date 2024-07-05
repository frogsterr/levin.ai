import socket

HOST = '0.0.0.0'
PORT = 65432
counter = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        conn.sendall(str(0).encode())

        while counter < 10:

            client_number = s.recv(1024)
            if not client_number:
                break

            print(f"Client sent {int(client_number.decode())}")
            client_number += 1
            conn.sendall(str(client_number).encode())
        
        
        print("We counted to 10!")




