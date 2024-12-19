import socket

def send_number_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    try:
        while True:
            number = input("Enter a number:")
            if number.lower() == 'exit':
                print("Closing connection.")
                break
            client.send(number.encode('utf-8'))
            response = client.recv(1024).decode('utf-8')
            print(f"Server Response: {response}")
    
    finally:
        client.close()

if __name__ == "__main__":
    send_number_to_server()

