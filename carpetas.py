# -*- coding: utf-8 -*-

import os

def carpetas(n_carpeta):
    try:
        os.chdir('/tmp/%s' % n_carpeta)
    except:
        os.makedirs('/tmp/%s' % n_carpeta)
        print '[+]Carpeta %s creada en /tmp/%s' % (n_carpeta, n_carpeta)
