from Tonk import Tonk, Deck
import matplotlib.pyplot as plot

#Tonk Stats
tonk = Tonk()
hand_cost = []
for i in xrange(100000):
    deck = Deck(); hand = []
    for i in xrange(5):
        hand.append(deck.draw())
    hand_cost.append(tonk.eval_hand(hand))
list.sort(hand_cost)
print hand_cost[100000/2]

plot.hist(hand_cost, 43)
plot.show()
