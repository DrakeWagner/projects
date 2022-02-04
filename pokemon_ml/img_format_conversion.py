#!/usr/bin/env python

'''
Because png images are generally better for sharp lines/brighter colors,
I will be keeping the format of the pictures as PNG. Below is some code
to convert to JPG in case I want to try a different approach
'''

import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

pic_folder = 'poke_pics'
wd = 'c:\\Users\\dwagn\\Desktop\\' + pic_folder
img = wd + '\\1bulbasaur.png'
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

def whiteBackground(img):
    img = Image.open(img).convert('RGB').resize((450,450))
    img = np.array(img)
    msk = np.all(img == (0,0,0), axis=-1)
    img[msk] = [255,255,255]
    plt.imshow(img)
    plt.axis('off')
    plt.show()

whiteBackground(img)
# Image.open(img).convert('RGB').resize((450,450))

# # visualize
# plt.imshow(toPNG(wd + '\\3bulbasaur'))
# plt.axis("off")
# plt.show()

