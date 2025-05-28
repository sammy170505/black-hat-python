import socket

target_host = "127.0.0.1"
target_port = 9997

# Create a UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data
client.sendto(b"AAABBBCCC", (target_host, target_port))

# Receive some data
data, addr = client.recvfrom(4096)

# Print the response
print(data.decode('utf-8'))
# Close the socket
client.close()
# Note: UDP is connectionless, so we don't need to connect the socket
# before sending data. The server will respond to the address we sent data to.
# The server must be running and listening on the specified port for this to work.