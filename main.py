from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()
red.save('red.jpg')
green.save('green.jpg')
blue.save('blue.jpg')
shift = 100
red = Image.open("red.jpg")
red2 = red
coordinates = (shift, 0, red.width, red.height)
coordinates2 = (shift/2, 0, red.width-shift/2, red.height)
print(coordinates2)
crop_red = red.crop(coordinates)
crop_red2 = red2.crop(coordinates2)
# green = Image.open("green.jpg")
# blue = Image.open("blue.jpg")
# new_image = Image.merge("RGB", (red, green, blue))
# crop_red.save('crop_red.jpg')
image_all = Image.blend(crop_red, crop_red2, 0.3)
image_all.save('all.jpg')
# print(image_all.width)