#Fuat Yiğit Koçyiğit    #
#CMPE472 Section 1     #
#16429085948          #

# import socket module
from socket import *
import sys  # In order to terminate the program

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
# Fill in start - 1 -
# serverSocket.bind((IP Address, Port))
serverSocket.bind(('192.168.1.72', 63342))
serverSocket.listen(1)
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    # Fill in start - 2 -
    connectionSocket, addr = serverSocket.accept()
    # Fill in end

    try:
        # Fill in start - 3 -
        message = connectionSocket.recv(1024).decode()
        # Fill in end
        filename = message.split()[1]
        f = open(filename[1:])

        # Fill in start - 4 -
        outputdata = f.read()
        # Fill in end

        # Send one HTTP header line into socket

        # http://192.168.1.72:63342/HelloWorld.html

        # Fill in start - 5 -
        connectionSocket.send("\nHTTP/1.1 200 OK\nContent-Type: text/html\n\n".encode())
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        # Send response message for file not found

        # http://192.168.1.72:63342/ByeWorld.html

        # Fill in start - 6 -
        connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
        # Fill in end

        # Close client socket
        # Fill in start - 7 -
        connectionSocket.close()
        # Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding