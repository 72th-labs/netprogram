from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9000)) 
s.listen(5)

print('계산기 서버가 시작되었습니다. 클라이언트를 대기합니다...')

while True:
    client, addr = s.accept()
    print('Connection from', addr)
    
    while True:
        try:
            data = client.recv(1024)
            if not data: 
                break
            
            expression = data.decode().replace(" ", "")
            result = 0
            
            if '+' in expression:
                a, b = expression.split('+')
                result = int(a) + int(b)
            elif '-' in expression:
                a, b = expression.split('-')
                result = int(a) - int(b)
            elif '*' in expression:
                a, b = expression.split('*')
                result = int(a) * int(b)
            elif '/' in expression:
                a, b = expression.split('/')
                result = round(int(a) / int(b), 1)
            else:
                result = "지원하지 않는 연산입니다."
            
            client.send(str(result).encode())
            
        except Exception as e:
            client.send(b'Error')
            
    client.close()