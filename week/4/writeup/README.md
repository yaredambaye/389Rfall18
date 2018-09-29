Writeup 3 - Pentesting I
======

Name: Yared Tsehaye
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Yared Tsehaye

## Assignment 4 Writeup

### Part 1 (45 pts)
I first stated by netcatting into the server using the command nc cornerstoneairlines.co 45. I was greeted with a prompt to enter aj 
IP address. This means that Fred implemented a ping system. so, i started testing different commands to see if the script would actually run and return some information. I sent over the command 

127.0.0.1| ls /

and i was able to see the list of files under the root directory of the server. this means i was able to run scripts by simply giving an IP| my_command and it will return what i needed it to return. i then went a couple of steps looking for any hidden files. finally i ran 

127.0.0.1| cat /home/flag.txt

and i got back the contents of the file flag.txt which is 

Good! Here's your flag: CMSC389R-{p1ng_as_a_$erv1c3}

I have included a screen shot the result i obtained from running the script. 
This system is vulerable to these types of attack because of mostly bad or lazy coding. An attacker can send over scripts as inputs and when it is processed, the script will be run if it is not escaped or treated as a required input. The best way to avoid this is to check the given value and input sanitization. This implementation will check the uptime of devices connected to the service. 
### Part 2 (55 pts)
Given what i got from part one, I implmented an interactive shell that takes advantage of the aforementioned vulerability. The code works simply by using the socket library and mimicing netcat. I prompt for input and take that input to make sure the correct command is executed. for example, if i get an 
  ls /
as input, the script will put 127.0.0.1| infront of it and send it to the server and display the results obtained. i also have a
pull command that will download a txt or ascii based file from the server to the local machine. I take the command
  pull <remote-path> <local-path>
then i send 127.0.0.1| cat <remote-path> to the server and then create a local file at the specified local-path and write the results obtained to that file. it is a simple shell with limited functionality but it demonstrates the vulnerabilty. for example,
  pull /home/flag.txt /root/flag.txt
will download a copy of the file the local machine i.e flag.txt in root. i have attached a screenshot named pull that shows this example. 
