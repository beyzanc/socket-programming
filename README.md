# Socket Programming

This repository covers the basics of socket programming, a method to connect two nodes on a network for communication. Essentially, socket programming involves two elements: ***a server and a client***.

## Server Side

The server creates a listener socket, listening on a specific IP address and port for incoming requests. This process is initiated by importing the socket library and creating a simple socket. The server then uses the bind() method to bind the listener socket to a specific IP and port. After binding, the server uses the listen() method to switch into listening mode, enabling it to monitor incoming connections.

Upon receiving a connection request, the server uses the accept() method to establish a connection with the client. After the communication is finished, the server uses the close() method to terminate the connection.

## Client Side

The client script attempts to connect to the server socket created at the specified IP address and port. After a connection is established, it continually checks whether input is from the server or the client, redirecting output accordingly. If the input is from the server, it displays the message on the terminal. If the input is from the user, it sends the user's message to the server for potential broadcasting to other users.

## Threading

In the context of socket programming, threads are particularly useful. A thread is a subprocess that runs a set of commands independent of any other thread. Each time a user connects to the server, a separate thread is created. Communications between the server and each client occur along individual threads, with each thread based on a socket object created for the identity of each client. This approach enables simultaneous and efficient communications with multiple users.

## Conclusion

Socket programming and threading are the backbone of many network communications, including web browsing. This repository provides a basic understanding and implementation of these concepts. Your contributions and improvements are always welcome.
