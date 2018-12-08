#!/usr/bin/env python2
# from the git repo
import md5py
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> temp-branch
import time
import socket
# nc 142.93.118.186 1234

host = "142.93.118.186"
port = 1234
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

data = s.recv(1024)
print(data)
<<<<<<< HEAD
=======
=======
>>>>>>> upstream/master
>>>>>>> temp-branch

#####################################
### STEP 1: Calculate forged hash ###
#####################################

<<<<<<< HEAD
message = 'karsforkids'    # original message here
=======
<<<<<<< HEAD
message = 'karsforkids'    # original message here

s.send("1\n")
data = s.recv(1024)
print(data)

s.send(message+"\n")
data = s.recv(1024)
print(data)

legit = data[data.index("hash: ")+6:data.index("hash: ")+40].strip()      # a legit hash of secret + message goes here, obtained from signing a message
print("legit => "+legit)
=======
message = ''    # original message here
legit = ''      # a legit hash of secret + message goes here, obtained from signing a message
>>>>>>> temp-branch

s.send("1\n")
data = s.recv(1024)
print(data)

s.send(message+"\n")
data = s.recv(1024)
print(data)

<<<<<<< HEAD
legit = data[data.index("hash: ")+6:data.index("hash: ")+40].strip()      # a legit hash of secret + message goes here, obtained from signing a message
print("legit => "+legit)
=======
# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print(fake_hash)
>>>>>>> upstream/master
>>>>>>> temp-branch


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> temp-branch



# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'kars'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print(fake_hash)

# msg = 11 secret = 7, padding = 512-64-88 = 360 = 45 bytes 
# 1 1 bit and 44 0 bits
val = 34


padding = '\x80'
for i in range(val):
	padding += '\x00'

padding+='\xa8'
for i in range(7):
  padding += '\x00'
<<<<<<< HEAD
=======
=======
padding = ''
>>>>>>> upstream/master
>>>>>>> temp-branch

# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash
payload = message + padding + malicious

<<<<<<< HEAD
print("\npayload => "+repr(payload))
print("\npayload length => "+str(len(payload)))
# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!
s.send("2\n")
data = s.recv(1024)
print(data)
s.send(fake_hash + "\n")
data = s.recv(1024)
print(data)
s.send(payload + "\n")
time.sleep(0.1) #delay of 1/10 of a second to propery print out the result everytime
data = s.recv(1024)
print(data)
=======
<<<<<<< HEAD
print("\npayload => "+repr(payload))
print("\npayload length => "+str(len(payload)))
# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!
s.send("2\n")
data = s.recv(1024)
print(data)
s.send(fake_hash + "\n")
data = s.recv(1024)
print(data)
s.send(payload + "\n")
time.sleep(0.1) #delay of 1/10 of a second to propery print out the result everytime
data = s.recv(1024)
print(data)
=======
# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!
>>>>>>> upstream/master
>>>>>>> temp-branch
