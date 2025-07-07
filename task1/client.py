import socket
import argparse


def client(server_ip, port):
    c = socket.socket()
    c.connect((server_ip, port))

    while True:
        msg = input(
            "Enter your Message to server or 'terminate' (if you want to close the connection):\n You: "
        )

        if msg.lower() == "terminate":
            print("Terminating client.....")
            c.close()
            break

        c.send(bytes(msg, "utf-8"))
        try:
            response = c.recv(1024).decode()
            print("Server:", response)
        except Exception as e:
            print(f"Connection lost with server: {e}")
            break


def main():
    parser = argparse.ArgumentParser(description="Socket client")
    parser.add_argument("server_ip", help="Server IP address to connect to")
    parser.add_argument("port", type=int, help="Port number to connect to")
    args = parser.parse_args()

    client(args.server_ip, args.port)


if __name__ == "__main__":
    main()
