import pandas as pd
import random
from Agents.AutoAgent import AutoAgent

#Simulates a deck of cards (No suits)
class Deck:

    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.cards = []
        for i in range(1,14):
            self.cards += [i] * 4
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)


class Tonk:

    def sort_hand(self, hand):
        list.sort(hand)
        return hand


    def eval_hand(self, hand):
        sum = 0
        for card in hand:
            sum += self.eval_card(card)
        return sum


    def eval_card(self, card):
        return min(card, 10)


    def choose_discard(self, hand):
        dups = {}

        #Getting all the duplicates in the hand
        for card in hand:
            if card not in dups:
                dups[card] = 0
            dups[card] += self.eval_card(card)

        #Getting the card with the highest value
        max_key = None; max = 0
        for key in dups:
            if dups[key] > max:
                max = dups[key]
                max_key = key

        #Returning the most expensive card
        return max_key


    def choose_draw(self, hand, deposit):
        return deposit not in hand


def play_tonk():

    df = pd.DataFrame({'turn': [], 'a': [], 'b': []})

    deck = Deck()
    tonk = Tonk()

    a = []; b = []
    for i in range(5):
        a.append(deck.draw())
        b.append(deck.draw())

    #Returning outputs
    tonk.sort_hand(a)
    tonk.sort_hand(b)
    temp = pd.DataFrame({'turn': [0], 'a': [a], 'b': [b]})
    df = df.append(temp)

    deposit = deck.draw()
    for i in range(1,7):

        #Playing game for A
        discard = tonk.choose_discard(a)
        a = list(filter(lambda x: x != discard, a))

        if tonk.choose_draw(a, deposit):
            deposit = discard
            a.append(deck.draw())
        else:
            a.append(deposit)
            deposit = discard

        #Playing game for B
        discard = tonk.choose_discard(b)
        b = list(filter(lambda x: x != discard, b))

        if tonk.choose_draw(b, deposit):
            deposit = discard
            b.append(deck.draw())
        else:
            b.append(deposit)
            deposit = discard

        #Returning outputs
        tonk.sort_hand(a)
        tonk.sort_hand(b)
        temp = pd.DataFrame({'turn': [i], 'a': [a], 'b': [b]})
        df = df.append(temp)

    return df



