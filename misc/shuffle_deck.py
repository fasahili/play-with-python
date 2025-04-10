import itertools
import random

ranks = range(1, 14)
suits = ['Spade', 'Heart', 'Diamond', 'Club']
deck = list(itertools.product(ranks, suits))

random.shuffle(deck)

print("You got:")
for i in range(5):
    rank, suit = deck[i]
    print(f"{rank} of {suit}")