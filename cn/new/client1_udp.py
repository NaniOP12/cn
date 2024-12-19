import socket

def send_message_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12346)

    try:
        while True:
            message = input("Enter a message: ")
            client.sendto(message.encode('utf-8'), server_address)
            if message.lower() == 'exit':
                print("Closing connection.")
                break
            response, _ = client.recvfrom(1024)
            print(f"Server Response: {response.decode('utf-8')}")
    finally:
        client.close()

if __name__ == "__main__":
    send_message_to_server()

