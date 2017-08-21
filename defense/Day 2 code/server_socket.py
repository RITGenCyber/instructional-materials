import sys
import socket

def http_server(ip, port, name):
	http_head = "HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n"
	http_message = "<i>Hello, this server is owned by</i> <b>" + name + "</b>\n"
	http_length = "Content-Length: " + str(len(http_message)) + "\n\n"
	http_end = "" 	

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((ip, port))
	sock.listen(5)
	while True:
		clientsocket, clientinfo = sock.accept()
		clientsocket.recv(1024)
		clientsocket.send(http_head + http_length + http_message + http_end)
		clientsocket.close()
		print_client(clientinfo)

	


def print_client(clientinfo):
	print "********** Request Received **********"
	print "IP: " + clientinfo[0] + " Port: " + str(clientinfo[1])
	
ip = sys.argv[1]
port = int(sys.argv[2])
name = sys.argv[3]

http_server(ip, port, name)

