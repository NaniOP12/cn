import socket

def start_udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('localhost', 12346))
    print("UDP Server listening on port 12346...")

    while True:
        data, addr = server.recvfrom(1024)
        message = data.decode('utf-8')
        
        if message.lower() == 'exit':
            print("Client requested to close the connection.")
            break

        print(f"Received message from {addr}: {message}")
        response = f"Message received: {message}"
        server.sendto(response.encode('utf-8'), addr)

    server.close()

if __name__ == "__main__":
    start_udp_server()

