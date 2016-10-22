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
    LINELISTA = sys.argv[3:] #cogemos todo el texto
except IndexError:
    sys.exit("")

LINE = ' '.join(LINELISTA)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
