#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("probable-v2-top1575.txt", 'r')
hsh = open("hashes",'r')
salts = string.ascii_lowercase

def crack():
	hasharr = []
	for line in hsh:
		hasharr.append(line.rstrip())	
# a string equal to 'abcdefghijklmnopqrstuvwxyz'.	
	for word in wordlist:		
		for salt in salts:				
   			hshchk=hashlib.sha512(salt+word.strip()).hexdigest()  
   						
   			for val in hasharr:
   				
   				if hshchk == val:
   					print(salt +word +line.strip() + " " + "\n")




if __name__ == "__main__":
	crack()
	