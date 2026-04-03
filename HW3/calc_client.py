from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 9000))

while True:

    msg = input('계산식 입력, 종료는 q: ')
    
    if msg == 'q':
        print("계산기 종료.")
        break
        
    s.send(msg.encode())
    
    data = s.recv(1024)
    print('계산 결과:', data.decode())

s.close()