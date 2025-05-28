import socket

target_host = 'www.google.com'
target_port = 80

# Create a socket object
#AF_INET is used for IPv4 addresses, SOCK_STREAM is used for TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# Send some data
# - "GET / HTTP/1.1" asks for the root page using HTTP 1.1
# - "Host: example.com" specifies the target domain (required in HTTP/1.1)
# - "\r\n\r\n" signals end of headers
# Must be sent as bytes, hence the b"" prefix
client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
# Receive some data
response = client.recv(4096)

# Print the response
print(response.decode('utf-8'))