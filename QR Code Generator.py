import qrcode

data = "https://github.com/Revanth-02082006/python-programs"
qr = qrcode.make(data)
qr.save("qr_code.png")
print("QR Code Generated!")
