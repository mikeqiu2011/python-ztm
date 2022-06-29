import os
import sys
from PIL import Image

folder_in = sys.argv[1]
folder_out = sys.argv[2]

print(folder_in)
if not os.path.exists(folder_out):
    os.makedirs(folder_out)

for file in os.listdir(folder_in):
    print(file)
    # filename, extension = file.split('.')
    [filename, extension] = os.path.splitext(file)
    if extension.lower() in ['.jpg', '.jpeg']:
        new_file = Image.open(f'{folder_in}/{file}')
        new_file.save(f'{folder_out}/{filename}.png')
