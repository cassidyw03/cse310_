# Overview

{This assignment was to improve my knowledge of networking frameworks and particularly peer to peer models.}

{To use this software you must open three terminals. The first will run the server, the second will run where the first client is and the third will run the second client. The server host the connection and the clients speak there!}

{My purpose for writing this software was to create a simple chat application where clients can connect to a server, send messages, and receive responses.}

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

{This is a peer to peer system, so it communicates via peers and not the server itself.}

{I used TCP and the Port number 12345. I decided to use TCP and not UDP because it is more reliable, it performs error-checking, and it is based on a connection between the sender and receiver before the transmission starts.}

{The peers receive messages via personal GUI displays. They enter a message and it shows up on their text screen and their peers text screen.}

# Development Environment

{I used Chat GPT for teaching me how to create a Network with a client and a server. It also helped me build the GUI!}

{This is made in python. For networking I needed the socket and threading libraries. The socket library allows to me communicate between two devices over a network. In this case I am communicating in separate terminals since I do not have access to another device and my machine cannot run a virtual machine. }

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Tutorials Point](https://www.tutorialspoint.com/Peer-to-Peer-Computing)
* [How to Geek](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* I need to make the name assignment more clear so that it won't be confusing what the name is supposed to be.
* I think adding a prettier GUI would be fun too. I would like to make so the messages from the 1st and 2nd person appear in different sides, like a text chain.