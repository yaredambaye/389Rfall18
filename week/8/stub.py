#!/usr/bin/env python2
#JORDAN BERNI
import sys
import struct
from datetime import datetime

MAGIC = 0xdeadbeef
PNGMAGIC = (0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a)
VERSION = 1

def bork(msg):
    sys.exit(msg)

def parse():
    indx = 4 + 4 + 4 + 8 + 4
    magic, version, unixtstamp, authorRaw, scount = struct.unpack("<LLLQL", data[0:indx])

    if magic != MAGIC:
        bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

    if version != VERSION:
        bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

    tstamp = datetime.fromtimestamp(unixtstamp)
    if tstamp >= datetime.today(): 
        bork("Bad timestamp! %d is before current time" % (tstamp))

    authorHex = hex(authorRaw)[2:]
    try:
        author = authorHex.decode('hex')[::-1]
    except TypeError:
        bork("Bad author! %s is not a valid ascii encoded string" % authorHex)

    if scount < 1:
        bork("Bad number of sections! Number of sections must be greater than 0 (not %d)" % scount)

    print("------- HEADER -------")
    print("MAGIC: %s" % hex(magic))
    print("VERSION: %d" % version)
    print("TIMESTAMP: %s" % tstamp)
    print("AUTHOR: %s" % author)
    print("SECTION COUNT: %d" % scount)

    print("\n-------  BODY  -------")

    for sNum in range(0, 11):
        indx = formatSection(sNum, indx, scount)
        print("")

def formatSection(sNum, i, scount):
    sType, sLen = struct.unpack("<LL", data[i:i+8])
    i = i + 8

    print("----  SECTION  %d  ----" % sNum)
    print("TYPE: %d" % sType)
    print("LENGTH: %d" % sLen)
    
    if sLen <= 0:
        return i

    if sType == 9:
        sValue = struct.unpack("%ds" % sLen, data[i:i+sLen])
        
    elif sType == 3:
        sValue = struct.unpack("%ds" % sLen, data[i:i+sLen])

    elif sType == 5:
        v = struct.unpack("<%dL" % (sLen/4), data[i:i+sLen])
        sValue = []
        for j in range(0,(sLen/4)):
            sValue.append(v[j])

    elif sType == 2:
        v = struct.unpack("<%dQ" % (sLen/8), data[i:i+sLen])
        sValue = []
        for j in range(0,(sLen/8)):
            sValue.append(v[j])

    elif sType == 4:
        sValue = struct.unpack("%ds" % sLen, data[i:i+sLen]) 

    elif sType == 6:
        if sLen != 16:
            bork("Bad section length! Section 6 must have a length of 16 not %d" % sLen)
        v1, v2 = struct.unpack("<dd", data[i:i+sLen])
        sValue = str(v1) + ", " + str(v2)

    elif sType == 7:
        if sLen != 4:
            bork("Bad section length! Section 7 must have a length of 4 not %d" % sLen)
        sValue, = struct.unpack("<L", data[i:i+sLen])
        if sValue < 0 or sValue > scount-1:
            bork("Bad section reference! %d is out of range (0 - %d)" % (sValue, scount-1))

    elif sType == 1:
        sValue = struct.unpack("%dB" % sLen, data[i:i+sLen])
        i = i + sLen
        pngFile = PNGMAGIC + sValue
        outFile = open(sys.argv[1] + ".png","w")
        outFile.write(struct.pack( "<%dB"  % len(pngFile), *pngFile))
        outFile.close()
        return i

    else:
        bork("Bad section type! %d is not a valid section type" % sType)

    print("VALUE: %s" % sValue)
    i = i + sLen
    return i
    
if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.rcff")

with open(sys.argv[1], 'rb') as rcff:
    data = rcff.read()

parse()