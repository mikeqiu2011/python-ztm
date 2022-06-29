from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')

print(img.format)  # JPEG
print(img.size)  # (640,640)
print(img.mode)  # RGB

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save('smooth.png')

conv_img = img.convert('L')
# conv_img.save('grey.png')
rotated_img = conv_img.rotate(90)
# rotated_img.show()

resized = conv_img.resize((300, 300))
# resized.show()

# box = (100, 100, 400, 400)
# regin = img.crop(box)
# regin.show()

img.thumbnail((100, 200))
img.show()
