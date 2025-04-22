import smtplib
from email.message import EmailMessage
email = EmailMessage()
email["From"] = "your_email@example.com"
email["To"] = "recipient@example.com"
email["Subject"] = "Hello from Python"
email.set_content("This is a test email.")
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("your_email@example.com", "your_password")
server.send_message(email)
server.quit()
