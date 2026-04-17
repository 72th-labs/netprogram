import socket
import struct
import random

HOST = 'localhost'
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print(f"UDP Server listening on {HOST}:{PORT}...")

while True:
    data, addr = sock.recvfrom(1024)
    msg = data.decode().strip()
    print(f"Received '{msg}' from {addr}")

    temp  = 0
    humid = 0
    lumi  = 0

    if msg == '1':
        temp  = random.randint(1, 50)
    elif msg == '2':
        humid = random.randint(1, 100)
    elif msg == '3':
        lumi  = random.randint(1, 150)

    # 항상 6바이트: 2바이트 정수 3개, 빅엔디언(네트워크 바이트 오더)
    packet = struct.pack('!HHH', temp, humid, lumi)
    sock.sendto(packet, addr)
    print(f"Sent: Temp={temp}, Humid={humid}, Lumi={lumi}")