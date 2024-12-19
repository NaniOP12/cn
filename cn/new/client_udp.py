import socket

def send_number_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12346)

    try:
        while True:
            number = input("Enter a number: ")
            if number.lower() == 'exit':
                print("Closing connection.")
                break
            client.sendto(number.encode('utf-8'), server_address)
            response, _ = client.recvfrom(1024)
            print(f"Server Response: {response.decode('utf-8')}")
    
    finally:
        client.close()

if __name__ == "__main__":
    send_number_to_server()

