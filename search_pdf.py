# -*- coding: utf-8 -*-
# DNF

import os
import fitz

key = '調漲'
os.chdir('./b/')

for filename in sorted(os.listdir()):
    if 'pdf' not in filename:
        continue
    pdf = fitz.open(filename)
    for i in range(pdf.pageCount):
        page = pdf.loadPage(i)
        areas = page.searchFor(key)
        if not len(areas) > 0:
            print(filename)
            break
    pdf.close()

def pdf2txt(filename):
    text = ''
    pdf = fitz.open(filename)
    for i in range(pdf.pageCount):
        page = pdf.loadPage(i)
        text += page.getText()
    pdf.close()
    return text



'''
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def pdf2txt(pdf_filename):
    txt = ''

    device = PDFPageAggregator(PDFResourceManager(), laparams=LAParams())
    interpreter = PDFPageInterpreter(PDFResourceManager(), device)
    doc = PDFDocument()
    parser = PDFParser(open(pdf_filename, 'rb'))
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize()
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed

    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        for x in layout:
            if isinstance(x, LTTextBoxHorizontal):
                txt = x.get_text()
    return txt
'''
