import socket
import threading
Host='localhost'
port=9090
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((Host,port))
serverSocket.listen()
print("The server is ready to receive:")
clients=[]
nicknames=[]
def broadcast(message):
    for client in clients:
        client.send(message)
#handle
def handle(client):
    while True:
        try:
            message= client.recv(1024)
            print(f"{nicknames[clients.index(client)]}says {message}")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            nicknames.remove(nickname)
            break


#receive
def receive():
    while True:
        client,address=serverSocket.accept()
        print(f"Connected with {str(address)}")
        client.send("NICKNAME".encode('utf-8'))
        nickname=client.recv(1024)
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} is now connected to server! \n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))
        thread=threading.Thread(target=handle,args=(client,))
        thread.start()


receive()
