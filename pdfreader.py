import sys
import PyPDF2

pdfdocument = sys.argv[1]
pdfFileObj = open(pdfdocument, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
rangePages = range(pdfReader.numPages) //number of pages
for x in rangePages:
  pageObj = pdfReader.getPage(x)
  print(pageObj.extractText())
