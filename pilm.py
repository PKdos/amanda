#-*- uncoding:utf-8 -*-

from PIL.ExifTags import TAGS
from PIL import Image

obje = '/tmp/amanda/proba2/imagenes/amhh-white.png'

def pilM(x):
    try:
        imgF = Image.open(x)
        info = imgF._getexif()
        print info
    except:
        print "archivo no encontrado"
pilM(obje)