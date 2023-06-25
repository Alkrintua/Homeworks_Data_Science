import socket
import threading
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            logging.info('Повідомлення від клієнта: %s', message)

            if message.lower() == 'привіт':
                response = 'Привіт, я чат-бот!'
            elif message.lower() == 'як справи?':
                response = 'У мене все добре, дякую!'
            elif message.lower() == 'до побачення':
                response = 'До побачення! Мені було приємно поговорити.'
            else:
                response = 'Отримав ваше повідомлення: ' + message

            client_socket.send(response.encode('utf-8'))
        except Exception as e:
            logging.error('Помилка при обробці клієнта: %s', str(e))
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 55000))
    server_socket.listen(10)
    logging.info('Сервер запущено. Очікування з\'єднання...')

    while True:
        client_socket, address = server_socket.accept()
        logging.info('Підключився клієнт: %s', str(address))

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()
