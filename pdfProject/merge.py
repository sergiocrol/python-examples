import PyPDF2
import sys

inputs = sys.argv[1:]

if len(inputs) < 2:
    print("You must provide at least two files to merge")
    sys.exit(1)


def pdf_combiner(pdf_list):
    merged_pdf = PyPDF2.PdfFileMerger()
    for file in pdf_list:
        merged_pdf.append(file)
    merged_pdf.write('./pdf/merged.pdf')


pdf_combiner(inputs)
