#!/usr/bin/python3
import socket
import subprocess
import sys


IP= input("Please enter IP address: ")
max_port = input("please enter how many ports to scan: ")


print ("-" * 60)
print ("Scanning: " + IP)
print ("-" * 60)
open_ports = []


try:
    for port in range(1,int(max_port)):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((IP, port))
        if result == 0:
            print ("Port {}:    Open".format(port))
            open_ports.append(port)
        sock.close()
except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ("Hostname couldn't' be resolved. Exitin")
    sys.exit()
except socket.error:
    print ("Could't connect to server")
    sys.exit()





print ("Scanning Completed! ")
open_ports_string= str(open_ports)
print ("Open ports: " + open_ports_string)
