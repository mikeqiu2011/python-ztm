import os
import sys
import PyPDF2

folder = sys.argv[1]

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(folder):
    pdf_file = PyPDF2.PdfFileReader(f'{folder}/{file}')
    merger.append(pdf_file)

merger.write('merged.pdf')
