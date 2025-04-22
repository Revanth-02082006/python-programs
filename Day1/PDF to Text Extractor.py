import PyPDF2
file = open("sample.pdf", "rb")
reader = PyPDF2.PdfReader(file)
for page in reader.pages:
    print(page.extract_text())
