import os, shutil
folder = input("Enter folder path: ")
for file in os.listdir(folder):
    ext = file.split(".")[-1]
    ext_folder = os.path.join(folder, ext)
    os.makedirs(ext_folder, exist_ok=True)
    shutil.move(os.path.join(folder, file), ext_folder)
