import os
import sys
from PIL import Image

folder_in = sys.argv[1]
folder_out = sys.argv[2]

print(folder_in)
# os.makedirs(folder_out)

for file in os.listdir(folder_in):
    print(file)
    filename, extension = file.split('.')
    if extension == 'jpg':
        new_file = Image.open(f'{folder_in}/{file}')
        new_file.save(f'{folder_out}/{filename}.png')
