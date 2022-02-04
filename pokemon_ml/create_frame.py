#!/usr/bin/env python

import pandas as pd
import os
from pathlib import Path

wd = 'c:\\Users\\dwagn\\Desktop\\'
pic_folder = wd + 'poke_pics'
os.chdir(wd)

poke_data = pd.read_csv('pokemon.csv').iloc[:,0:3]
poke_data['Name'] = poke_data['Name'].str.lower() \
                    .rename({'Number' : 'Pokemon_ID'}, axis=1)

pic_path = Path(pic_folder)
files = list(pic_path.glob('*.png'))
nms = [str(x).split('\\')[5].strip('0123456789')[:-4] for x in files] # name from path
pics_data = pd.DataFrame({'File' : files, 'Name' : nms})
full_data = pd.merge(poke_data, pics_data, on='Name')