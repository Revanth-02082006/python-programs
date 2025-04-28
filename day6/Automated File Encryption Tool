from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

with open("important.txt", "rb") as file:
    encrypted_data = cipher.encrypt(file.read())

with open("encrypted.txt", "wb") as file:
    file.write(encrypted_data)

print("File encrypted successfully!")
