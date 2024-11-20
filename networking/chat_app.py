# import socket
# import threading
# # Code to run on one device!!

# # Constants
# HOST = '127.0.0.1'  # Localhost for running on one machine
# PORT = 12346        # Port to listen on (must match for server and clients)
# # original 12345
# BUFFER_SIZE = 1024

# # Global list to store connected clients
# clients = []

# # Server code
# def start_server():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((HOST, PORT))
#     server_socket.listen(5)
#     print(f"[SERVER] Chat server started on {HOST}:{PORT}")
    
#     while True:
#         client_socket, client_address = server_socket.accept()
#         print(f"[SERVER] New connection from {client_address}")
#         clients.append(client_socket)
        
#         # Start a new thread for handling the client
#         client_thread = threading.Thread(target=handle_client, args=(client_socket,))
#         client_thread.start()

# def handle_client(client_socket):
#     try:
#         while True:
#             # Receive message from client
#             message = client_socket.recv(BUFFER_SIZE).decode()
#             if not message:
#                 break
            
#             print(f"[RECEIVED] {message}")
#             # Broadcast message to all other connected clients
#             broadcast_message(message, client_socket)
#     finally:
#         # Remove client and close connection
#         print(f"[SERVER] Client disconnected")
#         clients.remove(client_socket)
#         client_socket.close()

# def broadcast_message(message, sender_socket):
#     for client in clients:
#         if client != sender_socket:
#             try:
#                 # print errors for debugging
#                 print(f"[SERVER] Sending message to client: {message}")
#                 client.send(message.encode())
#             except:
#                 # print errors for debugging 
#                 print(f"[ERRORS] Could not send message to a client")
#                 # If sending fails, remove the client
#                 clients.remove(client)
#                 client.close()

# # Client code
# def start_client():
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((HOST, PORT))
    
#     # Start a thread to listen for incoming messages
#     listener_thread = threading.Thread(target=listen_for_messages, args=(client_socket,))
#     listener_thread.daemon = True
#     listener_thread.start()
    
#     print("[CLIENT] Connected to chat server")
#     print("Type your messages below. Type 'exit' to quit.")
    
#     while True:
#         message = input("")
#         if message.lower() == 'exit':
#             break
#         client_socket.send(message.encode())
    
#     client_socket.close()

# def listen_for_messages(client_socket):
#     while True:
#         try:
#             message = client_socket.recv(BUFFER_SIZE).decode()
#             if message:
#                 print(f"\n[CHAT] {message}", flush = True)
#         except:
#             # print errors for debugging 
#             print(f"[ERROR] Failed to receive message")
#             break

# # Main function to run both server and client
# if __name__ == "__main__":
#     mode = input("Enter 'server' to start the server or 'client' to start the client: ").strip().lower()
    
#     if mode == 'server':
#         start_server()
#     elif mode == 'client':
#         start_client()
#     else:
#         print("Invalid mode. Please enter 'server' or 'client'.")



# *************************************** SECOND SOLUTION ***************************************
# import socket
# import threading

# # Constants
# HOST = '127.0.0.1'  # Localhost
# PORT = 12348        # Port number for both server and client
# BUFFER_SIZE = 1024

# # Global list to store connected clients
# clients = []

# # Server code
# def start_server():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((HOST, PORT))
#     server_socket.listen(5)
#     print(f"[SERVER] Chat server started on {HOST}:{PORT}")
    
#     while True:
#         client_socket, client_address = server_socket.accept()
#         print(f"[SERVER] New connection from {client_address}")
#         clients.append(client_socket)
        
#         # Start a new thread for handling the client
#         client_thread = threading.Thread(target=handle_client, args=(client_socket,))
#         client_thread.start()

# def handle_client(client_socket):
#     try:
#         while True:
#             # Receive message from client
#             message = client_socket.recv(BUFFER_SIZE).decode()
#             if not message:  # Client disconnected
#                 break
#             print(f"[SERVER RECEIVED] {message}")
#             # Broadcast message to all clients
#             broadcast_message(message, client_socket)
#     except:
#         pass
#     finally:
#         # Remove client and close connection
#         print("[SERVER] Client disconnected")
#         clients.remove(client_socket)
#         client_socket.close()

# def broadcast_message(message, sender_socket):
#     for client in clients:
#         if client != sender_socket:
#             try:
#                 client.send(message.encode())
#             except:
#                 # If sending fails, remove the client
#                 clients.remove(client)
#                 client.close()

# # Client code
# def start_client():
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((HOST, PORT))
    
#     # Start a thread to listen for incoming messages
#     listener_thread = threading.Thread(target=listen_for_messages, args=(client_socket,))
#     listener_thread.daemon = True
#     listener_thread.start()
    
#     print("[CLIENT] Connected to chat server")
#     print("Type your messages below. Type 'exit' to quit.")
    
