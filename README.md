Which squares or spaces is a player most likely to land on in monopoly? Are they all equally likely? A python program to roll the two dice and move around the board, redirecting to jail or go or wherever the rules of the game dictate. Not particularly well tested and probably could be made much more efficient; and I might have overlooked some of the rules. Tennessee Avenue is the most likely to be landed on; Mediterranean Avenue is the least. And the Income Tax space seems to be particularly over-represented in the rankings, which is probably a bug on my part. 

Program assumes that player buys themselves out of jail at the first opportunity. Does it make a difference if the player pays to get out of jail, or waits and hopes to roll a double? 

But seems to confirm a hunch that the probabilities are not evenly distributed, orange and red are the colors that get landed on the most; brown and dark blue are landed on the least. 

Python 3 with matplotlib for bar graphs, and pandas for data manipulation. 

```
pip3 install matplotlib
pip3 install pandas 
python3 monopoly.py [number of times to roll the dice]
python3 graph.py
```

![bar graph of frequencies](https://raw.githubusercontent.com/minneapolis-edu/monopoly/master/monopolyfrequencies.png "Chart")
