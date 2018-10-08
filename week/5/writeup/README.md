Writeup 5 - Binaries I
======

Name: Yared Tsehaye
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Yared Tsehaye

## Assignment 5 Writeup

I put both methods into a dissasembler to figure out how it would run on an x86 system. the challenge for me was to figure out how to do it in 64 bit mode. normally x86 is associated with 32 bit systems. It wouldnt initally compile because as i said it was expecting a 32 bit move. I used the code i got as a starting point and modfied it using dword, qword and byte to make sure both moves are 64 bit registers. The most challanging bug i found was "invalid size of operand 1". it took me a while to figure this out but it was an issue that was created because of the use of mov on registers that were not equal width. 



