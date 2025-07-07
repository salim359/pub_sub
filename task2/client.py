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
        if message.strip().lower() == 'terminate':
            print("Terminate command received. Closing client.")
            client_socket.close()
            sys.exit(0)

def client(server_ip, port, role):
    c = socket.socket()

    c.connect((server_ip, port))
    print(f"Connected to server {server_ip}:{port} as a {role}.")
    print("Type 'terminate' to exit")

    if role == 'PUBLISHER': 
        init_msg = 'pub'
        # Send initial message to server to indicate role
        c.send(init_msg.encode('utf-8'))

        # Start thread to send messages to server
        send_thread = threading.Thread(target=send_messages, args=(c,), daemon=True)
        send_thread.start()
        
        # Wait for send thread to finish
        send_thread.join()
    else: 
        init_msg = 'sub'
        # Send initial message to server to indicate role
        c.send(init_msg.encode('utf-8'))

        # Main thread handles receiving messages
        receive_thread = threading.Thread(target=receive_messages, args=(c,), daemon=True)
        receive_thread.start()
        
        # Wait for receive thread to finish
        receive_thread.join()

    c.close()
    sys.exit(0)

def send_messages(c):
    """Thread function to handle publisher input and send to server"""
    while True:
        msg = input('PUB: ')
        if msg.lower() == 'terminate':
            print("Terminating client...")
            break
        c.send(msg.encode('utf-8'))

if __name__ == "__main__":

    server_ip=sys.argv[1]
    port=int(sys.argv[2])
    role=sys.argv[3]

    client(server_ip, port, role)