from PIL import Image

img = Image.open('./pokedex/pikachu.jpg')

print(img.format)  # JPEG
print(img.size)  # (640,640)
print(img.mode)  # RGB
