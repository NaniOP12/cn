import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(('localhost',1234))

while 1:
	query = input("Enter Message :")
	client_socket.send(query.encode())
	print(client_socket.recv(1024).decode())

client_socket.disconnect()
	
