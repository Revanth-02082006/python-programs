from PIL import Image, ImageDraw, ImageFont

image = Image.open("sample.jpg")
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.text((10, 10), "Watermark", fill="white", font=font)

image.save("watermarked.jpg")
print("Watermark added!")
