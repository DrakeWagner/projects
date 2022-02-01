#!/usr/bin/env python3

import os
from os.path import exists
import urllib.request
import requests
from bs4 import BeautifulSoup

# assign info
wd = 'c:\\Users\\dwagn\\Desktop'
os.chdir(wd)
filename = 'pokelinks.txt'
pic_folder = 'poke_pics'

# create text file/folder if not already exist
if exists(wd + '\\' + filename) == True:
    print(f'{filename} already exists')
else:
    with open(filename, 'w') as f:
        f.close()
    print(f'{filename} created at {wd}')
        
if exists(wd + '\\' + pic_folder):
    print(f'{pic_folder} already exists')
else:
    os.makedirs(pic_folder)
    print(f'{pic_folder} created at {wd}')

# list of pokemon names via website
url = 'https://pokemondb.net/pokedex/all'
page  = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
names = soup.find_all(class_='ent-name')
poke_names = []
[poke_names.append(x.text) for x in names]

def acquireLinks(pokemon, file):
    '''
    pokemon = pokemon to pull images of
    file = file to save to
    '''
    url = 'https://pokemondb.net/pokedex/{}#dex-sprites'
    page = requests.get(url.format(pokemon))

    soup = BeautifulSoup(page.content, 'html.parser')
    sprite_tags = soup.find_all('img', class_='img-fixed')
    links = []
    for image_tag in sprite_tags:
        links.append(image_tag['src'])
    sprites = [sp for sp in links if 'sprite' in sp]

    with open(file, 'a') as f:
        [f.write(x + '\n') for x in sprites]
        f.close()
    print(f'Updated {file} with ', len(sprites), ' new links.', sep='')

def reset_file(file):
    file = open(file, 'w')
    file.close()

def retrieveImage(link, dir, pokemon):

    # bypass 403
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Chrome')]
    urllib.request.install_opener(opener)

    urllib.request.urlretrieve(link, dir + '\\poke_images\\{}.png'.format(pokemon))

# begin scraping and saving links
for i in poke_names:
    acquireLinks(i, filename)

# save images from links
with open('pokelinks.txt') as f:
    lines = f.read().split('\n')
    iter = 0
    for url in lines:
        name = url.split('/')[-1].split('.png')[0]
        retrieveImage(url, wd, '{}{}'.format(iter, name))
        iter += 1
        print('{}/{}'.format(iter, len(lines)))

