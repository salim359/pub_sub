import socket
import threading

HOST = "localhost"
PORT = 8071

# Global data structures to store clients
publishers = {}  # {connection: (addr, connection)}
subscribers = {}  # {connection: (addr, connection)}
clients_lock = threading.Lock()

def broadcast_to_subscribers(message, sender_addr):
    """Send message to all subscribers"""
    with clients_lock:
        disconnected_subs = []
        for conn, (addr, _) in subscribers.items():
            try:
                conn.sendall(f"[{sender_addr}]: {message}".encode('utf-8'))
            except:
                print(f"Subscriber {addr} disconnected during broadcast.")
                disconnected_subs.append(conn)
        
        # Clean up disconnected subscribers
        for conn in disconnected_subs:
            if conn in subscribers:
                del subscribers[conn]

def handle_client(conn, addr):
    """Thread function to handle client communication"""
    client_type = None

    # First message should indicate client type ('pub' or 'sub')
    data = conn.recv(1024)
    if not data:
        return
    
    client_type = data.decode('utf-8').strip()
    
    with clients_lock:
        if client_type == 'pub':
            publishers[conn] = (addr, conn)
            print(f"Publisher {addr} connected. Total publishers: {len(publishers)}")
        elif client_type == 'sub':
            subscribers[conn] = (addr, conn)
            print(f"Subscriber {addr} connected. Total subscribers: {len(subscribers)}")
        else:
            print(f"Unknown client type '{client_type}' from {addr}")
            conn.close()
            return
    
    # Handle messages based on client type
    while True:
        data = conn.recv(1024)
        if not data:
            break
        
        message = data.decode('utf-8').strip()
        
        if message.lower() == 'terminate':
            print(f"{client_type.capitalize()} {addr} requested termination.")
            break
        
        if client_type == 'pub':
            print(f"Publisher {addr}: {message}")
            # Broadcast message to all subscribers
            broadcast_to_subscribers(message, addr)
        elif client_type == 'sub':
            print(f"Subscriber {addr}: {message}")
            # Subscribers typically don't send messages, but we log them


    # Clean up client from appropriate list
    with clients_lock:
        if conn in publishers:
            del publishers[conn]
            print(f"Publisher {addr} disconnected. Total publishers: {len(publishers)}")
        elif conn in subscribers:
            del subscribers[conn]
            print(f"Subscriber {addr} disconnected. Total subscribers: {len(subscribers)}")
    
    conn.close()

def server_commands():
    """Handle server commands"""
    while True:
        cmd = input().strip().lower()
        if cmd == 'exit':
            print("Server shutting down...")
            return
        elif cmd == 'status':
            with clients_lock:
                print(f"Publishers: {len(publishers)}, Subscribers: {len(subscribers)}")


def start_server():
    server_socket = socket.socket()
    # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)  # Allow multiple connections
    print(f"Pub-Sub Server is listening on {HOST}:{PORT}")
    print("Commands: status, exit/quit, help")
    
    # Start server command thread
    command_thread = threading.Thread(target=server_commands, daemon=True)
    command_thread.start()
    
    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"New connection from {addr}")
            
            # Start thread to handle this client
            client_thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            client_thread.start()
    
    except KeyboardInterrupt:
        print("\nServer interrupted. Shutting down...")
    
    finally:
        # Close all client connections
        with clients_lock:
            for conn, _ in list(publishers.items()):
                try:
                    conn.close()
                except:
                    pass
            for conn, _ in list(subscribers.items()):
                try:
                    conn.close()
                except:
                    pass
        
        server_socket.close()
        print("Server shut down complete.")

if __name__ == "__main__":
    start_server()
