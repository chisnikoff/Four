from PIL import Image

shift_value = 50
img = Image.open("monro.jpg")
red_channel, green_channel, blue_channel = img.split()

red_channel_double = red_channel
left_shift_coordinates = (shift_value, 0, red_channel.width, red_channel.height)
cropped_coordinates = (shift_value/2, 0, red_channel.width-shift_value/2, red_channel.height)
crop_red = red_channel.crop(left_shift_coordinates)
crop_red2 = red_channel_double.crop(cropped_coordinates)
img_red = Image.blend(crop_red, crop_red2, 0.3)

blue_channel_double = blue_channel
right_shift_coordinates = (0, 0, blue_channel.width-shift_value, blue_channel.height)
cropped_coordinates = (shift_value/2, 0, blue_channel.width-shift_value/2, blue_channel.height)
crop_blue = blue_channel.crop(right_shift_coordinates)
crop_blue2 = blue_channel_double.crop(cropped_coordinates)
img_blue = Image.blend(crop_blue, crop_blue2, 0.3)

cropped_coordinates = (shift_value/2, 0, green_channel.width-shift_value/2, green_channel.height)
img_green = green_channel.crop(cropped_coordinates)

new_image = Image.merge("RGB", (img_red, img_green, img_blue))
new_image.thumbnail((80, 80))
new_image.save('avatar.jpg')