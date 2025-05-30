
# Introduction

What is offensive security?

To outsmart a hacker, you need to think like one.

This is the core of "Offensive Security". It involves breaking on into computer systems, exploiting software bugs and finding loopholes in applications to gain unauthorized acces. The goal is to understand hacker tactics and enhance our system defences.

## Beginning  Your Learning Journey

In this TryHackMe Room, you will be guided through hacking you first website in a legal and safe environment. The goal is to show you how an ethical hacker operates.

But before we do that, let's review answering question, like the next:

Which of the following options better represents the process where you simulate a hacker's actions to find vulnerabilities in a system:

Answer: Offensive Security

## Hacking you first machine

Inside the machine, you have a website (fakebank.thm). To start with hacking we made a scan inside the web to analize if exists  some directories that we can acces and do something that could be unauthorized.

For this challengue we will use **gobuster**, that is a tool to help us with the scan.
First we need to use the parameter **-u** to indicate the website, like 'gobuster -u http:google.es'.

This is a brute force attack, so we need to select a wordlist dictionary with **-w** parameter, in this case we have **wordlist.txt** and finally our command be like this:

```shell
gobuster -u http://fakebank.thm -w wordlist.txt dir 
```

If we execute this into the terminal, we initialize a scan to find directories into the web:

![[001.png]]

When the program show us some directories that was find, we need to see first the number of status and if is 200 or 201 we have acces to that directory in the page.

So, in this case we have acces to **/bank-transfer** into the web **fakebank.thm**, to enter just we add the directory to the page url 'http://fakebank:/bank-transfer'

Inside the web, the mission is made a transaction from the account 2276 to our account 8881 of $2000.

When we have made a transaction of the correct amount we will se a message that contain the answer of the exercise. In this case: