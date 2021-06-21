import PyPDF2

# Without "with open..." we'd need to close the file and the end; this does not happen with "with"
# Int his case we need to use "rb" mode (read - binary), because PyPDF2 needs a binary code
with open('./pdf/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    # We have many options
    # numPages -> number of pages
    # getPage(0) -> get page number
    page = reader.getPage(0)
    # We can rotate the page
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    # Or add the rotated page to a new pdf we've created
    writer.addPage(page)
    with open('./pdf/tilt.pdf', 'wb') as new_file:
        writer.write(new_file)