import hashlib

def get_file_hash(filename):
    with open(filename, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()

file1 = "original.txt"
file2 = "copy.txt"

if get_file_hash(file1) == get_file_hash(file2):
    print("Files are identical.")
else:
    print("Files have been modified!")
