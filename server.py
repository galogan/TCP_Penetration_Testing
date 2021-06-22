import socket

# Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Gets the ip address of the socket. I could have also hardcoded it to host = 192.168.6.210

host = socket.gethostbyname()
port = 444

# Binding the socket
serversocket.bind((host, port))

# Starting TCP listener
serversocket.listen(3)

while True:
    # Accepts information coming in from client
    clientsocket, address = serversocket.accept()

    print("Received connection from " % str(address))

    message = 'Thank you for connecting to the server' + "\r\n"

    # ascii is used to encode the message
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()  # Closes connection with the client
