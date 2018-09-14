OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Thursday, September 13 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `kruegster1990`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `kruegster1990` and answer the following questions:

1. What is `kruegster1990`'s real name?

Fred Krueger

2. List all personal information (including social media accounts) you can find about him. For each, briefly detail how you discovered them.

Name => Fred Krueger I found this on his csic website. my initial search was on google and this was the first
		come up.

Occupation =>  works at cornerstone airlines. => found on his twitter account linked on the csic website. his twitter a ccount also had more information including year of birth and where he lives which is in silverspring MD.

Twitter, reddit, instagram account under kruegster 1990 => All were found using osint database username checking website. i have attached images of his instagram and twitter account. 

Email=> kruegster@tutanota.com I found this when i googled cornerstone airlines. it led me to the website cornerstoneairlines.co which is under his name and email under about.


3. What is the IP address of the webserver hosting his company's site? How did you discover this?

142.93.118.186  I found this from my nmap scan of cornerstone airlines.co and using Whois search.

4. List any hidden files or directories you found on this website. Did you find any flags?

There is a hidden directory called /secret when inspecting robots.txt file. There is a flag in it. 
CMSC389R-{fly_th3_sk1es_w1th_u5}

5. Did you find any other IP addresses associated with this website? What do they link to, or where did you find them?
Yes it is the ip address of the admin website. 

142.93.117.193 i found it on cornerstoneairlines.co website under admin. 

6. If you found any associated server(s), where are they located? How did you discover this?
It is the admin server located on that ip address. i discovered this using an nmap scan.

7. Which operating system is running on the associated server(s)? How did you discover this?

Linux   

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)

CMSC389R-{dns-txt-rec0rd-ftw}   
CMSC389R-{h1dden_fl4g_in_s0urce}
CMSC389R-{fly_th3_sk1es_w1th_u5}

### Part 2

Use the provided python stub code [('stub.py')](stub.py) or write your own program in another language to gain access to the Cornerstone Airlines administrator server via an open port that you should have found in Part 1. 

Once you have gained access to the Cornerstone Airlines administrator portal with the correct login credentials, you will have access to a system shell. 

Use your knowledge of Linux and OSINT techniques to locate a specific flight record, read it, and submit the flag inside.

Your response here should briefly document how you approached and solved this part of the assignment. You should also push your bruteforce program to the "week/2/writeup" folder of your GitHub repository.

Note: If you choose to write your own program in another language, please include instructions on how to execute your program, including what version of the language you are using. You will **NOT** receive credit if the TAs cannot run your program.

If you are stuck on this part of the assignment, let us know! The facilitator staff is here to help and teach, and we are open to releasing hints as time goes on!





Once i was able to determine the admin server ip address, i used Nmap to obtain an open port.

i got a list of open ports and i tried to nc into them.

My Nmap scan yielded ports 
22
80
2222
10010
1337

open. When i executed 

nc 132.93.117.193 1337

command i was prompted with a login. I then used the stub.py program to continiually open the server and give it a username and a list of passwords to bruteforce the login. I had to find the username so i compiled a list of username possibilties which included 

kruegster1990
kruegster@tutanota.com
CORNERSTONE
cornerstoneairlies
kruegster

My brute force program was taking long. while it was running, i decided to dig deeper into fred krueger and found his instagram profile. i noticed that he had a lot of pokemon pictures so i downloaded a list of pokemon and started a scan using that file. finally, i was able to bruteforce it to find the username and password. 

Username: kruegster
Password: pokemon


i then procedded to navigate the directory using ls command because i know from my scan that this is running on linux. i went to the home/flight_records directory where there was a large collection of flight document texts. i opened one and each one has a flag inside. Since i was looking for a very specific flight i went back and looked at his profiles. I have attached an image i found on instagram of a boarding ticket which had a specific flight information on it. i then procedded to look for and open that specific flight and i found this flag.

CMSC389R-{c0rn3rstone-air-27670} 




### Format
In the "week/2/writeup" directory of our repository there is a README.md file for you to edit and submit your homework in. Use this as a template and directly edit it with your answers. Complete your bruteforce program in this directory as well. When you've finished the assignment, [Push it](https://github.com/UMD-CS-STICs/389Rfall18/blob/master/HW_Submit_Instructions.md) up to your personal GitHub for us to grade.

Your responses to every prompt in this assignment should include answers to any specific questions along with a brief explanation of your thought process and how you obtained the answer.

### Scoring

Part 1 is worth 45 points, and part 2 is worth 55 points.

### Tips

Reference the slides from lecture 2 to help you effectively utilize available OSINT techniques.
