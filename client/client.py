import socket
import sys 
import threading

def receive_messages(client_socket):
    """Thread function to continuously receive messages from server"""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Server disconnected.")
                break
            print(f'Server: {message}')
            if message.strip().lower() == 'terminate':
                print("Terminate command received. Closing client.")
                client_socket.close()
                sys.exit(0)
        except:
            break

def client(server_ip, port, role, topic):
    c = socket.socket()

    c.connect((server_ip, port))
    print(f"Connected to server {server_ip}:{port} as a {role} on topic [{topic}]")
    print("Type 'terminate' to exit")

    # Map role to server-expected string
    role_map = {'PUBLISHER': 'pub', 'SUBSCRIBER': 'sub'}
    role_for_server = role_map.get(role.upper(), role.lower())
    init_msg = f"{role_for_server}:{topic}"
    c.send(init_msg.encode('utf-8'))

    if role.upper() == 'PUBLISHER': 
        send_thread = threading.Thread(target=send_messages, args=(c,), daemon=True)
        send_thread.start()
        send_thread.join()
    else:
        receive_thread = threading.Thread(target=receive_messages, args=(c,), daemon=True)
        receive_thread.start()
        receive_thread.join()

    c.close()
    sys.exit(0)

def send_messages(c):
    """Thread function to handle publisher input and send to server"""
    while True:
        msg = input('PUB: ')
        if msg.lower() == 'terminate':
            print("Terminating client...")
            c.send(msg.encode('utf-8'))
            break
        c.send(msg.encode('utf-8'))

    c.close()
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python client.py <server_ip> <port> <PUBLISHER/SUBSCRIBER> <TOPIC>")
        sys.exit(1)

    server_ip = sys.argv[1]
    port = int(sys.argv[2])
    role = sys.argv[3].upper()
    topic = sys.argv[4].upper()

    client(server_ip, port, role, topic)