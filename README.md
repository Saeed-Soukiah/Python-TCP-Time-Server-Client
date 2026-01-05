# Python TCP Time Server & Client

This repository contains a simple implementation of a **TCP server** and **TCP client** in Python.  
The server listens for incoming connections and sends the current system time to the client.  
The client connects to the server, receives the time, and prints it.

---

## 🚀 Features
- TCP/IP socket communication using Python's `socket` library
- Server sends current system time to connected clients
- Client receives and displays the time
- Lightweight and beginner-friendly example of socket programming

---

## 📂 Project Structure
```
├── Server.txt   # Python server code
├── Client.txt   # Python client code
```

---

## ⚙️ How to Run

### 1. Start the Server
```bash
python Server.txt
```
The server will start listening on `hostname:12345`.

### 2. Run the Client
```bash
python Client.txt
```
The client will connect to the server and display the current time.

---

## 🖥️ Example Output

### Server:
```
Server listening on myhostname:12345
Got a connection from 127.0.0.1:54321
```

### Client:
```
Tue Jan  6 02:17:00 2026
```

---

## 📚 Learning Goals
- Understand how TCP sockets work in Python
- Learn how to bind, listen, accept, connect, send, and receive data
- Practice client-server communication basics

---

## 🔧 Requirements
- Python 3.x
- No external dependencies (uses built-in `socket` and `time` modules)

---

## 📜 License
This project is licensed under the MIT License. Feel free to use and modify it for learning purposes.
```
