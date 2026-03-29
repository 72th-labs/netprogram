import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

my_name = "leejihwan"  
sock.send(my_name.encode())

id_bytes = sock.recv(4)
student_id = int.from_bytes(id_bytes, byteorder='big')
print(student_id)

sock.close()