#     while True:
#         message = input("")
#         if message.lower() == 'exit':
#             client_socket.close()
#             break
#         client_socket.send(message.encode())

# def listen_for_messages(client_socket):
#     while True:
#         try:
#             # Receive and display message
#             message = client_socket.recv(BUFFER_SIZE).decode()
#             if message:
#                 print(f"\n[CHAT] {message}")
#         except:
#             # Stop the loop if the connection is broken
#             break

# # Main function to run server or client
# if __name__ == "__main__":
#     mode = input("Enter 'server' to start the server or 'client' to start the client: ").strip().lower()
    
#     if mode == 'server':
#         start_server()
#     elif mode == 'client':
#         start_client()
#     else:
#         print("Invalid mode. Please enter 'server' or 'client'.")

# *************************************** THIRD SOLUTION ***************************************
# import socket
# import threading

# # Constants
# HOST = '127.0.0.1'  # Localhost
# PORT = 12345        # Port to listen on
# BUFFER_SIZE = 1024

# # Flag to control the server loop
# server_running = True

# # List of connected clients
# clients = []

# # Server code
# def start_server():
#     global server_running
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((HOST, PORT))
#     server_socket.listen(5)
#     print(f"[SERVER] Chat server started on {HOST}:{PORT}")

#     # Run server loop
#     while server_running:
#         try:
#             server_socket.settimeout(1)  # Check for stop condition periodically
#             client_socket, client_address = server_socket.accept()
#             print(f"[SERVER] New connection from {client_address}")
#             clients.append(client_socket)
            
#             # Start a new thread for the client
#             client_thread = threading.Thread(target=handle_client, args=(client_socket,))
#             client_thread.start()
#         except socket.timeout:
#             continue

#     # Clean up and close server
#     print("[SERVER] Shutting down...")
#     for client in clients:
#         client.close()
#     server_socket.close()

# def handle_client(client_socket):
#     try:
#         while True:
#             message = client_socket.recv(BUFFER_SIZE).decode()
#             if not message:
#                 break
#             print(f"[RECEIVED] {message}")
#             broadcast_message(message, client_socket)
#     except:
#         pass
#     finally:
#         print("[SERVER] Client disconnected")
#         clients.remove(client_socket)
#         client_socket.close()

# def broadcast_message(message, sender_socket):
#     for client in clients:
#         if client != sender_socket:
#             try:
#                 client.send(message.encode())
#             except:
#                 clients.remove(client)
#                 client.close()

# # Input thread to stop server
# def stop_server():
#     global server_running
#     while True:
#         command = input()
#         if command.lower() == "exit":
#             server_running = False
#             break

# # Main function
# if __name__ == "__main__":
#     # Start server in a thread
#     server_thread = threading.Thread(target=start_server)
#     server_thread.start()
    
#     # Start input listener for stopping the server
#     stop_server()
#     server_thread.join()

# *************************************** FOURTH SOLUTION *************************************** 
# for GUI implementation
# import socket
# import threading

# # Server Configuration
# HOST = '127.0.0.1'
# PORT = 12345
# BUFFER_SIZE = 1024

# # List to manage connected clients
# clients = []

# def broadcast_message(message, sender_socket):
#     for client in clients:
#         if client != sender_socket:
#             try:
#                 client.send(message.encode())
#             except:
#                 clients.remove(client)
#                 client.close()

# def handle_client(client_socket):
#     while True:
#         try:
#             # Receive message
#             message = client_socket.recv(BUFFER_SIZE).decode()
#             print(f"[SERVER] Received: {message}")
#             # Broadcast message to all other clients
#             broadcast_message(message, client_socket)
#         except:
#             # Handle client disconnect
#             print("[SERVER] Client disconnected")
#             clients.remove(client_socket)
#             client_socket.close()
#             break

# def start_server():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((HOST, PORT))
#     server_socket.listen(5)
#     print(f"[SERVER] Server running on {HOST}:{PORT}")

#     while True:
#         client_socket, client_address = server_socket.accept()
#         print(f"[SERVER] Connected with {client_address}")
#         clients.append(client_socket)
#         client_thread = threading.Thread(target=handle_client, args=(client_socket,))
#         client_thread.start()

# if __name__ == "__main__":
#     start_server()

# *************************************** FIFTH SOLUTION *************************************** 

import socket
import threading

# Server Configuration
HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 1024

# List to manage connected clients
clients = []

def broadcast_message(message, sender_socket):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            clients.remove(client)
            client.close()

def handle_client(client_socket):
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(BUFFER_SIZE).decode()
            print(f"[SERVER] Received: {message}")
            # Broadcast message to all clients
            broadcast_message(message, client_socket)
        except:
            # Handle client disconnect
            print("[SERVER] A client has disconnected.")
            clients.remove(client_socket)
            client_socket.close()
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[SERVER] Server running on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"[SERVER] Connected with {client_address}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()

