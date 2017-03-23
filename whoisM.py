# -*- encoding: utf-8 -*-

import pythonwhois
import dns
import dns.query
import dns.resolver
import dns.zone

def dec():
    print "=" * 20

def whois(x):
    whois = pythonwhois.get_whois(x)
    dec()
    print "Datos whois:"
    dec()
    for key in whois.keys():
        print "[+] %s : %s \n" %(key, whois[key])
    dec()
    print "Datos DNS:"
    dec()
    try:
        ansA=(dns.resolver.query(x,'A'))
        print ansA.response.to_text()
        dec()
    except:
        print "fallo A"
        dec()
    try:
        ansM=(dns.resolver.query(x,'MX'))
        print ansM.response.to_text()
        dec()
    except:
        print "fallo MX"
        dec()
    try:
        ansN=(dns.resolver.query(x,'NS'))
        print ansN.response.to_text()
        dec()
    except:
        print "fallo NS"
        dec()
    try:
        ansAA=(dns.resolver.query(x,'AAAA'))
        print ansAA.response.to_text()
        dec()
    except:
        print "fallo AAAA"
        dec()
    dec()