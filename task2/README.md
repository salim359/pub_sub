# Task 2: Publish-Subscribe (Pub-Sub) Communication System

## Overview
This project implements a publish-subscribe messaging system using Python sockets. The server acts as a message broker that manages publishers and subscribers, broadcasting messages from publishers to all connected subscribers in real-time.

## Features
- **Multi-client support**: Handles multiple publishers and subscribers simultaneously
- **Message broadcasting**: Messages from publishers are automatically sent to all subscribers
- **Role-based client connections**: Clients connect as either publishers or subscribers
- **Concurrent connections**: Multithreaded server handles multiple clients concurrently
- **Real-time messaging**: Instant message delivery from publishers to subscribers
- **Connection management**: Automatic cleanup of disconnected clients
- **Server commands**: Built-in commands for monitoring and control

## Architecture
- **Server**: Acts as a message broker, managing client connections and routing messages
- **Publishers**: Clients that send messages to the server for broadcasting
- **Subscribers**: Clients that receive messages from publishers via the server

## Files
- `server.py` - Pub-Sub server implementation with message brokering
- `client.py` - Client implementation supporting both publisher and subscriber roles
- `README.md` - This documentation file
- `task2.mkv` - Video demonstration of the system

## Requirements
- Python 3.x
- No external dependencies (uses built-in socket and threading modules)

## Usage

### Starting the Server
```bash
python server.py
```

The server will:
- Listen on `localhost:8071`
- Accept multiple client connections
- Display connection status for publishers and subscribers
- Show all incoming messages with sender information
- Broadcast messages from publishers to all subscribers

**Server Commands:**
- `status` - Show current number of publishers and subscribers
- `exit` - Shutdown the server gracefully
- `Ctrl+C` - Force shutdown

### Starting Clients

#### Publisher Client
```bash
python client.py <server_ip> <port> PUBLISHER
```

Example:
```bash
python client.py localhost 8071 PUBLISHER
```

The publisher will:
- Connect to the server and register as a publisher
- Prompt for messages to send with `PUB: `
- Broadcast messages to all subscribers via the server
- Type `terminate` to disconnect

#### Subscriber Client
```bash
python client.py <server_ip> <port> SUBSCRIBER
```

Example:
```bash
python client.py localhost 8071 SUBSCRIBER
```

The subscriber will:
- Connect to the server and register as a subscriber
- Receive and display messages from all publishers
- Show messages in format: `Server: [publisher_address]: message`
- Automatically disconnect when receiving `terminate` command

## Example Usage Scenario

1. **Start the server:**
   ```bash
   python server.py
   ```

2. **Start a subscriber in another terminal:**
   ```bash
   python client.py localhost 8071 SUBSCRIBER
   ```

3. **Start a publisher in another terminal:**
   ```bash
   python client.py localhost 8071 PUBLISHER
   ```

4. **Send messages from publisher:**
   ```
   PUB: Hello subscribers!
   PUB: This is a test message
   ```

5. **Subscriber receives:**
   ```
   Server: [('127.0.0.1', 54321)]: Hello subscribers!
   Server: [('127.0.0.1', 54321)]: This is a test message
   ```

## Technical Details

### Communication Protocol
1. **Connection Phase**: Client sends role identifier ('pub' or 'sub')
2. **Message Phase**: Publishers send messages, subscribers receive broadcasts
3. **Termination Phase**: 'terminate' command closes connections gracefully

### Threading Model
- **Server**: One thread per client connection + main thread for new connections
- **Publisher Client**: Main thread for input, separate thread for sending
- **Subscriber Client**: Main thread for receiving, separate thread for message handling

### Data Structures
- `publishers`: Dictionary mapping connections to publisher information
- `subscribers`: Dictionary mapping connections to subscriber information
- `clients_lock`: Thread lock for safe concurrent access to client lists

## Message Flow
1. Publisher sends message to server
2. Server receives message and identifies sender
3. Server broadcasts message to all connected subscribers
4. Subscribers receive message with sender identification

## Error Handling
- Automatic cleanup of disconnected clients
- Graceful handling of network errors
- Thread-safe client management
- Proper resource cleanup on termination

## Improvements from Task 1
- **Multiple clients**: Supports many publishers and subscribers vs. single client
- **Message broadcasting**: One-to-many communication pattern
- **Role-based connections**: Different client types with specific behaviors
- **Concurrent messaging**: Multiple publishers can send simultaneously
- **Better resource management**: Improved cleanup and error handling