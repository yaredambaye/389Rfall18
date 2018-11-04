Writeup 7 - Forensics I
======

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 7 writeup

### Part 1 (40 pts)

1.	What kind of file is it?
It is a JPEG file. I opened the file first with a text editor and I got a dump. I have attached an image that has the number at the front. I used this https://www.garykessler.net/library/file_sigs.html website to check what kind of file it is. It begins with FF D8 so it is a JPEG file.
2.	Where was this photo taken? Provide a city, state and the name of the building in your answer.
It was takin in Chicago Illinois at john hancock observatory (360Chicago) building.
3.	When was this photo taken? Provide a timestamp in your answer.
 2018:08:22 11:33:24.
4.	What kind of camera took this photo?
Apple Iphone 8
5.	How high up was this photo taken? Provide an answer in meters.
GPSAltitude: 539.5 m
6.	Provide any found flags in this file in standard flag format.
 I found two flags in the file. one was from running strings and grep using the key word cmsc on the image file and i was able to find the first flag cmsc389-{look i found a string}. a detailed image is attached. 

 I found the second flag by running binwalk. i first noticed that there was a second image that was not jpeg attached to the file. I used the command binwalk -D 'png image:png' image
 and i was able to extract the hidden image file. when i opened the image it had the message magic bytes and the hidden flag cmsc389e-{abr@ cadabra}. The image is attached under the name 248F20.png.

### Part 2 (55 pts)

*SUBMIT YOUR WRITEUP DETAILING YOUR APPROACH AND SOLUTION TO THIS PROBLEM HERE (>250 words). Dont forget to include the flag!*
