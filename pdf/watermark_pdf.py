from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file = "merged.pdf"
watermark = "pdf_files/wtr.pdf"
merged = "watermark.pdf"

input_pdf = PdfFileReader(open(pdf_file, "rb"))
watermark_page = PdfFileReader(open(watermark, "rb")).getPage(0)

output = PdfFileWriter()

for i in range(input_pdf.getNumPages()):
    pdf_page = input_pdf.getPage(i)
    pdf_page.mergePage(watermark_page)
    output.addPage(pdf_page)

with open(merged, "wb") as merged_file:
    output.write(merged_file)
