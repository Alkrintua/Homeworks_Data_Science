# import socket
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(('', 50000))
# sock.listen(10)
# print("Server is running, please press Ctrl+C to stop")
# while True:
#     conn, adr = sock.accept()
#     print("connected: ", adr)
#     a = conn.recv(1024)
#     print(str(a))
#     conn.send(a)
# conn.close


