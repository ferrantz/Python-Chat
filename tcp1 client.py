import threading
import socket

host = input(str("Enter server address you want to connect to: "))
Port = 15103
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host, Port))
buffersize = 2048
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "quit"

def send(conn):
    
    while True:
            message = input()
            if message == DISCONNECT_MESSAGE:
                conn.close()
                break
            else:
                clientSocket.send(message.encode("utf8"))
        
def receive(sock, buffersize):

    while True:
        try:
            reply = clientSocket.recv(buffersize)
            if reply.decode() == DISCONNECT_MESSAGE:                
                print("Closing connection...")
                sock.close()
                break
            print("Server:" + reply.decode())
        except ConnectionAbortedError:   
            print("Connection closed")
            break

def main():
    t1 = threading.Thread(target=send, args=(clientSocket,))                  
    t2 = threading.Thread(target=receive, args=(clientSocket, buffersize))    
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()