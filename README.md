# Publish-Subscribe Communication System

## Overview

This repository contains a comprehensive implementation of communication systems using Python sockets, progressing from basic client-server architecture to advanced publish-subscribe patterns with topic-based messaging.

## Project Structure

```
pub_sub/
├── task1/          # Basic Socket Client-Server Communication
├── task2/          # Publish-Subscribe System
├── task3/          # Pub-Sub with Topic Support
├── task4/          # Improvement Proposals
└── README.md       # This overview file
```

## Tasks Overview

### Task 1: Basic Socket Client-Server Communication
**Location:** `task1/`

A foundational implementation of TCP socket communication between a client and server.

**Key Features:**
- Simple TCP socket communication
- Interactive bidirectional messaging
- Multithreaded server for concurrent I/O
- Command-line argument support
- Graceful connection termination

**Files:**
- `server.py` - Socket server implementation
- `client.py` - Socket client implementation
- `README.md` - Detailed documentation
- `task1.mov` - Video demonstration

### Task 2: Publish-Subscribe System
**Location:** `task2/`

An advanced messaging system implementing the publish-subscribe pattern with a central message broker.

**Key Features:**
- Multi-client support (publishers and subscribers)
- Real-time message broadcasting
- Role-based client connections
- Concurrent connection handling
- Connection management with automatic cleanup

**Files:**
- `server.py` - Pub-Sub message broker
- `client.py` - Universal client (publisher/subscriber)
- `README.md` - Comprehensive documentation
- `task2.mkv` - Video demonstration

### Task 3: Topic-Based Pub-Sub System
**Location:** `task3/`

Enhanced publish-subscribe system with topic-based message organization and routing.

**Key Features:**
- Topic-based message routing
- Selective message subscription
- Thread-safe operations
- Server monitoring and status commands
- Organized communication channels

**Files:**
- `server.py` - Topic-aware message broker
- `client.py` - Topic-based publisher/subscriber client
- `README.md` - Implementation documentation
- `task3.mkv` - Video demonstration

### Task 4: Improvement Proposals
**Location:** `task4/`

Contains proposals and suggestions for enhancing the pub-sub system with middleware and advanced features.

**Files:**
- `improvement_proposal.pdf` - Detailed improvement suggestions and architectural enhancements

## Getting Started

### Prerequisites
- Python 3.x
- No external dependencies (uses built-in Python modules)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd pub_sub
   ```

2. **Choose a task to run:**
   - For basic client-server: `cd task1`
   - For pub-sub system: `cd task2`
   - For topic-based pub-sub: `cd task3`

3. **Follow the specific README in each task directory for detailed instructions**

## System Architecture Evolution

### Task 1: One-to-One Communication
```
Client ←→ Server
```

### Task 2: One-to-Many Broadcasting
```
Publisher₁ ─┐
Publisher₂ ─┤
Publisher₃ ─┤─→ Message Broker ─→ Subscriber₁
             │                   ├─→ Subscriber₂
             │                   └─→ Subscriber₃
```

### Task 3: Topic-Based Routing
```
Publisher₁ (Sports) ─┐
Publisher₂ (News)  ──┤
Publisher₃ (Tech)  ──┤─→ Message Broker ─→ Topic: Sports  ─→ Subscriber₁
                     │                   ├─→ Topic: News   ─→ Subscriber₂
                     │                   └─→ Topic: Tech   ─→ Subscriber₃
```

## Key Learning Outcomes

- **Socket Programming**: Understanding TCP socket communication in Python
- **Concurrent Programming**: Implementing multithreaded servers for handling multiple clients
- **Message Patterns**: Implementing publish-subscribe messaging patterns
- **System Design**: Progressing from simple client-server to complex distributed messaging systems
- **Topic Management**: Organizing and routing messages based on topics/channels

## Video Demonstrations

Each task includes a video demonstration showing the system in action:
- `task1.mov` - Basic client-server communication
- `task2.mkv` - Pub-sub system with multiple clients
- `task3.mkv` - Topic-based message routing

## Contributing

This project demonstrates the evolution of communication systems from basic socket programming to advanced messaging patterns. Each task builds upon the previous one, showing progression in complexity and functionality.

## License

This project is for educational purposes, demonstrating socket programming and messaging system implementations in Python.