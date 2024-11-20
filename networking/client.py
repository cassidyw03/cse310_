# client.py

import socket
import threading

# Server Connections
HOST = '127.0.0.1'
PORT = 65432

# Create a TCP socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    # Receive messages from the server
    while True:
        try:
            # Receive and print message from server
            message = client.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def send_messages():
    # Send messages to the server
    while True:
        message = input("You: ")
        client.send(message.encode('utf-8'))

# Start threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()

  