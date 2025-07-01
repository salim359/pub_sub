import socket
import threading

HOST = "localhost"
PORT = 8071

def handle_client(conn, addr):
    """Thread function to continuously receive messages from client"""
    while True:
        data = conn.recv(1024)
        if not data:
            print(f"Client {addr} disconnected.")
            break
        message = data.decode('utf-8')
        print(f"Client {addr}: {message}")
    conn.close()

def send_messages(conn):
    """Thread function to handle server input and send to client"""
    while True:
        msg = input("Server: ")
        if msg.lower() == "exit":
            print("Server shutting down...")
            conn.close()
            break
        conn.sendall(msg.encode('utf-8'))

def start_server():
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server is listening on {HOST}:{PORT}")
        
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    # Start thread to handle client messages
    client_thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
    client_thread.start()
    
    # Start thread to handle server input
    server_thread = threading.Thread(target=send_messages, args=(conn,), daemon=True)
    server_thread.start()
    
    # Wait for server thread to finish (when user types 'exit')
    server_thread.join()
            
    server_socket.close()

if __name__ == "__main__":
    start_server()
