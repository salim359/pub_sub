# Middleware Architectures Assignment

## Overview
This repository contains the implementation of the Middleware Architectures Assignment (IS3108 / SCS3203) for UCSC, 2025. The assignment focuses on designing and implementing a Publish/Subscribe (Pub/Sub) middleware using client-server socket programming in Python. It consists of four tasks:

**Task 1:** Implement a client-server socket application where the client sends messages via a Command Line Interface (CLI) to the server, which displays them. The client terminates on the "terminate" keyword.

**Task 2:** Extend the application to support multiple concurrent clients, distinguishing between Publishers and Subscribers, with the server echoing Publisher messages to Subscriber clients.

**Task 3:** Add topic-based message filtering, allowing Publishers to send messages on specific topics and Subscribers to receive messages only for their subscribed topics.

**Task 4:** Propose a distributed architecture to improve availability and reliability, addressing the single point of failure in the server.

The project is developed in Python and uses CLI-based interfaces, as specified in the assignment guidelines.

### Prerequisites

* Python 3.x (tested with Python 3.12)
* A Linux, macOS, or Windows system with Python installed
* Basic understanding of running Python scripts from the command line
* A screen recording tool (e.g., OBS Studio, Kazam, or SimpleScreenRecorder) for creating screencasts for Tasks 1–3
* A diagramming tool (e.g., Draw.io, Lucidchart, or pen-and-paper) for Task 4’s architecture diagram

### Setup

- Clone the Repository:
`git clone <repository-url>`
`cd <repository-name>`

- Replace `<repository-url>` with the URL of this GitHub repository.

- Ensure Python is Installed:Verify Python 3 is installed:
`python3 --version`

- If not installed, download from python.org.


### Usage
**Task 1: Client-Server Application**

Objective: Implement a client-server socket application where the client sends CLI messages to the server, which displays them. The client terminates on "terminate".

Run the Server:<br>
`cd assignment/task1`<br>
`python3 server.py`

Expected output:<br>
`Socket created`<br>
`Server is listening localhost:<port_number>`<br>
`Connected by ('127.0.0.1', 33516)`


Run the Client:In a separate terminal:<br>
`python3 client.py 127.0.0.1 <port_number>`

Expected output:<br>
`Connected to server 127.0.0.1:<port_number>`


Test Communication:

Type messages in the client CLI (e.g., "Hello, server!") and press Enter.

Server output: <br>
`Connected to client: ('127.0.0.1', <port>)`<br>
`Message from ('127.0.0.1', <port>): Hello, server!`

Type "terminate" in the client to disconnect:Terminating client...

Server output: `Client ('127.0.0.1', <port>) disconnected`

Screencast:

Record both terminals showing message exchange and termination.
Save as task1_demo.mp4 in assignment/task1/.


**Task 2: Publishers and Subscribers**
Objective: Extend Task 1 to handle multiple concurrent clients, with clients specifying "PUBLISHER" or "SUBSCRIBER" roles. The server echoes Publisher messages to all Subscribers.

Run the Server: <br>
`cd server`<br>
`python3 server.py`

Expected output:<br>
`Server listening on port 8071...`


Run Publisher Client:<br>
`python3 client.py 127.0.0.1 8071 PUBLISHER`


Run Subscriber Client (in another terminal):<br>
`python3 client.py 127.0.0.1 8071 SUBSCRIBER`


Test Communication:

Type messages in the Publisher client CLI; they should appear on all Subscriber client CLIs.
Type "terminate" in any client to disconnect it.
Server logs connections and disconnections.


Screencast:

Record the server and multiple clients (at least one Publisher and one Subscriber) showing message exchange.
Save as task2_demo.mp4 in assignment/task2/.

**Task 3: Publishers and Subscribers Filtered on Topics/Subjects**
Objective: Extend Task 2 to include topic-based filtering, where clients specify a topic via a command-line argument, and Publishers send messages to Subscribers on the same topic.

Run the Server:
`cd assignment/task3`<br>
`python3 server.py 8000`


Run Publisher Client:<br>
`python3 client.py 127.0.0.1 8000 PUBLISHER TOPIC_A`


Run Subscriber Client:<br>
`python3 client.py 127.0.0.1 8000 SUBSCRIBER TOPIC_A`


Test Communication:

Type messages in the Publisher client CLI for TOPIC_A; they should appear only on Subscriber clients subscribed to TOPIC_A.
Test with multiple topics (e.g., TOPIC_B) to verify filtering.
Type "terminate" to disconnect clients.


Screencast:

Record the server and multiple clients (Publishers and Subscribers on different topics) showing topic-based message exchange.
Save as task3_demo.mp4 in assignment/task3/.

**Task 4: Enhance the Architecture**
Objective: Propose a distributed architecture to improve availability and reliability, addressing the single point of failure in the server. No implementation is required, only documentation.

Documentation:

See assignment/task4/architecture.md for the proposed architecture.
Includes a diagram (e.g., created with Draw.io) and a description of improvements over the single-server model.
Focuses on mitigating server failure through distributed nodes.



Note: 

Task 4 documentation is in progress. Update this section once the architecture proposal is finalized.
Troubleshooting

Address already in use: `lsof -i :8000`
`sudo kill -9 <PID>`

Or use a different port (e.g., 8001).
Connection refused:Ensure the server is running before starting clients and that IP/port match.
Firewall:For remote testing (e.g., 192.168.10.2), open the port (e.g., 8000) in your firewall:sudo ufw allow 8000


Invalid arguments:Verify command-line arguments (e.g., python3 client.py 127.0.0.1 8000 for Task 1).

### Submission

Files:

Task 1: server.py, client.py, task1_demo.mp4
Task 2: server.py, client.py, task2_demo.mp4
Task 3: server.py, client.py, task3_demo.mp4
Task 4: architecture.md (with embedded or linked diagram)
