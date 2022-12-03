import socket
import threading

server_sock = None

clients = {}
names ={}

def create_server():

    global server_sock

    server_sock = socket.socket()
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('0.0.0.0', 5000))
    server_sock.listen()

    accept_thread = threading.Thread(target=accept_connection)
    accept_thread.start()


def accept_connection():

    print('Thread accept connection started!')

    while True:

        client_sock, client_addr = server_sock.accept()
        clients[client_addr] = client_sock
        print(client_addr)

        data = client_sock.recv(1024)
        names[client_addr] = data.decode("utf-8")

        print(names)

        receive_thread = threading.Thread(target=receive_message, args=[client_sock])
        receive_thread.start()

def send_message(client_sock, data):
    
    client_sock.send(data)

def send_message_to_all(sender, data):
    message = data.decode("utf-8")
    sender_message = names[sender.getpeername()] + ' : ' + message
    for client_sock in clients.values():
        if client_sock != sender:
         
            client_sock.send(sender_message.encode())

def receive_message(client_sock):

    while True:

        try:
            data = client_sock.recv(1024)
        except:
            del clients[client_sock.getpeername()]
            break

        if data:
            print(data.decode("utf-8"))
            try: 
                send_message_to_all(client_sock, data)
            except:
                pass
        else:
            client_sock.close()
            del clients[client_sock.getpeername()]
            break

create_server()