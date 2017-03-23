#-*- coding: utf-8 -*-
# qpy: 2
# qpy: console

import nmap
import shodan
import socket
import requests
import scrap02
import sshM

#Funcion principal

def nmapM(x):
    es_web = False
    es_ssh = False
    ports = (80, 8080, 443, 10000)
    lista = []
    ip = x
    nm = nmap.PortScanner()
    result = nm.scan(arguments="-sV -A %s " %(ip))
    for i in result['scan']:
        if i == "127.0.0.1":
            continue
        print " "
        print "#" * 25
        print "[+]" + str(i)
        print "#" * 25
        print "-" * 25
        try:
            print result['scan'][i]['vendor']
        except:
            pass
        try:
            for a in result['scan'][i]['tcp']:
                lista.append(a)
#comprobar si es server web paso 1:
                if int(a) == 80 or a == 8080 or a == 443 or a == 10000:
                    es_web = True
                if int(a) == 22:
                    es_ssh = True
                print "-" * 20
                print "  -----Puerto: " + str(a) + "---------"
                print "-" * 20
                try:
                    for b in result['scan'][i]['tcp'][a]:
                        print "    " + str(b) + "  :  " + str(result['scan'][i]['tcp'][a][b])
                except:
                    pass
        except:
            print "hmmm... no detecto puertos"
            pass
        try:
            for c in result['scan'][i]['portused']:
                print "Otro puerto: "
                print c
        except:
            pass
        try:
            print ("-") * 25
            print "Los puertos detectados por nmap son: "
            print lista
        except:
            pass
#Segundo paso en comprobacion web... una peticion options a los posibles puertos
        if es_ssh == True:
            print 'Detectado ssh, comenzando ataque de fuerza bruta'
            sshM.brute(ip)
        if es_web == True:
            print "=" * 35
            print "Vaya, unos puertos interesantes..."
            print "A ver que opina de http options..."
            for i in ports:
                try:
                    re = requests.options("http://%s:%i" % (ip, i))
                    print "En el puerto: %i" % i
                    print "Opciones http: " + re.headers['Allow']
                    re = requests.get("http://%s:%i" % (ip, i))
                    if re.status_code == 200:
                        print 'Realizando scraping'
                        ejec = scrap02.scraping("http://%s:%i" % (ip, i))
                        ejec.req()
                        ejec.texto()
                except:
                    pass
            print "Pos es lo que hay..."
            print "=" * 35
        else:
            pass
        es_web = False
        lista = []
#Info por parte de shodan
    print "-" * 100
    print "Informacion por shodan: "
    print "-" * 100
    try:
        sks = "COzlDXt75lpES3mTKxqziflaXaxvMUFO"
        sak = shodan.Shodan(sks)
        try:
            y = socket.gethostbyname(x)
            print "ip: " + y
            results = sak.host(y)
        except:
            print "vale un es una URL valida"
            print "probando por IP"
            results = sak.host(x)
        print "puertos abiertos: "
        print results['ports']
        print "tags: %s" % results["tags"]
        for i in results["hostnames"]:
            print "hostname: %s" % i
        print "isp: %s" % results["isp"]
        print "os: %s" % results['os']
        print "organizacion: : %s" % results['org']
        print "ASN: %s" % results['asn']
    except shodan.APIError, e:
        print "Error: %s" % e
