#!/usr/local/bin/python3

from PIL import Image, ImageDraw, ImageFont

import sys
import uuid

IMAGE_SIZE = (250, 100)
FONT_PATH = 'fonts/RobotoCondensed-Regular.ttf'
FONT_SIZE = 40
RED = '#FF0000'

def get_font(unique=True):
	return ImageFont.truetype(font=FONT_PATH, size=FONT_SIZE)

def get_filename(unique=True):
	if unique:
		return uuid.uuid4().hex + '.png'
	else:
		return 'test.png'

def get_text_centered_image(text):
	im = Image.new('RGB', IMAGE_SIZE)
	draw = ImageDraw.Draw(im)
	font = get_font()

	text_size = draw.textsize(text, font=font)

	print('Text Size: ', text_size)
	print('Image Size: ', IMAGE_SIZE)

	centered_position = get_centered_position(IMAGE_SIZE, text_size)

	draw.text(centered_position, text, fill=RED, font=font)

	return im

def get_centered_position(outer_size, inner_size):
	W, H = outer_size
	w, h = inner_size

	return ((W - w) / 2, (H - h) / 2)



if __name__ == '__main__':
	text = sys.argv[1]
	im = get_text_centered_image(text)
	im.save('generated/' + get_filename(unique=False), 'PNG')



