#!/usr/bin/env python3

import requests
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import dotenv
# from dotenv import load_dotenv
import os


### Load in Spotify API credentials here 
os.chdir('C:\\Users\\dwagn\\Desktop')
dotenv.load_dotenv()
CLIENT_ID = os.getenv('spotify-client-id')
CLIENT_SECRET = os.getenv('spotify-client-secret')
os.chdir('C:\\Users\\dwagn\\git\\projects')


### Setup 
AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']

try:
    auth_response.status_code == 200
    print('Successfully accessed API')
except:
    raise Exception('API credentials rejected.')
    
headers = {'Authorization': 'Bearer {}'.format(access_token)}
url = 'https://api.spotify.com/v1/'    

artist_share_url = input('Paste artist spotify share link: ')
artist_id = artist_share_url.split('/')[4].split('?')[0]
print(artist_id)
    
albums = requests.get(url + 'artists/' + artist_id + '/albums', 
                 headers=headers, 
                 params={'include_groups': 'album', 'limit': 50}).json()

album_names_dates = {}
for album in albums['items']:
    album_names_dates[album['name']] = album['release_date']

artist_name = requests.get(url + 'artists/' + artist_id, headers=headers).json()['name']


### Gather Track Info
%%time
track_info = []
repeat_detection = []

for i in albums['items']:

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
    
    
df['release_date'] = pd.to_datetime(df['release_date'])
cols = df.columns.tolist()
cols = cols[-4:] + cols[:-4] # Last 4 columns to front
df = df[cols]

# Shorten long album names for graphs
for name in df['album_name']:
    if len(name) > 25:
        short_name = name[0:25]
        df = df.replace(name, short_name)
        
# remove tracks with na values, if any
def removeErrors(dataframe):
    na_tracks = []
    for track in dataframe[~dataframe['error'].isna()]['track_name']: 
        na_tracks.append(track)
    print('Removing: ', na_tracks)
    dataframe = dataframe[dataframe['error'].isna()].drop('error', 1) 

if ('error' in df.columns): 
    removeErrors(df)
    
# reformat track durations
def toMinsSecs(time):
    minutes = int(time)
    seconds = int((time - minutes) * 60)
    if seconds < 10:
        seconds = str(seconds).zfill(2) # adds zeros before single seconds
    full = '{}:{}'.format(minutes, seconds)
    return full

df['duration_mins'] = (df['duration_ms']/60000).round(2)
df['duration_full'] = df['duration_mins'].map(lambda x: toMinsSecs(x))

# subset by album
by_album = df.groupby('album_name').agg({'danceability':'mean',
                                         'energy':'mean',
                                         'loudness':'mean',
                                         'speechiness':'mean',
                                         'acousticness':'mean',
                                         'instrumentalness':'mean',
                                         'liveness':'mean',
                                         'valence':'mean',
                                         'tempo':'mean',
                                         'time_signature':'mean',
                                         'duration_ms':'sum',
                                         'duration_mins':'sum'}).round(3).reset_index()


# remove extra/repeated albums
# for repeat albums, go through and pick shortest album
albs_to_keep = {}
for name in by_album['album_name']:
    trim_name = name.split('(')[0].strip()
    alb_len = len(df[df['album_name'] == '{}'.format(name)])
    print(trim_name,':',alb_len)
    for i in albs_to_keep.keys():
        if (name[0:5] in i) & (alb_len <= albs_to_keep[i]):
            albs_to_keep[i] = 0
    albs_to_keep[name] = alb_len
albs_to_keep = {x:y for x,y in albs_to_keep.items() if y != 0}

by_album = by_album[by_album['album_name'].isin(albs_to_keep)].reset_index(drop=True)


### Top Correlations
corr_mat = by_album.corr(method='pearson').round(2)
sorted_mat = corr_mat.unstack().sort_values() \
             [:-(len(by_album.columns))-1] \
             [::2]
sorted_mat = sorted_mat.sort_values(ascending=False)
top_5_corr = sorted_mat.head(5)
bottom_5_corr = sorted_mat.tail(5)
print('Top 5 positive correlations:\n{}\n\nTop 5 negative correlations:\n{}' \
      .format(top_5_corr, bottom_5_corr))


### Album Lengths Graph
plt.figure(figsize=(10,10))
ax = sns.barplot(data=by_album, 
                 x='album_name', 
                 y='duration_mins',
                order = by_album.sort_values('duration_mins').album_name)
plt.xlabel("Album", size=15)
plt.ylabel("Duration in Minutes", size=15)
plt.title("Album Lengths for {artist}".format(artist = artist_name), size=18)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 30)


# The largest positive correlation for this artist
var1 = str(top_5_corr[0:1]).split()[0]
var2 = str(top_5_corr[0:1]).split()[1]

plt.figure(figsize=(10, 10))
plt.title("{var1} vs. {var2} for {artist} (by album)".format(var1 = var1,
                                                  var2 = var2,
                                                  artist = artist_name), size=18)
plt.tight_layout()
ax = sns.scatterplot(data=by_album, 
                 x=var1, 
                 y=var2,
                 s=1000,
                 hue='album_name',
                 palette='Set1')

ax.legend(h[1:len(album_names_dates)+1], 
          labs[1:int(len(album_names_dates))+1], loc='best', title=None)


# The largest negative correlation for this artist
var1 = str(bottom_5_corr[0:1]).split()[0]
var2 = str(bottom_5_corr[0:1]).split()[1]

plt.figure(figsize=(10, 10))
plt.title("{var1} vs. {var2} for {artist} (by album)".format(var1 = var1,
                                                  var2 = var2,
                                                  artist = artist_name), size=18)
plt.tight_layout()
ax = sns.scatterplot(data=by_album, 
                 x=var1, 
                 y=var2,
                 s=1000,
                 marker='o',
                 hue='album_name',
                 palette='Set1')
sns.set_style("ticks")
plt.xlabel(var1, size=15)
plt.ylabel(var2, size=15)

ax.legend(h[1:len(album_names_dates)+1], 
          labs[1:int(len(album_names_dates))+1], loc='best', title='Albums')