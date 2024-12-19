import socket
import math

def start_udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('localhost', 12346))
    print("UDP Server listening on port 12346...")

    while True:
        data, addr = server.recvfrom(1024)
        number = data.decode('utf-8')

        if number.lower() == 'exit':
            print("Client requested to close the connection.")
            break

        try:
            number = int(number)
            if number < 0:
                result = "Factorial is not defined for negative numbers."
            else:
                result = math.factorial(number)
        except ValueError:
            result = "Invalid input. Please enter a valid number."
        server.sendto(str(result).encode('utf-8'), addr)

    server.close()

if __name__ == "__main__":
    start_udp_server()

