
Writeup 9 - Crypto I
=====

<<<<<<< HEAD
Name: Yared Tsehaye	
=======
<<<<<<< HEAD
Name: Yared Tsehaye
=======
Name: Yared Tsehaye	
>>>>>>> completed assignment 10
>>>>>>> temp-branch
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Yared Tsehaye

## Assignment 9 Writeup

### Part 1 (60 Pts)

>You have recovered a few SHA512 password hashes from the Cornerstone Airlines webserver in the file hashes. You also have a gut feeling that these passwords come from this password list. We have copied over this password list into the GitHub repository for your convenience. You also have found hints on their server that each password is salted by pre-pending a single, lowercase character ('a', 'b', ..., 'z'), though you don't know if the same salt is used for each password. Your task is to write a script to bruteforce each of these hashes, and print out each of the salts and passwords found. Stub code is probided in part1.py.

I opened the word list and opened the hashes file. I then took a word from the word list then added a lowercase letter to it then checked it then converted it to sha512 with hashlib. I then used checked that against all the hashes to see if they matched. If they did, then i printed the salt and the word and the hash on a new line.
It put out the following results. 

![alt text][logo]

[logo]: https://github.com/yaredambaye/389Rfall18/blob/master/week/9/writeup/part1.PNG "part 1 results"

The words are 

mjordan 
uloveyou
kneptune
ppizza


### Part 2 (40 Pts)

>You found an interesting trivia service running on a distant computer. From my experience of highly-contrieved trivia services such as this one, I have a hunch if you can answer each of the questions, you'll get a flag in return. Stub code is provided in part2.py. nc 142.93.117.193 7331

The second part was a bit tricky. I first started out by just nc'ing to the server and using an online hasher to get the correct results. i tried to do this a few times(at least 10) by manually inputing the results, and i failed to get the flag. 

I then used python to automate this process for me. The first time i connect i get the following prompt. 

![alt text][logo]

[logo]: [logo]: https://github.com/yaredambaye/389Rfall18/blob/master/week/9/writeup/ncd.PNG
 "prompt"

The line i want to extract is the third line which begins with find me. I need to know the hash type and the word to hash. 
When i answer correctly i get the string "correct!" and then the same prompt that begins with find me on a new line. 

so I used a while loop that breaks when it finds the flag("CMSC" in the data recieved). if it is the first time, it extracts the fourth line otherwise it extracts the second line. I extract the hash type and string to hash then send back the hash. when it finally breaks, it prints the results and exits. I obtained the following when my program finished running.

![alt text][logo]

[logo]: [logo]: https://github.com/yaredambaye/389Rfall18/blob/master/week/9/writeup/part2.PNG
 "part 2 results"

