import zipfile

with zipfile.ZipFile("compressed.zip", "w") as zipf:
    zipf.write("file1.txt")
    zipf.write("file2.txt")

print("Files compressed successfully!")
