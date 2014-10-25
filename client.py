#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import sys
import socket

SERVER = sys.argv[1]
PORT = sys.argv[2]

# Contenido que vamos a enviar
LINE = sys.argv[3]
registro = 'REGISTER sip:' + sys.argv[4] + ' SIP/1.0\r\n\r\n'
EXPIRES = 'Expires: ' + sys.argv[5]

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, int(PORT)))

if (LINE == 'register'):
	print "Enviando registro: " + registro
	expires = EXPIRES + "\r\n\r\n"
my_socket.send(registro + expires)
data = my_socket.recv(1024)

print 'Recibido -- ', data
print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
