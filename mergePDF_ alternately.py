# -*- coding: utf-8 -*-
# Merge pages of two PDF alternately.
 
import sys
import argparse
from PyPDF3 import PdfFileReader, PdfFileWriter

if __name__ == '__main__':    
    pathA = sys.argv[1]
    pathB = sys.argv[2]
    pathOut = sys.argv[3]
 
    print('Reading files...')
    pdfA = PdfFileReader(pathA)
    pdfB = PdfFileReader(pathB)
    out = PdfFileWriter()

    print('Merging files...')
    numA = pdfA.getNumPages()
    numB = pdfB.getNumPages()
    for i in range(max(numA, numB)):
        if i < numA:
            out.addPage( pdfA.getPage(i) )
        if i < numB:
            out.addPage( pdfB.getPage(i) )

    print('Writing the merged file...')
    with open(pathOut, 'wb') as f:
        out.write(f)

