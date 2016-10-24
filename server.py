#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import time
import json
import sys

dicc_cliente = {}
clientes = []


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    dicc_cliente = {}

    def register2json(self):
        """
        Actualizar fichero json con los datos del dicc
        """
        fichJson = open('registered.json', 'w')
        json.dump(self.dicc_cliente, fichJson)

    def json2registered(self):
        """
        comprobar si existe el fichero .json
        """
        try:
            open('registered.json', 'r')
            print("existe el fichero")
        except:
            print("NO existe el fichero")
            pass

    def comprobarExpires(self):
        """
        Comprobar si ha expirado un cliente
        """
        deleteList = []
        horaActual = time.gmtime(time.time())
        for cliente in self.dicc_cliente:
            if time.strptime(self.dicc_cliente[cliente][1], '%Y-%m-%d %H:%M:%S') <= horaActual:
                deleteList.append(cliente)
                print("cliente borrado", cliente)
        for i in deleteList:
            del self.dicc_cliente[i]

    def Register(self, ip, sip, expires):
        """
        Registrar a clientes en el diccionario
        """
        self.comprobarExpires()
        self.dicc_cliente[sip[4:]] = [ip, expires]
        self.json2registered()
        self.register2json()
        print(self.dicc_cliente)

    def handle(self):
        """
        Manejador
        """
        sip = []
        IP = str(self.client_address[0])
        Port = str(self.client_address[1])
        print("IP:" + IP + "\nPort:" + Port)
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        line = self.rfile.read()
        print("El cliente nos manda ", line.decode('utf-8'))
        linea = line.decode('utf-8').split()
        sip = linea[1]
        expires = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + float(linea[4])))
        self.Register(IP, sip, expires)


if __name__ == "__main__":

    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
