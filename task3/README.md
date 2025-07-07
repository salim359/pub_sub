# Task 3: Pub-Sub System with Topic Support

## Overview
This task implements a **Publisher-Subscriber (Pub-Sub) system with topic-based messaging** using Python sockets. The system allows multiple publishers and subscribers to communicate through specific topics, enabling organized message distribution.

## Architecture
- **Server**: Central message broker that manages topics and routes messages
- **Publishers**: Clients that send messages to specific topics
- **Subscribers**: Clients that receive messages from specific topics
- **Topics**: Message categories that organize communication channels

## Key Features
- ✅ **Topic-based messaging**: Messages are organized by topics
- ✅ **Multiple publishers and subscribers**: Support for concurrent clients
- ✅ **Thread-safe operations**: Safe handling of multiple client connections
- ✅ **Real-time message broadcasting**: Instant delivery to all topic subscribers
- ✅ **Server monitoring**: Built-in status commands for monitoring active connections
- ✅ **Graceful termination**: Clean shutdown mechanisms

## Files
- `server.py`: Pub-Sub server with topic management
- `client.py`: Universal client that can act as publisher or subscriber
- `README.md`: This documentation file
- `task3.mkv`: Video demonstration of the system

## Usage

### Starting the Server
```bash
python server.py
```
The server will start listening on `localhost:8071` and display available commands.

**Server Commands:**
- `status`: Shows active subscribers by topic
- `exit`: Gracefully shuts down the server

### Running a Publisher
```bash
python client.py <server_ip> <port> PUBLISHER <TOPIC>
```

Example:
```bash
python client.py localhost 8071 PUBLISHER SPORTS
```

### Running a Subscriber
```bash
python client.py <server_ip> <port> SUBSCRIBER <TOPIC>
```

Example:
```bash
python client.py localhost 8071 SUBSCRIBER SPORTS
```

## Example Workflow

1. **Start the server:**
   ```bash
   python server.py
   ```

2. **Start a subscriber for SPORTS topic:**
   ```bash
   python client.py localhost 8071 SUBSCRIBER SPORTS
   ```

3. **Start another subscriber for NEWS topic:**
   ```bash
   python client.py localhost 8071 SUBSCRIBER NEWS
   ```

4. **Start a publisher for SPORTS topic:**
   ```bash
   python client.py localhost 8071 PUBLISHER SPORTS
   ```

5. **Send messages from the publisher:**
   ```
   PUB: Basketball game tonight!
   PUB: Final score: 105-98
   ```

6. **Subscribers will receive:**
   ```
   Server: [SPORTS] ('127.0.0.1', 54321): Basketball game tonight!
   Server: [SPORTS] ('127.0.0.1', 54321): Final score: 105-98
   ```

## Message Format
- **Publisher to Server**: Raw message text
- **Server to Subscribers**: `[TOPIC] (publisher_address): message`

## Topic Management
- Topics are created automatically when first accessed
- Each topic maintains its own list of subscribers
- Messages are only delivered to subscribers of the specific topic
- Topics are case-sensitive (converted to uppercase)

## Termination
- **Publishers**: Type `terminate` to disconnect
- **Subscribers**: Use Ctrl+C to disconnect
- **Server**: Type `exit` in server console

## Technical Details
- **Protocol**: TCP sockets
- **Threading**: Multi-threaded server handling concurrent clients
- **Synchronization**: Thread locks for safe topic management
- **Error Handling**: Automatic cleanup of disconnected clients
- **Port**: Default 8071 (configurable in server.py)

## Network Protocol
1. **Client Connection**: Client connects to server
2. **Role Declaration**: Client sends `{role}:{topic}` (e.g., "pub:SPORTS")
3. **Message Flow**:
   - Publishers send messages directly
   - Server broadcasts to all topic subscribers
   - Subscribers receive formatted messages

## Improvements in Task 3
Compared to basic pub-sub systems, this implementation adds:
- **Topic isolation**: Messages are only sent to relevant subscribers
- **Better organization**: Multiple conversation channels
- **Scalability**: Easy to add new topics dynamically
- **Enhanced monitoring**: Server can track activity per topic
