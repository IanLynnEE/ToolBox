# -*- coding: utf-8 -*-
# Merge pages of PDF with similar name.

import os
from PyPDF3 import PdfFileReader, PdfFileWriter

if __name__ == '__main__':    
    for filename in sorted(os.listdir()):
        if '-' in filename:
            out = PdfFileWriter()
            rootname = filename.split('-')[0] + '.pdf'
            pdfA = PdfFileReader(rootname)
            pdfB = PdfFileReader(filename)

            for i in range(pdfA.getNumPages()):
                out.addPage( pdfA.getPage(i) )
            out.addPage( pdfB.getPage(0) )
            with open(rootname, 'wb') as f:
               out.write(f)
            os.system(f'rm {filename}')
