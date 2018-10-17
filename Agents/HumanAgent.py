
#------------------------------------------------------------------------------#
# Imports
#------------------------------------------------------------------------------#

from UI import UI

#------------------------------------------------------------------------------#
# Human Agent
#------------------------------------------------------------------------------#

#Agent that plays a game of Tonk
class HumanAgent:

    #Initializing the tonk agent
    def __init__(self, name):
        self.name = name


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

        #Getting the hand and the current deposit
        hand = records[self.name].iloc[-1]
        value = self.eval_hand(hand)
        print(f'Pile: {UI.to_human_readable(records["Place"].iloc[-1])}', end=' ')
        print(f'|| {UI.hand_to_human_readable(hand)}: {value}')

        #Returning the card chosen by the user
        choice = 0
        while choice == 0:
            choice = UI.get_card('Choose a value to discard: ')
            if choice not in hand: choice = 0
        return choice


    #Chooses which card to draw
    def choose_draw(self, records):

        #Getting the current deposit
        deposit = int(records['Place'].iloc[-1])
        #print 'Pile: ' + str(self.to_human_readable(deposit))
        print('Draw from deck? (y/n) ', end='')

        #Getting the choice from the user
        choice = UI.from_human_readable(input())
        return choice[0].lower() == 'y'


    #Chooses when to call tonk
    def choose_tonk(self, records):

        #Getting the current hand
        hand = records[self.name].iloc[-1]
        value = self.eval_hand(hand)
        print(str(UI.hand_to_human_readable(hand)) + ': ' + str(value))

        print('Call Tonk? (y/n) ', end='')

        #Getting the choice from the user
        choice = UI.from_human_readable(input())
        return choice[0].lower() == 'y'


#------------------------------------------------------------------------------#
#
#------------------------------------------------------------------------------#
