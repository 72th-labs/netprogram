import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())

    name_bytes = client.recv(1024)
    print(name_bytes.decode())
 
    student_id = 20211497  
    
    id_bytes = student_id.to_bytes(4, byteorder='big') 
    client.send(id_bytes)
    
    client.close()