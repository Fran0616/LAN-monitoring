
Summarry: 
===========
A host monitoring is a great tool to help monitor a Local Area Network (LAN). It works by sending an ICMP echo request to the network host. 
It automates the network troubleshooting process and makes it more efficient for a user. 

Goal:
==========
1. Automate the pinging process by adding every printer hostname into the script. 
2. Help to make network troubleshooting more efficient. 

How it works?
==================
1. The computer will send an Internet Control Message Protocol (ICMP) echo request on the network to the host and 
this will be picked up by the router.
2. The router will route the ICMP to the host, and wait for a reply.
3. If the host is available it will respond to the request and let the router know that it's available.
    a. If the host isn’t available the router will acknowledge that it received no packet back.
4. The router will send the result back to the computer letting it know if the host is up or down.

Version 1.1
==================

Goal: The goal of this update is to be able to display the printer's toner level. 

How it works?
1. The client computer sends a request to the printer HTTP server
2. The printer HTTP server sends the HTML file to the client computer.
3. The client computer split each line as a list 
4. The client computer closes the url request with the use of the close method. 
5. Next the client computer prints line 35 in the HTML file by specifying the line in the print statement 
(line to print = n +1 ) n being the argument, so if you want to print line 36 the argument will be 35.

Code templet is [here:](https://github.com/Fran0616/Fran/blob/master/.github/workflows/host_availability.py_
