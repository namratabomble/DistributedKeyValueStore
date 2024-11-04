Distributed Key-Value Store
A simplified, distributed key-value store implemented with Python and Flask, designed to demonstrate concepts of scalable and fault-tolerant storage across multiple nodes. This project showcases skills in data partitioning, hashing, inter-node communication, and basic data replication to maintain availability.

Project Overview


Partitions data using hashing to distribute key-value pairs across multiple nodes.
Enables inter-node communication with HTTP, allowing nodes to forward requests when needed.
Implements basic replication to improve fault tolerance and ensure data availability during node failures.

### Features

Distributed Data Storage: Each node stores a subset of the data, allowing horizontal scaling.
Hashing-Based Partitioning: A hash function assigns each key to a specific node.
Inter-Node Request Forwarding: Requests for data stored on other nodes are forwarded automatically.
Data Replication (optional): Basic replication across nodes provides resilience against node failures.

### Tech Stack
Python
Flask - for REST API and server setup
REST API
HTTP - for inter-node communication
Hashlib - for hashing-based data partitioning
Requests - for forwarding HTTP requests between nodes
JSON - for data formatting
Getting Started
Prerequisites
Python 3.6 or later
Virtual environment (recommended for package management)
