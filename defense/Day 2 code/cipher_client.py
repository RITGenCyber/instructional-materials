import sys
import socket

if len(sys.argv) != 4:
	print sys.argv[0] + " IP-Address Port Filename"
	sys.exit(1)

ip = sys.argv[1]
port = int(sys.argv[2])
file = sys.argv[3]

def read_cipher(filename):
	cipher_encrypt = dict()
	cipher_decrypt = dict()
	cipherfile = open(filename)
	for line in cipherfile:
		letter1 = line[0]
		letter2 = line[2]
		cipher_encrypt[letter1] = letter2
		cipher_decrypt[letter2] = letter1
	return cipher_encrypt, cipher_decrypt

def encrypt(plaintext, cipher_enc):
	ciphertext = ""
	for letter in plaintext:
		if letter in cipher_enc:	
			ciphertext  = ciphertext + cipher_enc[letter]
		else:
			ciphertext = ciphertext + letter

	return ciphertext

def decrypt(ciphertext, cipher_dec):
	plain = ""
	for letter in ciphertext:
		if letter in cipher_dec:	
			plain  = plain + cipher_dec[letter]
		else:
			plain = plain + letter

	return plain


def client(ip, port, cipher_enc, cipher_dec):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((ip, port))
	while True:
		print "****** Enter your message: "
		msg = raw_input()
		if msg != "QUIT":
			ct = encrypt(msg, cipher_enc)
			sock.send(ct)
			ct = sock.recv(1024)
			pt = decrypt(ct, cipher_dec)
			print "****** Message from " + ip
			print(pt)
		else:
			sock.close()
			break


cipher_encrypt, cipher_decrypt = read_cipher(file)
client(ip, port, cipher_encrypt, cipher_decrypt)

