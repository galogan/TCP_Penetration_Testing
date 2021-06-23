import socket

# Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Gets the ip address of the socket. I could have also hardcoded it to host = 192.168.6.210

# Binding the socket
serversocket.bind((socket.gethostname, 8888))

# Starting TCP listener
serversocket.listen(5) # 5 means the number of connections in the queue

while True:
    # Accepts information coming in from client
    clientsocket, address = serversocket.accept()

    print("Received connection from %s " % str(address))

    message = 'Thank you for connecting to the server' + "\r\n"

    # ascii is used to encode the message
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()  # Closes connection with the client
