import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".avi"],
    "Scripts": [".py", ".js"]
}

TARGET_DIR = "C:/Users/YourUsername/Downloads"

def organize_files():
    for filename in os.listdir(TARGET_DIR):
        file_path = os.path.join(TARGET_DIR, filename)
        if os.path.isfile(file_path):
            for category, extensions in FILE_CATEGORIES.items():
                if any(filename.endswith(ext) for ext in extensions):
                    category_path = os.path.join(TARGET_DIR, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_path, filename))

if __name__ == "__main__":
    organize_files()
    print("Files organized successfully!")
