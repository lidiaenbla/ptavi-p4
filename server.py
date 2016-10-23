#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver

clientes = {}

def registro(ip):
    clientes["dir"] = ip 

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    def handle(self):
        clientes = {}
        IP = str(self.client_address[0])
        Port = str(self.client_address[1])
        registro(IP)
        print("IP:" + IP + "\nPort:" + Port)
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        for line in self.rfile:
            print("El cliente nos manda ", line.decode('utf-8'))

if __name__ == "__main__":
    serv = socketserver.UDPServer(('', 6001), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
