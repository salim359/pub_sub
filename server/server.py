import socket
import threading

HOST = "localhost"
PORT = 8071



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


socket = socket.socket()
socket.bind((HOST, PORT))

socket.listen(1)
print(f"Server is listening {HOST}:{PORT}")

conn, addr = socket.accept()
print(f"Connected by {addr}")


# Start thread to read from client
threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

# Main thread reads CLI input
read_cli_input(conn)

socket.close()
