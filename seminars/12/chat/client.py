import socket
import threading

client_sock = socket.socket()
client_sock.connect(('localhost', 5000))

client_sock.send(input('Введите имя пользователя: ').encode())

def receive_message():

    while True:

        data = client_sock.recv(1024)

        if data:
            print(data.decode("utf-8"))
        else:
            client_sock.close()
            break

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

while True:

    client_sock.send(input().encode())