import PyPDF2
import sys

if len(sys.argv) < 2:
    print("Please, provide an input file")
    sys.exit(1)


def mark_file(input_file):
    reader = PyPDF2.PdfFileReader(open(input_file, 'rb'))
    writer = PyPDF2.PdfFileWriter()
    wtr_page = PyPDF2.PdfFileReader(open('./pdf/wtr.pdf', 'rb')).getPage(0)
    for i in range(reader.getNumPages()):
        pdf_page = reader.getPage(i)
        pdf_page.mergePage(wtr_page)
        writer.addPage(pdf_page)

    with open('./pdf/marked.pdf', 'wb') as marked_pdf:
        writer.write(marked_pdf)


mark_file(sys.argv[1])
