import socket
import struct

HOST = 'localhost'
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

requests = ['1', '2', '3']
idx = 0

while True:
    msg = requests[idx % 3]
    idx += 1

    sock.sendto(msg.encode(), (HOST, PORT))

    # 항상 6바이트 수신: 2바이트 정수 3개, 빅엔디언
    data, _ = sock.recvfrom(6)
    temp, humid, lumi = struct.unpack('!HHH', data)

    print(f"Temp={temp}, Humid={humid}, Lumi={lumi}")