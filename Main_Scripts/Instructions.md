
INTERNET PROTOCOLS (ECE 573)

----------------------------------------------------------------------------------------------
Instructions to run the code:
----------------------------------------------------------------------------------------------

• There are totally three python files that must be run. One named FTPServer.py for the Servers, the other named Client_FTP.py for the Client and lastly, the Init.py for initializing   the ‘Timer.txt’ file at the client side.

• Environment used for testing: Windows 7 Platform

• Make sure that the file to be transferred by the client is in the current working directory (for example C:\Python27).

• Run the Init.py file at the client side first, so that a text file ‘Timer.txt’ is created which stores the File transfer time for all the iterations which is to be run.

• Prompt to be entered at the client:
  p2mpclient server-1-ip server-2-ip server-3-ip server-port# file-name MSS

• Prompt to be entered at the server:
  p2mpserver port# file-name p

• First run the server code and enter the prompt for invoking the server, then run the client code (after executing Init.py) and enter the prompt to invoke the clienst.

• The file sent by the client will be stored in a folder named IP_Project2 in the current working directory at the receivers’ side. The time taken for the transfer will be stored at the client side in Timer.txt within the folder named IP_Project2 in the current working directory.