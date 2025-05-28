import socket
import threading

# You don’t know in advance which interface the client
# will use to connect — 0.0.0.0 means “accept them all.”
IP = '0.0.0.0'  # Listen on all interfaces
PORT = 9998  # Port to listen on

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)  # Allow up to 5 queued connections
    print(f"Server listening on {IP}:{PORT}")

    # Server loop: handle one client at a time as they connect
    while True:
        # Accept a new connection (blocking call until a client connects)
        client_socket, addr = server.accept()

        # addr[0] = the client's IP address
        # addr[1] = the client's port number (used on their side
        print(f"Accepted connection from {addr[0]}:{addr[1]}")

        # Create a new thread to handle the client so the server can keep listening
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

def handle_client(client_socket):
    # `with` ensures socket is closed properly after use
    with client_socket as sock:
        # Receive up to 1024 bytes from the client
        request = sock.recv(1024)

        # .decode("utf-8") converts bytes to string
        print(f'[*] Received: {request.decode("utf-8")}')
        
        # Send a response back to the client
        sock.send(b'ACK')

if __name__ == "__main__":
    main()