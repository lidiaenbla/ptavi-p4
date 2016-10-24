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
    EXPIRES = sys.argv[5]
except IndexError:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")
if REGISTER == "register":
    if DIR.split('@'):
        SIP = "sip:" + DIR + " SIP/2.0\r\n"
        print(EXPIRES)
        LINE = "REGISTER " + SIP + "Expires: " + EXPIRES + "\r\n"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
