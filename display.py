# props to http://ozzmaker.com/add-colour-to-text-in-python/

import curses

reset = '\033[0;0;0m'

print('\033[0;33;40m   yellow normal ' + reset)
print('\033[1;33;40m   yellow  ' + reset)
print('\033[3;33;40m   yellow  ' + reset)
print('\033[5;33;40m   yellow  ' + reset)

print('\033[0;31;40m   red  ' + reset)
print('\033[1;31;40m   red bold ' + reset)
print('\033[3;31;40m   red dark ' + reset)
print('\033[5;31;40m   red blink' + reset)   #5 is blinking


colors = {
    'brown' : '\033[1;37;40m'  ,
    'light blue'  : '\033[36m',
    'pink' : '\033[35m',
    'orange' : '\033[33m',
    'red' : '\033[31m',
    'yellow' : '\033[33m',
    'green' : '\033[32m',
    'dark_blue' : '\033[34m',   #why does this print orange?
    'bad'  : '\033[2;31;40m',
    'good' : '\033[2;31;40m',
    'cards' : '\033[2;31;40m',
    'utilities' : '\033[1;30;47m',
    'railroads' : '\033[1;30;47m',
}

def outputstuff(counts, groups):

    print(chr(27) + "[2J")

    for group in groups.keys():
        #display count for these squares

        print( colors[group] + '** ' + group + ' **' + reset)

        for square in groups[group]:
            print(square, counts[square])


    # for key in counts.keys():
    #     print (key, counts[key])


        #TODO curses - color code and update as dice are rolled
