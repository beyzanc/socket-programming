import socket
import threading
Host = socket.gethostbyname(socket.gethostname())
Port= 65432
buffersize=1024
Addr=(Host,Port)
user_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_socket.connect(Addr)
print("-----Welcome to Marmara University Chat System------")


def chating():
    print("If you want to exit please type (LOGOUT)")
    while True:
        print("Type Message : ")
        message = input()
        if message=="LOGOUT":
            user_socket.send("\nUSER LOGGED OUT".encode("utf8"))
            exit()
        else:
            user_socket.send(message.encode("utf8"))
def receiving():
    while True:
        print(user_socket.recv(buffersize).decode("utf8"))




while True:
    name=input("Please Type Your Username: ")
    user_socket.send(name.encode("utf8"))
    x=user_socket.recv(buffersize).decode("utf8")
    if x== "True":
        print("your name is already used")
        continue
    else:
        print("Welcome", name)

        break

while True:
    user2=input("Please type name of the Person's Username Who you would like to chat with?")
    user_socket.send(user2.encode("utf8"))
    if user_socket.recv(buffersize).decode("utf8")=="True":
        print(user2, "is available")
        chat=threading.Thread(target=chating)
        receive=threading.Thread(target=receiving)
        chat.start()
        receive.start()

        break
    else:
        print(user2,"is NOT FOUND")
        continue

















