from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

pdf_file = "merged.pdf"
watermark = "pdf_files/wtr.pdf"
merged = "watermark.pdf"

with open(pdf_file, "rb") as input_file, open(watermark,
                                              "rb") as watermark_file:
    input_pdf = PdfFileReader(input_file)
    watermark_page = PdfFileReader(watermark_file).getPage(0)

    output = PdfFileWriter()

    for i in range(input_pdf.getNumPages()):
        pdf_page = input_pdf.getPage(i)
        pdf_page.mergePage(watermark_page)
        output.addPage(pdf_page)

    with open(merged, "wb") as merged_file:
        output.write(merged_file)
