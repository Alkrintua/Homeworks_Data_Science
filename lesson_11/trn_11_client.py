import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 50000))
sock.send(bytes("7", encoding="UTF-8"))
a = sock.recv(1024)
sock.close()
print(a)