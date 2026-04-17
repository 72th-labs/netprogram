import socket
import time

DEVICE1_HOST = '127.0.0.1'
DEVICE1_PORT = 5001
DEVICE2_HOST = '127.0.0.1'
DEVICE2_PORT = 5002

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.connect((DEVICE1_HOST, DEVICE1_PORT))
print("Connected to Device 1")

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.connect((DEVICE2_HOST, DEVICE2_PORT))
print("Connected to Device 2")

with open('data.txt', 'a') as f:
    while True:
        user_input = input("\nInput (1 / 2 / quit): ").strip()

        if user_input == '1':
            sock1.send('Request'.encode())
            response  = sock1.recv(1024).decode()
            timestamp = time.strftime("%a %b %d %H:%M:%S %Y")
            line      = f"{timestamp}: Device1: {response}\n"
            print(line, end='')
            f.write(line)
            f.flush()

        elif user_input == '2':
            sock2.send('Request'.encode())
            response  = sock2.recv(1024).decode()
            timestamp = time.strftime("%a %b %d %H:%M:%S %Y")
            line      = f"{timestamp}: Device2: {response}\n"
            print(line, end='')
            f.write(line)
            f.flush()

        elif user_input == 'quit':
            sock1.send('quit'.encode())
            sock2.send('quit'.encode())
            print("Sent quit to both devices. Terminating.")
            break

        else:
            print("Invalid input. Enter 1, 2, or quit.")

sock1.close()
sock2.close()