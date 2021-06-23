import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket.connect((socket.gethostname(), 8888))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
