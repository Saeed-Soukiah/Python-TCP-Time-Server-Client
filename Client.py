import socket

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
host = socket.gethostname()
port = 12345
s.connect((host, port))

# Receive data BEFORE closing the socket
data = s.recv(1024)
print(data.decode('ascii'))

# Close the socket after communication is done
s.close()