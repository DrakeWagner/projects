# Function to pull python functions
# included in spotify.ipynb

import time
import os
import dotenv
import requests
import pandas as pd
import numpy as np

def pull_albums(artist_id):
	global requests	
	global url

	album_names_dates = {}

	# for duplicates
	albs_added = []
	to_remove = []

	track_info = []
	repeat_detection = []

	albums = requests.get(url + 'artists/' + artist_id + '/albums', 
                 headers=headers, 
                 params={'include_groups': 'album', 'limit': 50}).json()

	for album in albums['items']:
	    album_names_dates[album['name']] = album['release_date']

	artist_name = requests.get(url + 'artists/' + artist_id, headers=headers).json()['name']
	print(f'Successfully accessed {artist_name}')

	for i in range(len(albums['items'])):
	    alb_name = albums['items'][i]['name']
	    if alb_name in albs_added:
	        to_remove.append(i)
	    albs_added.append(alb_name)

	iter = 0
	for i in albums['items']:
	    
	    if iter not in to_remove:

	        r = requests.get(url + 'albums/' + i['id'] + '/tracks', 
	            headers=headers)
	        tracks = r.json()['items']

	        for track in tracks:
	            detailsr = requests.get(url + 'audio-features/' + track['id'], headers=headers).json()

	            # combine with album info
	            detailsr.update({
	                'track_name': track['name'],
	                'album_name': i['name'],
	                'album_id': i['id'],
	                'release_date': i['release_date']
	            })

	            track_info.append(detailsr)
	        print('{} added...'.format(i['name']))
	        
	    iter += 1

	print('Execution time: ', time.process_time() - start, sep='')
