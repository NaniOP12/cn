import socket

def send_message_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    try:
        while True:
            message = input("Enter a message: ")
            client.send(message.encode('utf-8'))
            if message.lower() == 'exit':
                print("Closing connection.")
                break
            response = client.recv(1024).decode('utf-8')
            print(f"Server Response: {response}")
    finally:
        client.close()

if __name__ == "__main__":
    send_message_to_server()

