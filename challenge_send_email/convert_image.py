# can remove shebang
#!/usr/bin/env python3

import os
from PIL import Image

#root = os.path.expanduser('~') + /data/images'
path = 'data/images/'
new_path ='data/new_images/'
		
for image in os.listdir(path):
	print(image)
	if '.tiff' or '.png' in image:
		img = Image.open( path + image)
#		img = Image.open(image)
		name = image.split('.')[0]
		new_filename = new_path + name
		img.resize((600, 400)).convert("RGB").save(new_filename + '.jpg', 'JPEG')
		print(new_filename+ '.jpg')