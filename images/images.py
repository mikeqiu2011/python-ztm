from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')

print(img.format)  # JPEG
print(img.size)  # (640,640)
print(img.mode)  # RGB

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save('smooth.png')

conv_img = img.convert('L')
conv_img.save('grey.png')
