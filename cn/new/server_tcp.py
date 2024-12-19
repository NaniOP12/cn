import socket
import math

def start_tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(1)
    print("TCP Server listening on port 12345...")
    client_socket, client_address = server.accept()
    print(f"Connection from {client_address}")
    
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')

            if not data:
                break 

            if data.lower() == 'exit':
                print("Client requested to close the connection.")
                break

            try:
                number = int(data)
                if number < 0:
                    result = "Factorial is not defined for negative numbers."
                else:
                    result = math.factorial(number)
            except ValueError:
                result = "Invalid input. Please enter a valid number."
            client_socket.send(str(result).encode('utf-8'))
    
    finally:
        client_socket.close()
        server.close()

if __name__ == "__main__":
    start_tcp_server()

