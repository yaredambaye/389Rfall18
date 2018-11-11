#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import string

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


#Find me the sha1 hash of iCLuoFcwtc
def answer():
	count = 0
	found = 0 
	# receive some data	
	while(found==0):
		if count == 0:
			idx = 3
			count=1
		else:
			idx=1

		data = s.recv(1024)
		if("CMSC" in data):
			found = 1
			print(data)
			break		
		info = data.split("\n")
		info_line = info[idx].split(" ") 
		hash_type=info_line[3]
		hash_val=info_line[6]

		cmd="hash_object = hashlib."+hash_type+"(b\'"+hash_val+"\').hexdigest()"
		exec(cmd)	
		s.send(bytes(hash_object + "\n"))

	# close the connection
	s.close()




if __name__ == "__main__":
	answer()
