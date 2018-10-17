
#------------------------------------------------------------------------------#
# Imports
#------------------------------------------------------------------------------#

import pandas as pd
import random

#------------------------------------------------------------------------------#
# Deck
#------------------------------------------------------------------------------#

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


#------------------------------------------------------------------------------#
# Simulated Game
#------------------------------------------------------------------------------#

#Plays a game of Tonk
class SimulatedGame:

    #Creating a new game of tonk
    def __init__(self, agents):

        #Getting all the players in the game
        self.agents = {}
        for agent in agents:
            self.agents[agent.name] = agent

        #Creating the deck
        self.deck = Deck()
        self.hands = {}

        #Dealing the hands
        for agent_name in self.agents:
            self.hands[agent_name] = []
            for x in range(5):
                self.hands[agent_name].append(self.deck.draw())

        #Order of the rows
        order = ['Move', 'Place', 'Count', 'Take', 'From']

        #Sorting each of the hands
        for key in self.hands:
            self.hands[key] = sorted(self.hands[key])

        #Creating the first record
        start = {}
        for col in order:
            start[col] = 'X'
        for hand in self.hands:
            start[hand] = [self.hands[hand]]

        #Getting the starting card from the deck
        start['Place'] = self.deck.draw()

        #Reorganizing the records
        order = sorted(list(self.agents.keys())) + order
        self.records = pd.DataFrame(start, index=[0])
        self.records = self.records[order]


    #Adds the current state of the game to the record
    def add_record(self, move, place, count, take, frm):

        #Sorting each of the hands
        for key in self.hands:
            self.hands[key] = sorted(self.hands[key])

        #Creating a new record
        new_record = {}
        new_record.update(self.hands)
        new_record['Move'] = move
        new_record['Place'] = place
        new_record['Count'] = count
        new_record['Take'] = take
        new_record['From'] = frm

        #Adding record to the dataframe
        self.records = self.records.append(new_record, ignore_index=True)


    #Returning the information that a single agent knows
    def sanitize(self, agent_name):

        #Removing the other players' draws
        record = pd.DataFrame.copy(self.records)
        record.loc[record['From'] == 'Deck', 'Take'] = '?'

        #Removing the other players' hands
        order = [agent_name, 'Move', 'Place', 'Count', 'Take', 'From']
        for value in record.columns.values:
            if value not in order:
                record[value] = record[value].apply(len)

        #Returning the new record
        return record


    #Playing a new game of Tonk
    def play(self):

        tonk = False; turn = 0
        while not tonk:

            for agent_name in self.agents:

                #Getting the info for the agent
                agent = self.agents[agent_name]
                agent_info = self.sanitize(agent_name)

                #Letting the agent tonk
                if turn >= 2:
                    if agent.choose_tonk(agent_info):
                        tonk = True; break

                #Getting the current hand
                hand = self.records[agent_name].iloc[-1]

                #Choosing which card to discard and updating the hand
                discard = agent.choose_discard(agent_info)
                len_start = len(hand)
                hand = list(filter(lambda x: x != discard, hand))
                len_end = len(hand)
                num_discard = len_start - len_end

                #Choosing where to draw the next card from
                from_deck = agent.choose_draw(agent_info)
                if from_deck: frm = 'Deck'
                else: frm = 'Pile'

                #Choosing the next card
                if from_deck: new_card = self.deck.draw()
                else: new_card = self.records['Place'].iloc[-1]
                hand.append(new_card)
                self.hands[agent_name] = hand

                #Updating the record
                self.add_record(agent_name, discard, num_discard, new_card, frm)

            #Starting the next turn
            turn += 1

        #Returning the game record
        return self.records

#------------------------------------------------------------------------------#
#
#------------------------------------------------------------------------------#
