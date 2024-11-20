# import socket
# import threading
# import tkinter as tk
# from tkinter import scrolledtext, messagebox

# # Client Configuration
# HOST = '127.0.0.1'
# PORT = 12345
# BUFFER_SIZE = 1024

# class ChatClient:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Chat Application")

#         # GUI Components
#         self.chat_display = scrolledtext.ScrolledText(root, state='disabled', width=50, height=20)
#         self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#         self.entry_message = tk.Entry(root, width=40)
#         self.entry_message.grid(row=1, column=0, padx=10, pady=10)

#         self.send_button = tk.Button(root, text="Send", width=10, command=self.send_message)
#         self.send_button.grid(row=1, column=1, padx=10, pady=10)

#         # Socket Setup
#         self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         try:
#             self.client_socket.connect((HOST, PORT))
#         except ConnectionRefusedError:
#             messagebox.showerror("Connection Error", "Could not connect to the server. Please ensure the server is running.")
#             self.root.destroy()
#             return

#         # Start Listening for Incoming Messages
#         self.listener_thread = threading.Thread(target=self.receive_messages, daemon=True)
#         self.listener_thread.start()

#     def send_message(self):
#         message = self.entry_message.get()
#         if message.strip():
#             self.client_socket.send(message.encode())
#             self.entry_message.delete(0, tk.END)

#     def receive_messages(self):
#         while True:
#             try:
#                 message = self.client_socket.recv(BUFFER_SIZE).decode()
#                 self.display_message(message)
#             except:
#                 print("[ERROR] Lost connection to the server.")
#                 break

#     def display_message(self, message):
#         self.chat_display.config(state='normal')
#         self.chat_display.insert(tk.END, f"{message}\n")
#         self.chat_display.config(state='disabled')
#         self.chat_display.see(tk.END)

#     def on_close(self):
#         self.client_socket.close()
#         self.root.destroy()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ChatClient(root)
#     root.protocol("WM_DELETE_WINDOW", app.on_close)  # Graceful exit
#     root.mainloop()

# ************************* SECOND SOLUTION **************************
# import socket
# import threading
# import tkinter as tk
# from tkinter import scrolledtext, messagebox

# # Client Configuration
# HOST = '127.0.0.1'
# PORT = 12345
# BUFFER_SIZE = 1024

# class ChatClient:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Chat Application")

#         # GUI Components
#         self.chat_display = scrolledtext.ScrolledText(root, state='disabled', width=50, height=20)
#         self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#         self.entry_message = tk.Entry(root, width=40)
#         self.entry_message.grid(row=1, column=0, padx=10, pady=10)

#         self.send_button = tk.Button(root, text="Send", width=10, command=self.send_message)
#         self.send_button.grid(row=1, column=1, padx=10, pady=10)

#         # Socket Setup
#         self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         try:
#             self.client_socket.connect((HOST, PORT))
#         except ConnectionRefusedError:
#             messagebox.showerror("Connection Error", "Could not connect to the server. Please ensure the server is running.")
#             self.root.destroy()
#             return

#         # Start Listening for Incoming Messages
#         self.listener_thread = threading.Thread(target=self.receive_messages, daemon=True)
#         self.listener_thread.start()

#     def send_message(self):
#         message = self.entry_message.get()
#         if message.strip():
#             try:
#                 # Send message to the server
#                 self.client_socket.send(message.encode())
#                 self.display_message(f"You: {message}")
#                 self.entry_message.delete(0, tk.END)
#             except:
#                 messagebox.showerror("Connection Error", "Unable to send the message.")
#                 self.root.destroy()

#     def receive_messages(self):
#         while True:
#             try:
#                 # Receive messages from the server
#                 message = self.client_socket.recv(BUFFER_SIZE).decode()
#                 self.display_message(message)
#             except:
#                 print("[ERROR] Lost connection to the server.")
#                 break

#     def display_message(self, message):
#         """Display a message in the chat window."""
#         self.chat_display.config(state='normal')
#         self.chat_display.insert(tk.END, f"{message}\n")
#         self.chat_display.config(state='disabled')
#         self.chat_display.see(tk.END)

#     def on_close(self):
#         self.client_socket.close()
#         self.root.destroy()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ChatClient(root)
#     root.protocol("WM_DELETE_WINDOW", app.on_close)  # Graceful exit
#     root.mainloop()

import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Client Configuration
HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 1024

class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")

        # GUI Components
        self.chat_display = scrolledtext.ScrolledText(root, state='disabled', width=50, height=20)
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.entry_message = tk.Entry(root, width=40)
        self.entry_message.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(root, text="Send", width=10, command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.entry_name_label = tk.Label(root, text="Enter your name:")
        self.entry_name_label.grid(row=2, column=0, padx=10, pady=10)

        self.entry_name = tk.Entry(root, width=40)
        self.entry_name.grid(row=2, column=1, padx=10, pady=10)

        self.client_name = ""
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Attempt to connect to the server
        try:
            self.client_socket.connect((HOST, PORT))
        except ConnectionRefusedError:
            messagebox.showerror("Connection Error", "Could not connect to the server. Please ensure the server is running.")
            self.root.destroy()
            return

        self.client_name = self.entry_name.get() if self.entry_name.get() else "Anonymous"
        self.client_socket.send(self.client_name.encode())  # Send the client name to the server

        # Start listening for incoming messages
        self.listener_thread = threading.Thread(target=self.receive_messages, daemon=True)
        self.listener_thread.start()

    def send_message(self):
        """Send the message to the server."""
        message = self.entry_message.get()
        if message.strip():
            try:
                self.client_socket.send(message.encode())  # Send message to server
                self.display_message(f"You: {message}")  # Display sent message on own GUI
                self.entry_message.delete(0, tk.END)
            except:
                messagebox.showerror("Connection Error", "Unable to send the message.")
                self.root.destroy()

    def receive_messages(self):
        """Listen for messages from the server."""
        while True:
            try:
                message = self.client_socket.recv(BUFFER_SIZE).decode()
                self.display_message(message)  # Display the received message
            except:
                print("[ERROR] Lost connection to the server.")
                break

    def display_message(self, message):
        """Display a message in the chat window."""
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, f"{message}\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

    def on_close(self):
        """Close the client socket and GUI."""
        self.client_socket.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClient(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)  # Graceful exit
    root.mainloop()


