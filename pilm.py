#-*- uncoding:utf-8 -*-

from PIL.ExifTags import TAGS
from PIL import Image

def pilM(x):
    try:
        imgF = Image.open(x)
        info = imgF._getexif()
        print info
    except:
        print "archivo no encontrado"
