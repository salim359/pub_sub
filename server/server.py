import socket
import threading
import argparse

HOST = "192.168.8.125"


def handle_client(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            print("Client disconnected.")
            break
        print(f"{addr}: {data.decode()}")


def read_cli_input(conn):
    while True:
        msg = input("")
        if msg.lower() == "exit":
            conn.close()
            break
        print(f"server: {msg}")
        conn.sendall(msg.encode())


def main():
    parser = argparse.ArgumentParser(description="Socket server")
    parser.add_argument("port", type=int, help="Port number to listen on")
    args = parser.parse_args()

    port = args.port

    server_socket = socket.socket()
    server_socket.bind((HOST, port))

    server_socket.listen(1)
    print(f"Server is listening {HOST}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Start thread to read from client
    threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

    # Main thread reads CLI input
    read_cli_input(conn)

    server_socket.close()


if __name__ == "__main__":
    main()
