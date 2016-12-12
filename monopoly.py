
import random
import sys
import time
import pickle

from random import shuffle
from collections import namedtuple, defaultdict, deque
import display

#TODO fix spellings
#TODO tests
#TODO curses output

'''
    rolling 3 doubles in a row, go to jail
    landing on go to jail square
    getting out of jail vs. being on just visiting (or not)
    chance and community chest redirect cards
        - chance, out of 16 cards: advance to boardwalk; nearest railroad; nearest utility; st charles place; go; reading; illinois; go to jail; go back 3 spaces
         - community chest, out of 16 cards: advance to go; go to jail;
'''


# railroads end with 'railroad' and utilities end with 'utility' so they can be identifed when player has to advance to a square of these types
# 'C' = Chance, 'CC' = community chest.

squares = ['go', 'mediterranean', 'CC', 'baltic', 'income tax', 'reading railroad', 'oriental avenue', 'C', 'vermont avenue', 'conneticut ave',
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
    'bad'  : ('income tax' , 'luxury tax', 'go to jail', 'jail'),
    'good' : ('go', 'free parking' ),
    'cards' : ( 'C' , 'CC'),
    'utilities' : ('electric company utility', 'water works utility' ),
    'railroads' : ('reading railroad', 'pennsylvania railroad', 'b&o railroad', 'short line railroad'),
}


chance = deque([ 'boardwalk', 'st charles', 'reading railroad', 'go', 'jail', 'illinois avenue', '^^^goback3', '^^^railroad', '^^^utility'] + [None]*10)
community_chest = deque(['go', 'jail'] + [ None ] * 14)  # 14 blank cards - pick one at random and test if none

shuffle(chance)
shuffle(community_chest)

print(chance)
print(community_chest)


class Dice():

    was_double = False

    def roll(self):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        #print(roll1, roll2)
        was_double = (roll1 == roll2)
        total = roll1 + roll2

        RollResult = namedtuple('Roll', ['roll1', 'roll2', 'total', 'was_double'])
        return RollResult(roll1, roll2, total, was_double)


class Board():

    def __init__(self):
        self.current_square = 0
        self.total_squares = len(squares)


    def advance(self, num_squares):
        self.current_square += num_squares
        self.current_square = self.current_square % self.total_squares
        return squares[self.current_square]


    def to_square(self, square_name):
        '''Advance to a particular square. If name begins with the special characters '^^^' have to
        figure out which square to move to. Otherwise, move to the square named in square_name'''

        if square_name.startswith('^^^'):
            if square_name == '^^^goback3':
                self.advance(-3)
            elif square_name == '^^^railroad':
                while not squares[self.current_square].endswith('railroad'):
                    self.advance(1)
            elif square_name == '^^^utility':
                while not squares[self.current_square].endswith('utility'):
                    self.advance(1)
        else:
            self.current_square = squares.index(square_name)

        return squares[self.current_square]



dice = Dice()
board = Board()

# roll dice loads of times

list_of_tups = [ (square, 0) for square in squares ]

square_land_count = dict(list_of_tups)

doubles = 0;

try :
    totalrolls = int(sys.argv[1])
except :
    totalrolls = 1000      #Default val, if no arg or is not readable as an integer.

print('Rolling dice %d times' % totalrolls)


for roll_count in range(0, totalrolls):

    roll = dice.roll()


    if roll.was_double:

        doubles += 1
        if doubles == 3:
            #print('go to jail')
            current_square = 'jail'
            board.to_square('jail')    #Assume player pays to get out of jail so can keep moving. Does this make any difference to probability of landing on any particular square?
            doubles = 0

        else :
            current_square = board.advance(roll.total)

    else:
        doubles = 0
        current_square = board.advance(roll.total)

    #print('landed on ' + current_square)

    square_land_count[current_square] += 1

    if current_square == 'CC' :   # community chest
        card = community_chest.popleft()   #take from the start....
        community_chest.append(card)       #and add to the end
        if card is not None:                #If card is one that redirects to another square, then move
            current_square = board.to_square(card)
            square_land_count[current_square] += 1

    if current_square == 'C':   #chance
        card = chance.popleft()   #take from the start....
        chance.append(card)       #and add to the end
        if card is not None:
            current_square = board.to_square(card)
            square_land_count[current_square] += 1

    if current_square == 'go to jail':
        current_square = board.to_square('jail')
        square_land_count[current_square] += 1

    #todo get out of jail  (?)


    if (roll_count % 1000 == 0):
        #display - don't want to update the console every single time.
        display.outputstuff(square_land_count, groups)


display.outputstuff(square_land_count, groups)

timestamp = int(time.time())   #Unique filename

output_file = open('square_data_%d' % timestamp, 'wb')

#Write to a file. Another program will read in and process.
pickle.dump(square_land_count, output_file)
