#!/usr/bin/env python

'''
Because png images are generally better for sharp lines/brighter colors,
I will be keeping the format of the pictures as PNG. Below is some code
to convert to JPG in case I want to try a different approach
'''

import os
from PIL import Image
import matplotlib.pyplot as plt

filename = 'pokelinks.txt'
pic_folder = 'poke_pics'
wd = 'c:\\Users\\dwagn\\Desktop\\' + pic_folder
os.chdir(wd)

print(wd)

def toPNG(img):
    file = Image.open(img + ".jpg") \
                .resize((450,450)) \
                .convert('RGB')
    file.save('{}.png'.format(img), 'png')
    print(type(file))
    return file

def toJPG(img):
    file = Image.open(img + ".png") \
                .resize((450,450)) \
                .convert('RGB')
    file.save('{}.jpg'.format(img), 'jpeg')                

    return file


# visualize
plt.imshow(toJPG(wd + '\\0bulbasaur'))
plt.axis("off")
plt.show()


# Plot the image without axes
# a = toPNG(wd + '\\0bulbasaur')
# plt.imshow(a)
# plt.axis("off")
# plt.show()