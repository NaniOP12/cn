import socket
import threading

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('localhost',1234))
server_socket.listen(5)

clients = [];


def handle(conn,_id):
	while 1:
		msg = conn.recv(1024).decode()
		for c in clients:
			if c!=conn:
				try:	
					brod_str= "User " + str(_id) +" : "+ msg
					c.send(brod_str.encode()) 
				except:	
					clients.remove(c)
	conn.close()

count = 0
while 1:
	conn,addr = server_socket.accept()
	print('New connection ' + str(addr[1]))
	count += 1
	clients.append(conn)
	threading.Thread(target = handle,args = (conn,count,)).start()


