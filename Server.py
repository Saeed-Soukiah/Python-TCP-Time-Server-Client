import socket
import time

# Create a TCP/IP socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to host and port
host = socket.gethostname() 
port = 12345
serversocket.bind((host, port))

# Listen for incoming connections
serversocket.listen(5)
print(f"Server listening on {host}:{port}")

while True:
    # Accept a connection
    clientsocket, addr = serversocket.accept()
    print(f"Got a connection from {addr[0]}:{addr[1]}")

    # Send current time
    current_time = time.ctime(time.time()) + "\r\n"
    clientsocket.send(current_time.encode('ascii'))

    # Close client socket
    clientsocket.close()