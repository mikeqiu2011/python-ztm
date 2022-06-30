import PyPDF2

with open('pdf_files/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    print(page)  # get page obj
    page.rotate(180)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('pdf_files/tilt.pdf', 'wb') as file_out:
        writer.write(file_out)
