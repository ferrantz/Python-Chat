import socket
import threading

host = input(str("Enter server address you want to connect to: "))
port = 15102
FORMAT = 'utf-8'
buffersize = 15103
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host, port))    

def receive(sock):   
    while True:
        try:
            message = sock.recv(buffersize).decode(FORMAT)
            if message:
                print (message)
            else:
                break
        except:
            print ("There's an error")
            break

def send(sock):  
    while True:
        try:
            message = input()  
            message = message.encode(FORMAT)
            sock.send(message)
        except:
            print ("Hmm... there's an error :c ")
            break
            
def start():
    receiveThread = threading.Thread(target = receive, args = (clientSocket,))
    sendThread = threading.Thread(target = send, args = (clientSocket,))
    receiveThread.start()
    sendThread.start()
                                     
start()