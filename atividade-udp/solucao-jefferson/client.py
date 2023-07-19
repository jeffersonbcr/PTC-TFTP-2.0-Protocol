import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

serverAddressPort = (localIP, localPort)
msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)