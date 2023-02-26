#!/usr/bin/python

import numpy as np
import pandas as pd
import os
dataset = pd.read_csv('data.csv')
dataset.head()

zero_not_accepted = ['organic','bakedgoods','cheese','crafts','flowers','eggs','seafood','herbs','vegetables','honey','jams','maple','meat','nursery','nuts','plants','poultry','prepared','soap','trees','wine','coffee','beans','fruits','grains','juices','mushrooms','petfood','tofu','wildharvested']
for column in zero_not_accepted:
    dataset[column] = dataset[column].replace(np.NaN, False)

dataset['organic'] = dataset['organic'].map({'-':False, 'Y':True, 'N':False})
dataset = dataset.dropna(subset = ['city', 'state'])
dataset = dataset.reset_index(drop=True)

dataset['website'] = ~dataset['website'].isnull()
dataset['facebook'] = ~dataset['facebook'].isnull()
dataset['twitter'] = ~dataset['twitter'].isnull()
dataset['youtube'] = ~dataset['youtube'].isnull()

new_pos = ['fmid', 'marketname',
       'othermedia', 'street', 'city', 'county', 'state', 'zip', 'season1date',
       'season1time', 'season2date', 'season2time', 'season3date',
       'season3time', 'season4date', 'season4time', 'x', 'y', 'location',
       'credit', 'wic', 'wiccash', 'sfmnp', 'snap', 'organic', 'bakedgoods',
       'cheese', 'crafts', 'flowers', 'eggs', 'seafood', 'herbs', 'vegetables',
       'honey', 'jams', 'maple', 'meat', 'nursery', 'nuts', 'plants',
       'poultry', 'prepared', 'soap', 'trees', 'wine', 'coffee', 'beans',
       'fruits', 'grains', 'juices', 'mushrooms', 'petfood', 'tofu',
       'wildharvested','website', 'facebook', 'twitter', 'youtube', 'updatetime']

dataset =dataset.reindex(columns=new_pos)

dataset = dataset.drop(columns=['othermedia','season1date','season1time','season2date','season2time','season3date','season3time','season4date','season4time','location'], axis = 1)
dataset.to_csv("fm_data.csv", index=False, header=False, sep = ';')

