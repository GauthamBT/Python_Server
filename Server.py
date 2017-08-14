import socket

from _socket import SOCK_STREAM, AF_INET

parentSocket = socket.socket(AF_INET, SOCK_STREAM, 0)

print("After socket")

parentSocket.bind(("127.0.0.1", 8888))

print("After bind")

parentSocket.listen(5)

print("After listen")

while True:
    slaveSocket, a = parentSocket.accept()

    print("After accept. Client Address: ", slaveSocket)
    
    slaveSocket.send(b'Hello Client')
    
    print("After send")
    
    print("Received message: ",(slaveSocket.recv(1024)).decode("utf-8"))
    
    file = open("new.txt","rb+")
    
    while c != None:
        c = file.read(1)
    
        slaveSocket.send(c)
    
    file.close()
    
    slaveSocket.close()

parentSocket.close()

print("End of program")