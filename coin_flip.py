"""
This is a coin flip game with the following rules:

Whenever heads or tails becomes 3 flips ahead of the other side,
the winner is paid out 8 dollars.  For each flip though, a dollar
will be substracted.

You can run the simulation N times by doing the following:

python coin_flip.py 10

"""

import random
import sys
import math

num_heads = 0
num_tails = 0
num_flips = 0
total_num_flips = 0
win_bonus_per_game = 8
total_winning = 0
iterations = int(sys.argv[1])

for i in range(iterations):
    while True:
        value = random.random()
        num_flips += 1
        if value <= .499999999999999:
            num_heads += 1
        else:
            num_tails += 1
        if num_heads - num_tails == math.fabs(3):
            total_winning += win_bonus_per_game
            total_num_flips += num_flips
            print "simulation: %s" % i
            print "num_heads: %s" % num_heads
            print "num_tails: %s" % num_tails
            print "num_flips: %s" % num_flips
            print "profit for game: %s" % (win_bonus_per_game - num_flips) 
            num_tails = 0
            num_heads = 0
            num_flips = 0
            break
        
net_profit = total_winning - total_num_flips
print "simulations run: %s" % iterations
print "net_profit: %s" % net_profit 