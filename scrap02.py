# -*- coding: utf-8 -*-

import requests
import threading
import mechanize
import carpetas
import pdfM
from bs4 import BeautifulSoup as bis

class scraping():
    def __init__(self, pagina):
        self.car = raw_input('Eliga el nombre de la carpeta: ')
        self.pagina = pagina
        self.pdf = []
        self.control = []
        self.imagenes = []
        self.sub = ''
        self.sublink = pagina
        carpetas.carpetas('amanda/%s' % self.car)
        carpetas.carpetas('amanda/%s/imagenes' % self.car)
        carpetas.carpetas('amanda/%s/pdf' % self.car)
        print 'Un poco de paciencia, la paciencia es una virtud ;)'
    def req(self):
        re = requests.get(self.sublink)
        if re.status_code == 200:
            bs = bis(re.text, 'lxml')
            self.links = bs.find_all('a')
            img = bs.find_all('img')
            for i in img:
                if i['src'] not in self.imagenes and 'http' in i['src']:
                    self.imagenes.append(i['src'])
                    threading.Thread(target=self.descarga(i['src'], 'img')).setDaemon(True)
                elif self.pagina + i['src'] not in self.imagenes and 'http' not in i['src'] and i['src'][0] == '/':
                    self.imagenes.append(self.pagina + i['src'])
                    threading.Thread(target=self.descarga(self.pagina + i['src'], 'img')).setDaemon(True)
                elif self.pagina + i['src'] not in self.imagenes and 'http' not in i['src'] and i['src'][0] != '/':
                    self.imagenes.append(self.pagina + '/' + i['src'])
                    threading.Thread(target=self.descarga(self.pagina + '/' + i['src'], 'img')).setDaemon(True)
        self.scrap1()
    def scrap1(self):
        for link in self.links:
            if hasattr(link, 'href'):
                try:
                    if ':' not in link['href'][:1] and '#' not in link['href']:
                        self.sub = ''
                        if 'http' in link['href'] and self.pagina in link['href']:
                            self.sublink = link['href']
                        elif 'http' not in link['href']:
                                if link['href'][0] == '/':
                                    self.sublink = self.pagina + link['href']
                                else:
                                    self.sublink = self.pagina + '/' + link['href']
                        elif self.sublink[-1] == '/':
                            for i in self.sublink[:-1]:
                                self.sub += i
                            self.sublink = self.sub
                            self.sub = ''
                        if '.pdf' in self.sublink and self.sublink not in self.pdf:
                            self.pdf.append(self.sublink)
                            threading.Thread(target=self.descarga(self.sublink, 'pdf')).setDaemon(True)
                        if self.sublink not in self.control:
                            self.control.append(self.sublink)
                            self.sub = ''
                            for i in self.sublink[7:]:
                                self.sub += i
                                if i == '/':
                                    sub2 = 'http://' + self.sub
                                    if sub2 not in self.control:
                                        self.control.append(sub2)
                                        try:
                                            self.sublink = sub2
                                            self.req()
                                        except:
                                            continue
                            try:
                                self.req()
                            except:
                                continue
                except:
                    continue
    def descarga(self, archivo, ext):
        self.archivo = archivo
        self.ext = ext
        bro = mechanize.Browser()
        nom = self.archivo
        nombre = nom.lower().rsplit('/', 1)[-1]
        if self.ext == 'pdf':
            try:
                dire = '/tmp/amanda/%s/pdf/%s' % (self.car, nombre)
                bro.retrieve(self.archivo, dire)
                pdfM.pdfM(dire)
            except:
                print 'No se ha podido descargar: %s' % self.archivo
        elif self.ext == 'img':
            try:
                dire = '/tmp/amanda/%s/imagenes/%s' % (self.car, nombre)
                bro.retrieve(self.archivo, dire)
            except:
                print 'No se ha podido descargar: %s' % self.archivo
    def texto(self):
        txt_listas = open('/tmp/amanda/%s/directorios.txt' % self.car, 'ab')
        txt_listas.write('<<<<<<<<<<directorios>>>>>>>>>>' + '\n')
        self.control.sort()
        for i in self.control:
            txt_listas.write(i.encode('utf-8') + '\n')
        txt_listas.close()
