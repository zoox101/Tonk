
#------------------------------------------------------------------------------#
# Human Interaction Model
#------------------------------------------------------------------------------#

class UI:


    @staticmethod
    def get_number(prompt='Enter a number:'):
        selection = None
        while selection is None:
            print prompt,
            selection = raw_input()
            try: selection = int(selection)
            except: selection = None
        return selection


    @staticmethod
    def get_from_list(list, prompt='Select value '):
        selection = None
        while selection is None:
            print prompt + str(list) + ':',
            selection = raw_input()
            if selection not in list:
                selection = None
        return selection


    @staticmethod
    def valid_card(card):
        card = UI.from_human_readable(card)
        try: card = int(card)
        except: card = 0
        return card


    #Gets a valid card from the user
    @staticmethod
    def get_card(prompt='Card:'):
        choice = 0
        while not 14 > choice > 0:
            print prompt,
            choice = UI.valid_card(raw_input())
        return choice


    #Gets a valid card from the user
    @staticmethod
    def get_hand(prompt='Hand:'):

        cards = None
        while cards is None:

            #Getting the string from the user
            print prompt,
            hand = UI.from_human_readable(raw_input())
            split = str.split(hand, ' ')

            #Getting the cards from the string
            cards = [UI.valid_card(card) for card in split]

            #Checking the each of the cards is valid
            for card in cards:
                if not 14 > card > 0:
                    cards = None; break

        #Returning the hand
        return cards


    #Converts a human readable cardname to the integer cardname
    @staticmethod
    def from_human_readable(cardname):
        cardname = cardname.upper()
        if cardname == 'K': cardname = '13'
        if cardname == 'Q': cardname = '12'
        if cardname == 'J': cardname = '11'
        if cardname == 'A': cardname = '1'
        return cardname


    #Converts a hand to the human readable format
    @staticmethod
    def to_human_readable(cardname):
        if cardname == 13: cardname = 'K'
        if cardname == 12: cardname = 'Q'
        if cardname == 11: cardname = 'J'
        if cardname == 1: cardname = 'A'
        return cardname


    #Converts a card to the human readable format
    @staticmethod
    def hand_to_human_readable(hand):
        human_readable_hand = []
        for card in hand:
            human_readable_hand.append(UI.to_human_readable(card))
        return human_readable_hand


#------------------------------------------------------------------------------#
#
#------------------------------------------------------------------------------#
