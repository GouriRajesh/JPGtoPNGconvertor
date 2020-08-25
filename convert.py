# The project converts JPG images to PNG images reading it from a source folder and creating
# a new destination folder and storing it in the same. Arguments are accepted from the commandline.
# 1st argument is sourcefolder/ and 2nd one the destinationfolder/

import sys
import os
from PIL import Image

source_folder = sys.argv[1]
destination_folder = sys.argv[2]

if not os.path.exists(destination_folder):
    # destination_folder does not exist
    os.makedirs(destination_folder)

for imagefile in os.listdir(source_folder):
    img = Image.open(f'{source_folder}{imagefile}')
    clean_imgname = os.path.splitext(imagefile)[0]
    img.save(f'{destination_folder}{clean_imgname}.png', 'png')
    print('Conversion done!')
