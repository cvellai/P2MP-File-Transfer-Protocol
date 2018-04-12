import os
import platform

OS = platform.system() 

wd = os.getcwd()
if OS == "Windows":
    directory = wd + "\IP_Project2"
else:
    directory = wd + "/IP_Project2"
if not os.path.exists(directory):
    os.makedirs(directory)
os.chdir(directory)

fptr = open("Timer.txt","w+")
fptr.write("\nFile Size(Bytes)\tNumOfReceivers\tMSS(Bytes)\tFile Transfer Time(sec)")
fptr.close()
