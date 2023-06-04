import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print('Повідомлення від клієнта:', message)
            ls = len(message.split(" "))


            response = 'Отримав ваше повідомлення: ' + message + "\nВ ньому знаходиться всього " + str(ls) + " слів."

            client_socket.send(response.encode('utf-8'))
        except:
            print('Відключився клієнт')
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 55000))
    server_socket.listen(10)
    print('Сервер запущено. Очікування з\'єднання...')

    while True:
        client_socket, address = server_socket.accept()
        print('Підключився клієнт:', address)

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()