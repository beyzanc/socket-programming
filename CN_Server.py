import socket
import threading
Host = socket.gethostbyname(socket.gethostname())
Port= 65432
buffersize=1024
Server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Addr=(Host,Port)
Server.bind(Addr)
Server.listen(5)


users = {}


print("Waiting for Connection...")
def accept():

    while True:
        clientsocket, address = Server.accept()
        print ("connection from ",address, "has been established")

        threading.Thread(target=join, args=(clientsocket,address)).start()
def join(clientsocket, address):

    while True:
        answer = ""
        name = clientsocket.recv(buffersize).decode("utf8")
        for i in users.keys():
            if i==name:
                answer="True"
                clientsocket.send(bytes(answer,"utf8"))
                break


        if answer=="True":
            continue




        answer="False"
        clientsocket.send(bytes(answer,"utf8"))
        users[name] = clientsocket
        break
    print(name, " loged in")
##############################################################
    user1 = name

    while True:
        user2 = clientsocket.recv(buffersize).decode("utf8")
        answer=" "

        if user2 in users.keys():
            answer="True"
            users[user1].send(bytes(answer, "utf8"))
            revceive_message()
            break

        else:
            answer="False"
            users[user1].send(bytes(answer,"utf8"))
            continue

def revceive_message():
    while True:
        for i in users:
            message=users[i].recv(buffersize).decode("utf8")
            name=i+": "
            message=name+message
            send(message)




def send(message):
    for i in users:
        users[i].send(bytes(message,"utf8"))


ACCEPT_THREAD = threading.Thread(target=accept())
ACCEPT_THREAD.start()