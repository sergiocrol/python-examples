from PIL import Image
import sys
import os
import re

try:
    inputFolder = sys.argv[1] if len(sys.argv) > 1 else sys.exit()
    outputFolder = sys.argv[2] if len(sys.argv) > 2 else "./PNG/"

    # If we have the directory as string
    input_directory = os.fsencode(inputFolder)
    os.makedirs(outputFolder, exist_ok=True)
        # An alternative way
        # if not os.path.exists(directory):
        #    os.makedirs(directory)

    for file in os.listdir(input_directory):
        # We decode each file
        filename = os.fsdecode(file)
        try:
            image = Image.open(f'{inputFolder}{filename}')
        except:
            # In case it is not an image, we ignore it and continue
            continue
        # regex (?<=\/) -> from '/', not included | .* -> anything | (?=\.) -> from '.' backward (not included)
        image_name = re.search(r"(?<=\/).*(?=\.)", image.filename).group(0)
            # An alternative way
            # image_name = os.path.splitext(filename)[0]
        image.save(f'{outputFolder}{image_name}.png', 'png')
except SystemExit as err:
    print("You have to provide an input folder")
