#Francisco :)
#This is just a templet and not the full code
import os #This module provides a portable way of using operating sysitem functionality
#import urllib.request  #module defines functions and classes which help in opening URLs(mostly HTTP) in a complex world - basic and digest authentication, redirections, cookies, and more
import socket
from datetime import datetime
#The list below stores the host name for the printer in the fifth floor
fifthFloorHostName = ["-c1 inputHostNameHere", "-c1 inputHostNameHere","-c1 inputHostNameHere", "-c1 inputHostNameHere","-c1 inputHostNameHere", "-c1 inputHostNameHere ", "-c1 inputHostNameHere", "-c1 inputHostNameHere","-c1 inputHostNameHere", "-c1 inputHostNameHere "]
#[501[0],502[1],503[2], 504[3],505[4],506[5],507[6],508[7],509[8], 510[9]]


print('Hello this program will test to see which printer is connected or not')
print ('Program running...')
print('Please wait...')

Rm501 = os.system("ping " + fifthFloorHostName[0])
Rm502 = os.system("ping " + fifthFloorHostName[1])
Rm503 = os.system("ping " + fifthFloorHostName[2])
Rm504 = os.system("ping " + fifthFloorHostName[3])
Rm505 = os.system("ping " + fifthFloorHostName[4])
Rm506 = os.system("ping " + fifthFloorHostName[5])
Rm507 = os.system("ping " + fifthFloorHostName[6])
Rm508 = os.system("ping " + fifthFloorHostName[7])
Rm509 = os.system("ping " + fifthFloorHostName[8])
Rm510 = os.system("ping " + fifthFloorHostName[9])
print('5th floor complete')
#add 4th floor room here

print('4th floor just got done')

#now add 3rd fl here
print('So now we done with the 3rd floor')

#second fl would go here
print('2nd fl all done')


#step two is to display the result of the ping result. 0 means that the phost is connected to the network
def fifthFloor():
    print ('___________________________')
    print ('5th floor results below:')
    
    if Rm501 == 0:
        print ('Room 501 Lexmark ms 510 is up')
    else:
        print ('Room 501 Lexmark ms 510 down')
        
    if Rm502 == 0:
        print ('Room 502 Lexmark ms 510 is up')
    else:
        print ('Room 502 Lexmark ms 510 down')
        
    if Rm503 == 0:
        print ('Room 503 Lexmark ms 510 is up')
    else:
        print ('Room 503 Lexmark ms 510 down')
    
    if Rm504 == 0:
        print ('Room 504 Lexmark ms 510 is up')
    else:
        print ('Room 504 Lexmark ms 510 down')
    
    if Rm505 == 0:
        print ('Room 505 Lexmark ms 510 is up')
    else:
        print ('Room 506 Lexmark ms 510 down')
    
    if Rm506 == 0:
        print ('Room 506 Lexmark ms 510 is up')
    else:
        print ('Room 506 Lexmark ms 510 down')
    
    if Rm507 == 0:
        print ('Room 507 Lexmark ms 510 is up')
    else:
        print ('Room 507 Lexmark ms 510 down')
        
    if Rm508 == 0:
        print ('Room 508 Lexmark ms 510 is up')
    else:
        print ('Room 508 Lexmark ms 510 down')
        
   

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
