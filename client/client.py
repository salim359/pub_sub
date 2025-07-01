import socket
import sys 
import threading

def receive_messages(client_socket):
    """Thread function to continuously receive messages from server"""
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            print("Server disconnected.")
            break
        print(f'Server: {message}')

def client(server_ip, port):
    c = socket.socket()

    c.connect((server_ip, port))
    print(f"Connected to server {server_ip}:{port}")
    print("Type 'terminate' to exit")
    
    # Start thread to receive messages from server
    receive_thread = threading.Thread(target=receive_messages, args=(c,), daemon=True)
    receive_thread.start()
    
    # Main thread handles sending messages
    while True:
        msg = input('You: ')
        if msg.lower() == 'terminate':
            print("Terminating client...")
            break
        c.send(msg.encode('utf-8'))

    c.close()
    sys.exit(0)
        
if __name__ == "__main__":

    server_ip=sys.argv[1]
    port=int(sys.argv[2])
    
    client(server_ip,port)