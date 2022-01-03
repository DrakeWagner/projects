#!/usr/bin/env python3

import os
import glob
import pandas as pd


# os.chdir('~\\git\\ds-5110-proj\\main\\data')
os.chdir('c:\\Users\\dwagn\\git\\ds-5110-proj\\main\\data')
print(os.listdir(os.curdir))
filenames = [i for i in glob.glob('*.{}'.format('csv'))]
print(filenames)

# # check overlapping columns
# def get_colnames(files):
#     for i in files:
#         print('Columns in file {}:'.format(i))
#         df1 = pd.read_csv(i)
#         names_list = list(df1.columns)
#         print(names_list, '\n')
# get_colnames(filenames)

# read in csv files
games = pd.read_csv('games.csv')
games_details = pd.read_csv('games_details.csv')
players = pd.read_csv('players.csv')
ranking = pd.read_csv('ranking.csv')
teams = pd.read_csv('teams.csv')

by_team = pd.merge(games_details, teams,
                    on='TEAM_ID',
                    how='inner')

home_teams_names = teams[['TEAM_ID', 'ABBREVIATION']]
home_teams_names['HOME_TEAM_ID'] = home_teams_names['TEAM_ID']
home_teams_names['HOME_TEAM_ABV'] = home_teams_names['ABBREVIATION']
merged = pd.merge(home_teams_names, games,
            on='HOME_TEAM_ID')

away_teams_names = teams[['TEAM_ID', 'ABBREVIATION']]
away_teams_names['VISITOR_TEAM_ID'] = away_teams_names['TEAM_ID']
away_teams_names['VISITOR_TEAM_ABV'] = away_teams_names['ABBREVIATION']
merged = pd.merge(away_teams_names, merged,
            on='VISITOR_TEAM_ID')
merged = merged.drop(columns=['TEAM_ID_x', 'TEAM_ID_y', 'TEAM_ID', 'ABBREVIATION_x', 'ABBREVIATION_y', 'GAME_STATUS_TEXT'])
merged.to_csv('merged.csv', index=False, encoding='utf-8-sig')
# selection by team 
# print(by_team.head())
# lakers = by_team.loc[by_team['TEAM_ABBREVIATION'] == 'LAL']
# print(lakers.head())

'''
# Combines all
combined = pd.concat([pd.read_csv(f) for f in filenames])
combined.to_csv( "combined_stats.csv", index=False, encoding='utf-8-sig')
'''