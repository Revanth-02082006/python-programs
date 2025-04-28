import os

directory = "C:/Users/Revanth/Documents"
for index, filename in enumerate(os.listdir(directory)):
    old_path = os.path.join(directory, filename)
    new_path = os.path.join(directory, f"file_{index}.txt")
    os.rename(old_path, new_path)

print("Files renamed successfully!")
