import socket
import random

HOST = '0.0.0.0'
PORT = 5001

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind((HOST, PORT))
server_sock.listen(1)
print(f"Device 1 listening on port {PORT}...")

conn, addr = server_sock.accept()
print(f"Connected from {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    msg = data.strip()

    if msg == 'Request':
        temp  = random.randint(0, 40)
        humid = random.randint(0, 100)
        illum = random.randint(70, 150)
        response = f"Temp={temp}, Humid={humid}, Illum={illum}"
        conn.send(response.encode())
        print(f"Sent: {response}")

    elif msg == 'quit':
        print("Received quit. Closing Device 1.")
        break

conn.close()
server_sock.close()