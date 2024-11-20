# import socket
# import threading

# # Server Configuration
# HOST = '127.0.0.1'
# PORT = 12345
# BUFFER_SIZE = 1024

# # List of connected clients
# clients = []

# def broadcast_message(message, sender_socket=None):
#     for client in clients:
#         # Send to all clients except the sender (optional: remove this check if you want to echo back to the sender)
#         if client != sender_socket:
#             try:
#                 client.send(message.encode())
#             except:
#                 clients.remove(client)
#                 client.close()

# def handle_client(client_socket):
#     while True:
#         try:
#             # Receive message from the client
#             message = client_socket.recv(BUFFER_SIZE).decode()
#             print(f"[SERVER] Received: {message}")
#             # Respond to the client
#             response = f"Server received: {message}"
#             client_socket.send(response.encode())
#             # Broadcast to other clients
#             broadcast_message(f"Client said: {message}", client_socket)
#         except:
#             print("[SERVER] A client has disconnected.")
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
#         # Handle client in a new thread
#         client_thread = threading.Thread(target=handle_client, args=(client_socket,))
#         client_thread.start()

# if __name__ == "__main__":
#     start_server()
import socket
import threading

# Server Configuration
HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 1024

# List to manage connected clients and their names
clients = []

def broadcast_message(message, sender_socket=None):
    """Broadcast message to all clients except the sender."""
    for client, client_name in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                clients.remove((client, client_name))
                client.close()

def handle_client(client_socket):
    """Handle messages from each client."""
    client_name = client_socket.recv(BUFFER_SIZE).decode()  # Get client's name when they first connect
    print(f"[SERVER] {client_name} connected.")

    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(BUFFER_SIZE).decode()
            if message:
                # Broadcast message to all clients
                broadcast_message(f"{client_name} said: {message}", client_socket)
        except:
            # Handle client disconnect
            print(f"[SERVER] {client_name} has disconnected.")
            clients.remove((client_socket, client_name))
            client_socket.close()
            break

def start_server():
    """Start the server and accept connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[SERVER] Server running on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"[SERVER] Connected with {client_address}")
        
        # Add client and their name to the clients list
        client_name = client_socket.recv(BUFFER_SIZE).decode()  # Receive the name of the client
        clients.append((client_socket, client_name))

        # Start handling this client in a separate thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()

