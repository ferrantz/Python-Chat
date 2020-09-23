import threading
import socket

SERVER = ""           
port = 10000
FORMAT = 'utf-8'
buffersize = 2048
DISCONNECT_MESSAGE = "quit"

def  send ():
    while True:
        message =  input()
        if message == DISCONNECT_MESSAGE:
            conn.close()
            print("Ending connection")
            break
        else:
            message = message.encode()
            conn.send(message)

def receive(sock):
    
    name = sock.recv(buffersize)
    name = name.decode()
    while True:
        try:
            reply = sock.recv(buffersize)
            if reply.decode() == DISCONNECT_MESSAGE:        
                print ("Ending connection")
                sock.close()
                break
            print (name + ":" + reply.decode())   
        except:
            print ("Connection closed")
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    try:
        serverSocket.bind((SERVER, port))
        serverSocket.listen(1)
        print ("Server is on")
        conn, addr = serverSocket.accept()
        if conn:                                   
            print('Connected by', addr)
            conn.send("Hi, we are connected! Type quit to disconnect. ENTER YOUR NAME: ".encode())
            
    except ConnectionAbortedError:
        print("There's an error")
    
def main():
    t1 = threading.Thread(target=send)
    t2 = threading.Thread(target=receive, args=(conn,))    
    t1.start()
    t2.start()
    
if __name__ == "__main__":
    main()
    