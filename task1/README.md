# Task 1: Socket Client-Server Communication

## Overview
This project implements a basic socket-based client-server communication system using Python. The server can handle one client connection at a time and enables bidirectional communication between the client and server.

## Features
- Simple TCP socket communication
- Interactive client-server messaging
- Graceful connection termination
- Command-line argument support
- Multithreaded server for concurrent input/output handling

## Files
- `server.py` - Socket server implementation
- `client.py` - Socket client implementation
- `README.md` - This documentation file

## Requirements
- Python 3.x
- No external dependencies (uses built-in socket and threading modules)

## Usage

### Starting the Server
```bash
python server.py <port>
```

Example:
```bash
python server.py 8080
```

The server will:
- Listen on the specified port (default host: 192.168.8.125)
- Accept one client connection
- Display incoming messages from the client
- Allow you to send messages back to the client
- Type 'exit' to close the server

### Starting the Client
```bash
python client.py <server_ip> <port>
```

Example:
```bash
python client.py 192.168.8.125 8080
```

The client will:
- Connect to the specified server IP and port
- Allow you to send messages to the server
- Display responses from the server
- Type 'terminate' to close the connection

## Communication Flow
1. Server starts and listens on the specified port
2. Client connects to the server
3. Both client and server can send messages interactively
4. Messages are displayed in real-time on both sides
5. Connection can be terminated by either side

## Example Session

**Server Terminal:**
```
$ python server.py 8080
Server is listening 192.168.8.125:8080
Connected by ('192.168.8.100', 12345)
('192.168.8.100', 12345): Hello server!
server: Hi there, client!
```

**Client Terminal:**
```
$ python client.py 192.168.8.125 8080
Enter your Message to server or 'terminate' (if you want to close the connection):
 You: Hello server!
Server: Hi there, client!
Enter your Message to server or 'terminate' (if you want to close the connection):
 You: terminate
Terminating client.....
```

## Technical Details
- Uses TCP sockets for reliable communication
- Server handles one client at a time
- Multithreaded design allows simultaneous message sending and receiving
- Error handling for connection issues
- Clean shutdown mechanisms

## Limitations
- Server only supports one client connection at a time
- Hardcoded server host IP (192.168.8.125)
- No message persistence or logging
- No authentication or security features

## Future Improvements
- Support for multiple concurrent clients
- Configurable server host IP
- Message logging and persistence
- Enhanced error handling and reconnection logic
- Security features (authentication, encryption)