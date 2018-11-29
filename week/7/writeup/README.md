Writeup 7 - Forensics I
======

Name: Yared Tsehaye
Section: 0202

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Yared T.

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
i found two flags.
1 was found by running strings on it. image flag1 is attached that details the commands and the flag returned. 
i found the second flag when i used binwalk to see what else the file has. I used the command 
binwalk -D 'png image:png' image
to extract the embedded png image. I have attached the image extracted as a png file. 

CMSC389R--{look_I_f0und_a_strlng}
CMSC389R--{abr@cadabra}

### Part 2 (55 pts)
This was more challanging than the first part. i first ran 

#### file binary 

to see what kind of file it is. i then got the result that it is a 64 bit ELF executable linux file. it then executed

#### ./binary

which output where is your flag?.  I ran binwalk and strings on the binary file to no avail. i then used gdb and set a breakpoint on main to see how it WAS executing. I have attached an image of the disassembled binary. i saw that it was trying to access a file called .stego in /tmp. I went to that directory and located the hidden file. i opened the file using hexedit and saw that the magic byte was a signature similar to a jpeg file but not quite. I changed it to match a jpeg file starting with FFD8  and changed the whole byte. i was presented with a picture of a stegaurus. its size is 220x160 pixels. I ran 

#### binwalk .stego 

and i was presented with only one file containing jpeg image data, thumbnail 72x0. The image width is 220 but the thumbnail width is only 72. The next step i took was to run steghide extract on the image to see if there was a hidden message embedded in there. I was presented with a prompt to enter the passphrase. i first ran it with an empty password passed to it and it returned that there was nothing with that passphrase. I tried to analyze the .stego file. I ran

#### file .stego 
#### strings .stego

and i didnt recieve a whole lot of useful information. i used exiftool to extract the thumbnail in the image to see if there was something

#### exiftool -b -ThumbnailImage .stego > thumbnail.jpg

but it was the same image. I also made sure to check that the file had the same signature of FFD9 at the end. since it is a jpeg file. 
I then tried different combination of passwords based on what i found including dinosaur, pokemon variations of stegosaurus, and the name of the dinosaur on the picture as well. The first password i tried was stegosaurus, but i spelled it wrong and had to do a lot of extra work instead of getting the flag right then. when i ran 

#### steghide extract -sf .stego 
#### Enter passphrase: stegosaurus
#### Warning: unknown JFIF revision number 0.01
#### wrote extracted data to "flag".

#### cat flag 
#### Congrats! Your flag is: CMSC389R-{dropping_files_is_fun}

I have attached a screenshot image that details the process. 




