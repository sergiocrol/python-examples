from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

# format = JPEG | size = (640, 640) | mode = RGB (color mode)
print(img.mode)

# We can filter an image (we can use blur, smooth, sharpen, etc
filtered_image = img.filter(ImageFilter.GaussianBlur(3))
filtered_image.save("./Modified/pikachu_blur.png", "png")

# We can convert the image (to greyscale, for instance)
convert_image = img.convert('L')
convert_image.save("./Modified/pikachu_grey.png", "png")

# Open the image in a window
# convert_image.show()

# We can also rotate
rotated_image = img.rotate(180)
rotated_image.save("./Modified/pikachu_rotate.png", "png")

# Or resize
resized_image = img.resize((320, 320))
resized_image.save("./Modified/pikachu_resize.png", "png")

# Or crop. The argument is a tuple (left, upper, right, lower), where left it'd be the position in pixels from where
# we start and right the position in pixel to where we finish (the same with upper and lower)
cropped_image = img.crop((100, 100, 400, 400))
cropped_image.save("./Modified/pikachu_crop.png", "png")

# We can also make a thumbnail from an image if we want to reduce the size.
# For instance, the astro.jpg image is 3.8MB, we can create a thumb
# This modify the original image, so we might want to create a copy before
astro = Image.open("./astro.jpg")
astro_copy = astro.copy()
astro_copy.thumbnail((300, 300))
astro_copy.save("./Modified/astro_thumb.jpg", "jpeg")