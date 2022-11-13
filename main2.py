import PyPDF2
pdf = open("contoh.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdf)
teks=""
p=0
while 1:
	try:
		page = reader.getPage(p)
		teks+=page.extractText()	
		p+=1
	except:
		break
print(teks)