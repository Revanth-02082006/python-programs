import qrcode
data = input("Enter data for QR code: ")
qr = qrcode.make(data)
qr.save("qrcode.png")
