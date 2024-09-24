from PIL import Image

shift_value = 50
img = Image.open("monro.jpg")
red_channel, green_channel, blue_channel = img.split()

red2 = red_channel
left_shift_coordinates = (shift_value, 0, red_channel.width, red_channel.height)
croped_coordinates = (shift_value/2, 0, red_channel.width-shift_value/2, red_channel.height)
crop_red = red_channel.crop(left_shift_coordinates)
crop_red2 = red2.crop(croped_coordinates)
img_red = Image.blend(crop_red, crop_red2, 0.3)
# img_red.save('red_shift.jpg')

blue2 = blue_channel
right_shift_coordinates = (0, 0, blue_channel.width-shift_value, blue_channel.height)
croped_coordinates = (shift_value/2, 0, blue_channel.width-shift_value/2, blue_channel.height)
crop_blue = blue_channel.crop(right_shift_coordinates)
crop_blue2 = blue2.crop(croped_coordinates)
img_blue = Image.blend(crop_blue, crop_blue2, 0.3)
# img_blue.save('blue_shift.jpg')

croped_coordinates = (shift_value/2, 0, green_channel.width-shift_value/2, green_channel.height)
img_green = green_channel.crop(croped_coordinates)

new_image = Image.merge("RGB", (img_red, img_green, img_blue))
new_image.save('all.jpg')
