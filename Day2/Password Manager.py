from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

password = input("Enter password: ")
encrypted_password = cipher.encrypt(password.encode())
print("Encrypted Password:", encrypted_password)
