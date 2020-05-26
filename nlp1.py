import PyPDF2
myfile = open('./data/US_Declaration.pdf', mode='rb')

pdf_reader = PyPDF2.PdfFileReader(myfile,strict=False)
pdf_reader.numPages
page_one = pdf_reader.getPage(0)
print(page_one.extractText())
person = 'prada'
print(f'my name is {person}')
#myfile.close()

pdf_reader = PyPDF2.PdfFileReader(myfile,strict=False)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)
pdf_output = open('./data/new.pdf','wb')
pdf_writer.write(pdf_output)
pdf_output.close()
myfile.close()

brand_new = open('./data/new.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(brand_new)
pdf_reader.numPages
