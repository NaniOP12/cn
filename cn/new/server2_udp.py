import socket

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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
            if is_prime(number):
                result = f"{number} is a prime number."
            else:
                result = f"{number} is not a prime number."
        except ValueError:
            result = "Invalid input. Please enter a valid number."
        server.sendto(result.encode('utf-8'), addr)

    server.close()

if __name__ == "__main__":
    start_udp_server()

