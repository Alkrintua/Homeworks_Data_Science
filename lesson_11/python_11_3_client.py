import socket

def start_client():
    server_address = ('localhost', 55000)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    while True:
        message = input('Введіть повідомлення: ')
        client_socket.send(message.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print('Відповідь сервера:', response)

    client_socket.close()

start_client()