from socket import *
import os

s = socket()
s.bind(('', 80))
s.listen(10)

print("웹 서버 실행 중...")

while True:
    c, addr = s.accept()
    
    data = c.recv(1024)
    if not data:
        c.close()
        continue
        
    msg = data.decode()
    req = msg.split('\r\n')
    
    request_line = req[0]
    try:
        method, path, version = request_line.split()
    except ValueError:
        c.close()
        continue
        
    filename = path[1:]
    
    if filename == '':
        filename = 'index.html'

    mimeType = None
    file_mode = None
    
    if filename == 'index.html':
        mimeType = 'text/html; charset=utf-8'
        file_mode = 'r'
    elif filename == 'iot.png':
        mimeType = 'image/png'
        file_mode = 'rb'
    elif filename == 'favicon.ico':
        mimeType = 'image/x-icon'
        file_mode = 'rb'

    if mimeType and os.path.exists(filename):
        if file_mode == 'r':
            f = open(filename, file_mode, encoding='utf-8')
            file_data = f.read()
            f.close()
        else:
            f = open(filename, file_mode)
            file_data = f.read()
            f.close()
            
        header = 'HTTP/1.1 200 OK\r\n'
        header += 'Content-Type: ' + mimeType + '\r\n'
        header += '\r\n'
        
        c.send(header.encode())
        
        if file_mode == 'r':
            c.send(file_data.encode())
        else:
            c.send(file_data)

    else:
        header = 'HTTP/1.1 404 Not Found\r\n'
        header += '\r\n'
        body = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
        
        c.send(header.encode())
        c.send(body.encode())

    c.close()