import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

import matplotlib
matplotlib.style.use('ggplot')

# string = ''
# with open('square.data', 'r') as f:
#     string = f.read()

# todo unpickle a dictionary

# counts = {'pacific avenue': 7, 'pennsylvania railroad': 14, 'park place': 8, 'oriental avenue': 12, 'states avenue': 11, 'pennsylvania avenue': 13,
#  'illinois avenue': 15, 'st charles': 11, 'reading railroad': 12, 'free parking': 21, 'atlantic avenue': 12, 'indiana avenue': 18, 'vermont avenue': 11,
#   'short line': 11, 'jail': 13, 'virginia avenue': 11, 'new york avenue': 18, 'north carolina avenue': 20, 'electric company utility': 14, 'go to jail': 11,
#    'income tax': 15, 'b&o railroad': 12, 'mediterranean': 17, 'kentucky avenue': 11, 'marvin gardens': 13, 'boardwalk': 13, 'CC': 35, 'ventnor avenue': 8,
#    'st james place': 12, 'water works utility': 13, 'baltic': 8, 'C': 43, 'tennessee ave': 12, 'go': 12, 'conneticut ave': 13}


# counts = {'illinois avenue': 264, 'marvin gardens': 241, 'st charles': 245,
# 'oriental avenue': 229, 'kentucky avenue': 304, 'pacific avenue': 270,
# 'indiana avenue': 294, 'reading railroad': 218, 'b&o railroad': 260,
# 'pennsylvania railroad': 249, 'water works utility': 315, 'park place': 237,
# 'conneticut ave': 234, 'virginia avenue': 241, 'C': 727, 'new york avenue': 269,
# 'tennessee ave': 299, 'income tax': 434, 'atlantic avenue': 251, 'vermont avenue': 232,
# 'states avenue': 220, 'short line': 231, 'baltic': 228, 'ventnor avenue': 264,
# 'go': 202, 'pennsylvania avenue': 245, 'boardwalk': 200, 'jail': 256, 'CC': 806,
# 'north carolina avenue': 252, 'mediterranean': 231, 'go to jail': 277,
# 'electric company utility': 229, 'st james place': 300, 'free parking': 246}

counts = {'baltic': 109723, 'virginia avenue': 123649, 'st james place': 139694, 'illinois avenue': 135121, 'conneticut ave': 115121, 'jail': 132896, 'pennsylvania railroad': 132880, 'indiana avenue': 135398, 'mediterranean': 107843, 'go to jail': 131780, 'short line': 120503, 'park place': 108392, 'CC': 383986, 'free parking': 142357, 'new york avenue': 145377, 'atlantic avenue': 134794, 'boardwalk': 108841, 'ventnor avenue': 134481, 'oriental avenue': 113641, 'states avenue': 119461, 'pennsylvania avenue': 124239, 'electric company utility': 116208, 'b&o railroad': 135121, 'pacific avenue': 133123, 'vermont avenue': 116247, 'income tax': 219853, 'kentucky avenue': 140203, 'marvin gardens': 130629, 'go': 107250, 'st charles': 112547, 'C': 367291, 'water works utility': 132487, 'reading railroad': 112729, 'tennessee ave': 145658, 'north carolina avenue': 130477}


square_names = ['go', 'mediterranean', 'CC', 'baltic', 'income tax', 'reading railroad', 'oriental avenue', 'C', 'vermont avenue', 'conneticut ave',
'jail',
'st charles', 'electric company utility', 'states avenue', 'virginia avenue', 'pennsylvania railroad', 'st james place', 'CC', 'tennessee ave', 'new york avenue',
'free parking',
'kentucky avenue', 'C', 'indiana avenue', 'illinois avenue', 'b&o railroad', 'atlantic avenue', 'ventnor avenue', 'water works utility', 'marvin gardens',
'go to jail',
'pacific avenue', 'north carolina avenue', 'CC', 'pennsylvania avenue', 'short line', 'C', 'park place', 'income tax', 'boardwalk' ]


groups = {
    'brown' : ('mediterranean', 'baltic') ,
    'light blue'  : ('oriental avenue', 'vermont avenue', 'conneticut ave'),
    'pink' : ('st charles', 'states avenue', 'virginia avenue'),
    'orange' : ('st james place', 'tennessee ave', 'new york avenue'),
    'red' : ('kentucky avenue', 'indiana avenue', 'illinois avenue'),
    'yellow' : ('atlantic avenue', 'ventnor avenue', 'marvin gardens'),
    'green' : ('pacific avenue', 'north carolina avenue', 'pennsylvania avenue'),
    'dark_blue' : ('park place', 'boardwalk' ),
    'bad'  : ('income tax' , 'go to jail', 'jail'),
    'good' : ('go', 'free parking'),
    'cards' : ( 'C' , 'CC'),
    'utilities' : ('electric company utility', 'water works utility' ),
    'railroads' : ('reading railroad', 'pennsylvania railroad', 'b&o railroad', 'short line'),
}

#Make a dictionary of names and corresponding color

empty_keys_list = [ (name, None) for name in square_names ]
square_names_and_groups = dict(empty_keys_list)

for group_name, list_of_names in groups.items():

    for name in list_of_names:
        square_names_and_groups[name] = group_name


print(square_names_and_groups)

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



#plt.plot(counts)

s = Series(counts)
print(s)

s = s.drop('C')
s = s.drop('CC')
s = s.drop('income tax')

s.sort()

print(s)

#s.plot()

#fig = plt.figure()

x = range(len(s))

barlist = plt.bar(x, s)

barlist[0].set_color('#00ff33')
# print(dir(barlist))
# print(dir(barlist[0]))
# print(type(barlist[0]))

print(s.keys())

print('**')
for bar, label in zip(barlist, s.keys()):

    print(label)
    #look up color for label
    group = square_names_and_groups[label]
    bar.set_color(colors[group])



plt.xticks(x, s.keys(), rotation='vertical')
plt.subplots_adjust(bottom=0.3)   #Shift the bottom up so the labels are not cut off

plt.show()



# ts = Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
#
# ts = ts.cumsum()
#
# ts.plot()
