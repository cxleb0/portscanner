import sys
import socket
import ipaddress #imported ipaddress model so we can use the ipaddress.ip_address(address) to validate our IP
from datetime import datetime
#import pyfiglet
#banner = pyfiglet.figlet_format("NMAP SCANNER")
#print(banner)

portmin = 0
portmax = 65535 #max number of ports
openports = []

#Error Handling for values entered for range of ports to scan
while True: #loop to ensure sure we get parameters that are only integers(beginning of range) + initalization of begin variable
    try:
        begin = int(input("Enter the beginning of the range of addresses you want to scan: ")) 
        break  # Exit the loop if a valid integer is entered
    except ValueError: #using ValueError because if conversion to int failed, we execute the print statement
        print("Invalid parameter. Please enter a valid integer.")

while True: #loop to ensure that range entered is greater than portmin
    if(begin >= portmin): #if valid range is entered, we continue to asking for target IP
        break
    else: #else if invalid range is entered, tell the user and prompt them for the end range value again
        print("Invalid range. The 'begin' value cannot be less than 0. Try again.")
        begin = int(input("Enter the begin of the range of addresses you want to scan: "))

while True: #loop to ensure we get parameters that are only integers(end of range) + initialization of end variable
    try:
        end = int(input("Enter the end of the range of addresses you want to scan: "))
        break # Exit the loop if a valid integer is entered
    except ValueError: #using ValueError because if conversion to int failed, we execute the print statement
        print("Invalid parameter. Please enter a valid integer.")

while True: #loop to ensure that a valid range is entered(i.e. our end value has to be >= our begin value)
    if(end >= begin): #if valid range is entered, we continue to asking for target IP. end value can be = to begin value because that is how we will only scan one port.
        break
    else: #else if invalid range is entered, tell the user and prompt them for the end range value again
        print("Invalid range. The 'end' value cannot be less than the 'begin' value. Try again.")
        end = int(input("Enter the end of the range of addresses you want to scan: "))

while True: #loop to ensure paramater is not entered that is greater than portmax
    if(begin > portmax):
        print("Range exceeded max range for valid port range. Try again.")
        begin = int(input("Enter the begin of the range of addresses you want to scan: "))
    elif(end > portmax):
        print("Range exceeded max range for valid port range. Try again.")
        end = int(input("Enter the end of the range of addresses you want to scan: "))
    else:
        break



#Error handling on the validity of the IP address
while True: #loop to ensure that the IP address that is entered is valid
    targetip = input(str("Enter the IP you would like to run a nmap scan on: "))
    try:
        validip = ipaddress.ip_address(targetip) #using ipaddress model, takes our entered ip address and checks if it is valid
        print("IP address is valid.") #will only execute if the ip address that is entered is valid
        break
    except:
        print("You entered an invalid IP address. Try again.")

print("-" * 50)
print("scanning IP:" + targetip)
print("scanning started at: " + str(datetime.now()))
print("-" * 50)

for port in range(portmin, portmax+1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((targetip, port))
            openports.append(port)
            result = s.connect_ex((targetip, port))
            if result == 0:
                print("[*] Port {} is open".format(port))
    except:
        pass    

