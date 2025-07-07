import socket
import threading

HOST = "localhost"
PORT = 8071

# New: topic -> list of subscriber connections
subscribers_by_topic = {}
clients_lock = threading.Lock()

def broadcast_to_subscribers(topic, message, sender_addr):
    """Send message to all subscribers of a topic"""
    with clients_lock:
        if topic not in subscribers_by_topic:
            return

        disconnected_subs = []
        for conn in subscribers_by_topic[topic]:
            try:
                conn.sendall(f"[{topic}] {sender_addr}: {message}".encode('utf-8'))
            except:
                print(f"[{topic}] Subscriber {sender_addr} disconnected during broadcast.")
                disconnected_subs.append(conn)

        for conn in disconnected_subs:
            subscribers_by_topic[topic].remove(conn)

def handle_client(conn, addr):
    """Handle client communication with topic support"""
    try:
        init_data = conn.recv(1024)
        if not init_data:
            conn.close()
            return

        parts = init_data.decode('utf-8').strip().split(":")
        if len(parts) != 2:
            print(f"Invalid initial data from {addr}")
            conn.close()
            return

        role, topic = parts[0].lower(), parts[1].upper()

        if role == "sub":
            with clients_lock:
                if topic not in subscribers_by_topic:
                    subscribers_by_topic[topic] = []
                subscribers_by_topic[topic].append(conn)
            print(f"[SUBSCRIBER] {addr} subscribed to topic [{topic}]")

            # Keep the connection open and wait for disconnect
            try:
                while True:
                    data = conn.recv(1)
                    if not data:
                        break
            except Exception:
                pass

        elif role == "pub":
            print(f"[PUBLISHER] {addr} publishing to topic [{topic}]")
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                message = data.decode('utf-8').strip()
                if message.lower() == 'terminate':
                    break

                broadcast_to_subscribers(topic, message, addr)

    except Exception as e:
        print(f"Error with client {addr}: {e}")
    finally:
        # Cleanup
        with clients_lock:
            for topic in subscribers_by_topic:
                if conn in subscribers_by_topic[topic]:
                    subscribers_by_topic[topic].remove(conn)
        conn.close()
        print(f"[DISCONNECTED] {addr}")

def server_commands():
    """Handle server commands"""
    while True:
        cmd = input().strip().lower()
        if cmd == 'exit':
            print("Server shutting down...")
            return
        elif cmd == 'status':
            with clients_lock:
                total = sum(len(v) for v in subscribers_by_topic.values())
                print(f"Active Subscribers: {total}")
                for topic, subs in subscribers_by_topic.items():
                    print(f"- {topic}: {len(subs)} subscriber(s)")

def start_server():
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Pub-Sub Server with Topics is listening on {HOST}:{PORT}")
    print("Commands: status, exit")

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
        print("Server interrupted. Shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
