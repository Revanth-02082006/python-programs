import PyPDF2

pdfs = ["file1.pdf", "file2.pdf"]
merger = PyPDF2.PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
print("PDFs merged successfully!")
