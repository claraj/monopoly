import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import pickle
import sys
import os

import matplotlib
matplotlib.style.use('ggplot')


try:
    #If filename spacified, use that.
    filename = sys.argv[1]
    print(filename)
except:
    #use most recent file created
    files = os.listdir()
    time_most_recent = 0
    filename = 'None'
    for f in files:
        if f.startswith('square_data'):
            mtime = os.path.getmtime(f)  # timestamp of last modification timestamp
            if mtime > time_most_recent:
                filename = f
                time_most_recent = mtime
            print(f, mtime)

    if time_most_recent == 0 :
        exit('No square_data file found.')

#TODO check for file io errors. TODO Move files to subdirectory to avoid cluttering code dir.

# unpickle a dictionary that monopoly module created and saved.

print(filename)
f = open(filename, 'rb')
counts = pickle.load(f)

#from a run with 5 million rolls
#counts = {'baltic': 109723, 'virginia avenue': 123649, 'st james place': 139694, 'illinois avenue': 135121, 'conneticut ave': 115121, 'jail': 132896, 'pennsylvania railroad': 132880, 'indiana avenue': 135398, 'mediterranean': 107843, 'go to jail': 131780, 'short line': 120503, 'park place': 108392, 'CC': 383986, 'free parking': 142357, 'new york avenue': 145377, 'atlantic avenue': 134794, 'boardwalk': 108841, 'ventnor avenue': 134481, 'oriental avenue': 113641, 'states avenue': 119461, 'pennsylvania avenue': 124239, 'electric company utility': 116208, 'b&o railroad': 135121, 'pacific avenue': 133123, 'vermont avenue': 116247, 'income tax': 219853, 'kentucky avenue': 140203, 'marvin gardens': 130629, 'go': 107250, 'st charles': 112547, 'C': 367291, 'water works utility': 132487, 'reading railroad': 112729, 'tennessee ave': 145658, 'north carolina avenue': 130477}

square_names = ['go', 'mediterranean', 'CC', 'baltic', 'income tax', 'reading railroad', 'oriental avenue', 'C', 'vermont avenue', 'conneticut ave',
'jail',
'st charles', 'electric company utility', 'states avenue', 'virginia avenue', 'pennsylvania railroad', 'st james place', 'CC', 'tennessee ave', 'new york avenue',
'free parking',
'kentucky avenue', 'C', 'indiana avenue', 'illinois avenue', 'b&o railroad', 'atlantic avenue', 'ventnor avenue', 'water works utility', 'marvin gardens',
'go to jail',
'pacific avenue', 'north carolina avenue', 'CC', 'pennsylvania avenue', 'short line railroad', 'C', 'park place', 'luxury tax', 'boardwalk' ]


groups = {
    'brown' : ('mediterranean', 'baltic') ,
    'light blue'  : ('oriental avenue', 'vermont avenue', 'conneticut ave'),
    'pink' : ('st charles', 'states avenue', 'virginia avenue'),
    'orange' : ('st james place', 'tennessee ave', 'new york avenue'),
    'red' : ('kentucky avenue', 'indiana avenue', 'illinois avenue'),
    'yellow' : ('atlantic avenue', 'ventnor avenue', 'marvin gardens'),
    'green' : ('pacific avenue', 'north carolina avenue', 'pennsylvania avenue'),
    'dark_blue' : ('park place', 'boardwalk' ),
    'bad'  : ('income tax', 'luxury tax', 'go to jail', 'jail'),
    'good' : ('go', 'free parking' ),
    'cards' : ( 'C' , 'CC'),
    'utilities' : ('electric company utility', 'water works utility' ),
    'railroads' : ('reading railroad', 'pennsylvania railroad', 'b&o railroad', 'short line railroad'),
}


#Make a dictionary of names and corresponding color

empty_keys_list = [ (name, None) for name in square_names ]
square_names_and_groups = dict(empty_keys_list)

for group_name, list_of_names in groups.items():

    for name in list_of_names:
        square_names_and_groups[name] = group_name


#print(square_names_and_groups)

colors = {
    'brown' : '#8B4513',
    'light blue'  : '#87CEEB',
    'pink' : '#FF00FF',
    'orange' : '#FF8C00',
    'red' : 'r',
    'yellow' : '#FFFF00',
    'green' : 'g',
    'dark_blue' : '#483D8B',
    'bad'  : '#FFFFFF',
    'good' : '#FFEBCD',
    'cards' : '#7FFFD4',
    'utilities' : '#2F4F4F',
    'railroads' : '#A9A9A9',
}

s = Series(counts)
#print(s)

s = s.drop('C')
s = s.drop('CC')

s.sort()

print(s)

x = range(len(s))

barlist = plt.bar(x, s)


for bar, label in zip(barlist, s.keys()):
    #look up color for label
    group = square_names_and_groups[label]
    bar.set_color(colors[group])


plt.xticks(x, s.keys(), rotation='vertical')
plt.subplots_adjust(bottom=0.3)   #Shift the bottom up so the labels are not cut off

plt.show()
