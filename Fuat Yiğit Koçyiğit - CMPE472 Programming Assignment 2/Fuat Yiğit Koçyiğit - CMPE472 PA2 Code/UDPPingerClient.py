# Fuat Yiğit Koçyiğit    #
# CMPE472 Section 1     #
# 16429085948          #

# UDPPingerClient.py

# Importing Python's standard socket module
from socket import *
#
# Importing datetime class
from datetime import datetime
#

# Setting the server name as local host as requested
serverName = 'localhost' #or 127.0.0.1
#
# Setting the server port as 12000 as requested
serverPort = 12000
#
# Creating UDP server socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
#
# Setting the server timeout value as 1 second requested
clientSocket.settimeout(1.0)
#
print("UDP Connection is established.")

# Sending 10 ping to the server as requested
for e in range(10):
    # I set the start of the send time to the StartTime variable (year-month-day hour:minute:seconds.microseconds)
    StartTime = datetime.now()
    #
    # Setting the client message as requested (Ping sequence_number time)
    message = "Ping " + str(e+1) + " " + str(StartTime)
    #

    # Trying to send and receive message within the timeout value
    try:
        # Sending the message to the server and expecting response within the timeout value
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        responseMessage, serverAddress = clientSocket.recvfrom(1024)
        #
        # Calculating the Round Trip Time (RTT) with [current time - send time]
        RTT = datetime.now() - StartTime
        #

        # Printing the ping results and the calculated Round Trip Time (RTT)
        print(f'{responseMessage.decode()}, Round Trip Time (RTT): {RTT}')
        #
    #
    # If timeout is reached, timeout message will be printed
    except Exception as e:
        print("Request timed out")
    #
#

# Closing the client socket
clientSocket.close()
#