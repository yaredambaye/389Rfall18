#!/usr/bin/env python2
#author Yared Tsehaye
import sys
import struct


def bork(msg):
    sys.exit(msg)

# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1 



if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.rcff ")

# Normally we'd parse a stream to save memory, but the RCFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as rcff:
    data = rcff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version, timestamp, author, section_count = struct.unpack("<LLL8sL", data[0:24])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

def printsections():
    print(" ------- HEADER ------- ")
    print(" MAGIC: %s" % hex(magic))
    print(" VERSION: %d" % int(version))

    # We've parsed the magic and version out for you, but you're responsible for
    # the rest of the header and the actual RCFF body. Good luck!
    print(" TIMESTAMP: " +  str(timestamp))
    print(" AUTHOR: %s" % author)
    print(" SECTION_COUNT: %d" % section_count)

    print("-------  BODY  ------- ")

    stbyte = 24 
    endbyte = stbyte + 8 
    
    for i in  range(section_count + 2):
        section_type, section_length = struct.unpack("<LL", data[stbyte:endbyte])
        section_number = i + 1
        st = endbyte     
        if section_type == 1:
            print(" SECTION_PNG ")
            

            contents = struct.unpack("%dB" % section_length, data[i:i+section_length])
            pngFile=(0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a)+contents
            outFile = open("output.png", "wb") 
            outFile.write(struct.pack( "<%dB"  % len(pngFile), *pngFile))
            outFile.close()
        elif section_type == 2:
            print(" SECTION_DWORDS ")
            contents = struct.unpack("<%dQ" % (section_length/8), data[st:st+section_length])
            print(" CONTENTS: ")
            for i in range (section_length / 8):
                print(contents[i])           
        elif section_type == 3:
            print(" SECTION_UTF8 ")
            contents = struct.unpack(str(section_length) + "s", data[st:st+section_length])
            print(" CONTENTS: %s\n" % contents)
        
        elif section_type == 4:
            print(" SECTION_DOUBLES ")
            contents = struct.unpack(str(section_length) + "s", data[st:st+section_length])
            print(" CONTENTS: %s\n" % contents)
        elif section_type == 5:
            print(" SECTION_WORDS ")
            contents = struct.unpack("<%dL" % (section_length/4), data[st:st+section_length])
            print(" CONTENTS: %s\n" % unicode(contents))
        elif section_type == 6:
            print(" SECTION_COORD ")
            cord_1 , cord_2 = struct.unpack("<dd", data[st:st+section_length])
            print(" CONTENTS: %s , %s \n" %(str(cord_1), str(cord_2)))
        elif section_type == 7:
            print(" SECTION_REFERENCE ")
            contents, = struct.unpack("<L", data[st:st+section_length])
            print(" CONTENTS: %s\n" % contents)
        elif section_type == 9:
            print(" SECTION_ASCII ")
            contents = struct.unpack(str(section_length) + "s", data[st:st+section_length])
            print(" CONTENTS: %s\n" % contents)          
        else:
            print(" INVALID ")
            sys.exit()
                
        stbyte = st+section_length 
        endbyte = stbyte + 8

if __name__ == "__main__":
    printsections()