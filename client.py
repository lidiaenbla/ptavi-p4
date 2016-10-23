#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

try:
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    REGISTER = sys.argv[3]
    DIR = sys.argv[4]
except IndexError:
    sys.exit("python3 client.py ip puerto register luke@polismassa.com")
#python3 client.py ip puerto register luke@polismassa.com
if REGISTER == "register":
    if DIR.split('@'):
        SIP = "sip:" + DIR + " SIP/2.0\r\n"
        LINE = "REGISTER " + SIP

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
