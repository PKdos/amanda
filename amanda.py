# -*- coding: utf-8 -*-

import sys
import geoM
import whoisM
import pilm
import pdfM
import nmapM
import carpetas
import os
help = '''
===========================================================
Trabajo fin de curso... pk2
Curso Python para pentesting
Introducir [opcion] [objetivo]
-----------------------OPCIONES----------------------------
--w Consulta whois + dns
--g Busqueda gps por ip
--help o --h para ver ayuda
--p Metadata de una imagen
--pf Metadata archivo.pdf
--nm Escaneo nmap + Shodan, fuerza bruta ssh y web scrapping
===========================================================
'''
def dec():
    print "=" * 30
"""valores externos"""
if len(sys.argv) <= 2:
    dec()
    print "Falta de argumentos validos...."
    print help
    exit()
else:
    comando = sys.argv[1]
    objetivo = sys.argv[2]

"""ejecucion de codigo"""
if __name__ == '__main__':
    carpetas.carpetas('amanda')
    carpetas.carpetas('amanda/user-pass')
    os.system('cp ./user-pass/* /tmp/amanda/user-pass')
    if comando == "--w":
        whoisM.whois(objetivo)
    elif comando == "--g":
        geoM.geoM(objetivo)
    elif comando == "--p":
        pilm.pilM(objetivo)
    elif comando == "--pf":
        pdfM.pdfM(objetivo)
    elif comando =="--nm":
        nmapM.nmapM(objetivo)
    elif comando == "--help" or comando == "-h":
        print help
    else:
        print "Sintaxis incorrecta..."
        print help
