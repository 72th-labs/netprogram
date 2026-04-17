import socket
import random

HOST = '0.0.0.0'
PORT = 5002

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind((HOST, PORT))
server_sock.listen(1)
print(f"Device 2 listening on port {PORT}...")

conn, addr = server_sock.accept()
print(f"Connected from {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    msg = data.strip()

    if msg == 'Request':
        heartbeat = random.randint(40, 140)
        steps     = random.randint(2000, 6000)
        cal       = random.randint(1000, 4000)
        response  = f"Heartbeat={heartbeat}, Steps={steps}, Cal={cal}"
        conn.send(response.encode())
        print(f"Sent: {response}")

    elif msg == 'quit':
        print("Received quit. Closing Device 2.")
        break

conn.close()
server_sock.close()