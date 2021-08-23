#Francisco :)
#This is just a templet and not the full code
import os #This module provides a portable way of using operating sysitem functionality
#import urllib.request  #module defines functions and classes which help in opening URLs(mostly HTTP) in a complex world - basic and digest authentication, redirections, cookies, and more
import socket
from datetime import datetime
#The list below stores the host name for the printer in the fifth floor
fifthFloorHostName = ["-c1 inputHostNameHere", "-c1 inputHostNameHere","-c1 inputHostNameHere", "-c1 inputHostNameHere","-c1 inputHostNameHere", "-c1 inputHostNameHere ", "-c1 inputHostNameHere", "-c1 inputHostNameHere","-c1 inputHostNameHere", "-c1 inputHostNameHere "]
#[527[0],524[1],514[2], 510[3],508[4],507[5],506[6],505[7],504[8], 521[9]]


print('Hello this program will test to see which printer is connected or not')
print ('Program running...')
print('Please wait...')

Rm527 = os.system("ping " + fifthFloorHostName[0])
Rm524 = os.system("ping " + fifthFloorHostName[1])
Rm514 = os.system("ping " + fifthFloorHostName[2])
Rm510 = os.system("ping " + fifthFloorHostName[3])
Rm508 = os.system("ping " + fifthFloorHostName[4])
Rm507 = os.system("ping " + fifthFloorHostName[5])
Rm506 = os.system("ping " + fifthFloorHostName[6])
Rm505 = os.system("ping " + fifthFloorHostName[7])
Rm504 = os.system("ping " + fifthFloorHostName[8])
Rm521 = os.system("ping " + fifthFloorHostName[9])
print('5th floor complete')
#add rest of room here

print('4th floor just got done')

print('So now we done with the 3rd floor')

print('2nd fl all done')


#step two is to display the result of the ping result. 0 means that the phost is connected to the network
def fifthFloor():
    print ('___________________________')
    print ('5th floor results below:')
    
    if Rm527 == 0:
        print ('Room 527 Lexmark ms 510 is up')
    else:
        print ('Room 527 Lexmark ms 510 down')
        
    if Rm524 == 0:
        print ('Room 524 Lexmark ms 510 is up')
    else:
        print ('Room 524 Lexmark ms 510 down')
        
    if Rm521 == 0:
        print ('Room 521 Lexmark ms 510 is up')
    else:
        print ('Room 521 Lexmark ms 510 down')
    
    if Rm514 == 0:
        print ('Room 514 Lexmark ms 510 is up')
    else:
        print ('Room 514 Lexmark ms 510 down')
    
    if Rm510 == 0:
        print ('Room 510 Lexmark ms 510 is up')
    else:
        print ('Room 510 Lexmark ms 510 down')
    
    if Rm508 == 0:
        print ('Room 508 Lexmark ms 510 is up')
    else:
        print ('Room 508 Lexmark ms 510 down')
    
    if Rm507 == 0:
        print ('Room 507 Lexmark ms 510 is up')
    else:
        print ('Room 507 Lexmark ms 510 down')
        
    if Rm506 == 0:
        print ('Room 506 Lexmark ms 510 is up')
    else:
        print ('Room 506 Lexmark ms 510 down')
        
    if Rm505 == 0:
        print ('Room 505 Lexmark ms 510 is up')
    else:
        print ('Room 505 Lexmark ms 510 down')
        
    if Rm504 == 0:
        print ('Room 504 Lexmark ms 510 is up')
    else:
        print ('Room 504 Lexmark ms 510 down')

def fourthFloor():
    print ('___________________________')
    print ('4th floor results below:')
    
    

def thirdFloor():
    print ('___________________________')
    print ('3rd floor results below:')
   
def secondFloor():
    print ('___________________________')
    print ('2nd floor results below:')
    

        


    

def main():
    
    fifthFloor()
    fourthFloor()
    thirdFloor()
    secondFloor()
    
    today = datetime.today()
    print('\nTimestamp:', today)
   

main()
