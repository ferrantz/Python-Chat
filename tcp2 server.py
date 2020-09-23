import socket 
import threading

PORT = 10000
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "quit"
buffersize = 2048
list_of_clients = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', PORT))

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send ("Now you are online! In this moment there are ".encode(FORMAT) + str({threading.activeCount() - 1}).encode(FORMAT) +  " users connected. Type quit to exit!".encode())  
    list_of_clients.append(conn)
    
    connected = True
    while connected:
        msg = conn.recv(buffersize).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            print("Closing connection...")
            conn.send("___You are outside the chatroom___".encode(FORMAT))
            conn.close()
            print ("{} has left the chat".format(addr))
            break
        
        else:
            print(f"[{addr}] {msg}")
            completeMessage = (HOST + ", " + str(PORT) + ": " + msg)
            broadcast(conn, completeMessage.encode(FORMAT))

def broadcast(sock, message):
    for socket in list_of_clients:
        if  socket != server and  socket != sock:
            try:
                socket.send(message)
            except:
                socket.close()
                list_of_clients.remove(socket)
                
def start():
    server.listen(10)
    print(f"[LISTENING] Server is listening on {HOST}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()