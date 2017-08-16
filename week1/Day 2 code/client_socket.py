import sys
import socket

if len(sys.argv) != 3:
	print sys.argv[0] + " IP-Address Port"
	sys.exit(1)

def http_client(ip, port):
	http_request = "GET / HTTP/1.1\r\n\r\n"
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((ip, port))
	sock.send(http_request)
	response = sock.recv(1024)
	sock.close()
	return response


def print_response(resp):
	print "********** RESPONSE **********"
	print resp
	print "******* RESPONSE LENGTH ******"
	print len(resp)

ip = sys.argv[1]
port = int(sys.argv[2])

print_response(http_client(ip, port))
