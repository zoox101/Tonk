
#------------------------------------------------------------------------------#
# Imports
#------------------------------------------------------------------------------#

import pandas as pd
import pickle

#------------------------------------------------------------------------------#
#
#------------------------------------------------------------------------------#

#Basic predictor. Always returns a loss.
class _BasicPredictor():
    def predict(self, df): return 0

#------------------------------------------------------------------------------#
# ClassifierAgent
#------------------------------------------------------------------------------#

#Constant time agent using basic rules
class AutoAgent:

    #Initializing the tonk agent
    def __init__(self, name, predictor=_BasicPredictor()):
        self.name, self.predictor = name, predictor


    #Evaluates the agent's hand
    def eval_hand(self, hand):
        sum = 0
        for card in hand:
            sum += self.eval_card(card)
        return sum


    #Evaluates a single card
    def eval_card(self, card):
        return min(card, 10)


    #Chooses the card to discard
    def choose_discard(self, records):

        #Getting the current hand and deposit
        hand = records[self.name].iloc[-1]
        deposit = int(records['Place'].iloc[-1])

        #Getting all the duplicates in the hand
        dups = {}
        for card in hand:
            if card != deposit:
                if card not in dups:
                    dups[card] = 0
                dups[card] += self.eval_card(card)

        #Getting the card with the highest value
        max_key = None; max = 0
        for key in dups:
            if dups[key] > max:
                max = dups[key]
                max_key = key

        #Checking to make sure the value picked a card
        if max_key is None:
            max_key = hand[0]

        #Returning the most expensive card
        return max_key


    #Chooses which card to draw
    def choose_draw(self, records):

        #Getting the hand and the current deposit
        hand = records[self.name].iloc[-1]
        deposit = int(records['Place'].iloc[-1])
        return deposit not in hand and deposit > 3


    def predict(self, v):
        data = {'asum': [v[0]], 'acount': [v[1]],\
            'bcount': [v[2]], 'turn': [v[3]]}
        df = pd.DataFrame(data)
        df = df[['asum', 'acount', 'bcount', 'turn']]
        return self.predictor.predict(df)


    #Chooses when to call tonk
    def choose_tonk(self, records):

        #Getting the current hand
        hand = records[self.name].iloc[-1]

        #Getting prediction variables
        hand_value = self.eval_hand(hand)
        len_my_hand = len(hand)

        #Getting all the opponents
        opponents = list(records.columns.values)
        order = ['Move', 'Place', 'Count', 'Take', 'From']
        for col in order:
            opponents.remove(col)
        opponents.remove(self.name)

        #Getting lengths of opponent hands
        opp_hands = []
        for opponent in opponents:
            opp_hands.append(records[opponent].iloc[-1])
        len_opp_hand = min(opp_hands)

        #Getting the current turn count
        opp_moves = []
        for opponent in opponents:
            opp_moves.append(len(records[records['Move'] == opponent]))
        turn_count = max(opp_moves)

        #Getting the prediction
        variables = [hand_value, len_my_hand, len_opp_hand, turn_count]
        prediction = self.predict(variables)

        #Checking to see if the agent should call Tonk
        high_win_prob = prediction > 0.50
        game_too_long = sum(records['Move'] == self.name) > 10
        return high_win_prob or game_too_long

#------------------------------------------------------------------------------#
#
#------------------------------------------------------------------------------#
