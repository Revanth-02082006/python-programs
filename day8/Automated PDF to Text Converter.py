import PyPDF2

pdf_file = "document.pdf"
with open(pdf_file, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        print(page.extract_text())
