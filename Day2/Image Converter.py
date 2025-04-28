from PIL import Image

image = Image.open("sample.jpg")
image.save("sample.png")
print("Conversion complete!")
