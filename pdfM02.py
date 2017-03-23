#-*-coding:utf8;-*-

from PyPDF2 import PdfFileReader, PdfFileMerger

obje = '/tmp/amanda/proba06/pdf/p_especialidad_mir_hh.pdf'
def pdfM(dir_arch):
#    try:
        merger = PdfFileMerger()
        pdfF = merger(PdfFileReader(dir_arch, "rb"))
        dicI = pdfF.getDocumentInfo()
        obj = dir_arch
        txt_salida = obj.lower().rsplit('.', 1)[0]
        text = open(txt_salida + '.txt', 'ab')
        for metaItem in dicI:
            text.write("[+] " + metaItem.encode('utf-8') + ":" + dicI[metaItem].encode('utf-8') + '\n')
        text.close()
#    except:
#        print "Fallo al abrir pdf"
pdfM(obje)