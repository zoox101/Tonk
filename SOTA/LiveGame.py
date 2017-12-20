import pandas as pd
from UI import UI
from TonkAgent1 import TonkAgent1

#------------------------------------------------------------------------------#
# Live Game
#------------------------------------------------------------------------------#

#Plays a game of Tonk
class LiveGame:


    #Creating a new game of tonk
    def __init__(self, agent, players):

        #Checking to make sure the player is in the list of players
        if agent.name not in players:
            print 'Error player not in list of players.'
            return

        #Getting the current agent
        self.agent = agent
        self.players = players

        #Order of the rows
        order = ['Move', 'Place', 'Count', 'Take', 'From']

        #Creating the first record
        start = {}
        for col in order: start[col] = 'X'
        for player in self.players: start[player] = 5

        #Getting the starting hand and starting pile
        start[self.agent.name] = [sorted(UI.get_hand('Starting hand:'))]
        start['Place'] = UI.get_card('Starting place value:')

        #Reorganizing the records
        order = self.players + order
        self.records = pd.DataFrame(start, index=[0])
        self.records = self.records[order]

        #Playing the game
        self.play()


    #Plays out the starting tonk fight
    def start_move(self):

        #Getting the first move
        move = UI.get_from_list(self.players, 'Player start ')
        discard = UI.get_card('Discarded card:')

        #Getting info from the first row
        start_row = self.records.iloc[-1]
        take = start_row['Place']

        #If the player took the card
        if self.agent.name == move:

            #Getting the player's hand
            hand = self.records[self.agent.name].iloc[-1]
            start_len = len(hand)
            hand = filter(lambda x: x != discard, hand)
            end_len = len(hand)
            count = start_len - end_len
            hand.append(take)
            hand = sorted(hand)

            #Populating the new row
            data = {}
            for player in self.players: data[player] = start_row[player]
            data[self.agent.name] = hand
            data['Move'] = self.agent.name
            data['Place'] = discard
            data['Count'] = count
            data['Take'] = take
            data['From'] = 'Pile'

            #Updating the records
            self.records = self.records.append(data, ignore_index=True)

        #If the opponent took the card
        else:

            count = UI.get_number('Number discarded:')

            #Populating the new row
            data = {}
            for player in self.players: data[player] = start_row[player]
            data[move] = start_row[move] - count + 1
            data['Move'] = move
            data['Place'] = discard
            data['Count'] = count
            data['Take'] = take
            data['From'] = 'Pile'

            #Updating the records
            self.records = self.records.append(data, ignore_index=True)

        #Getting the next player
        index = self.players.index(move)
        next = (index + 1) % len(self.players)
        return self.players[next]


    #Playing move for the opponent
    def opp_move(self, opp_name):

        #Getting the row for the previous game
        data = {}
        start_row = self.records.iloc[-1]
        for player in self.players: data[player] = start_row[player]

        #Getting the opponent's move from the user
        data['Place'] = UI.get_card('Discarded card:')
        count = UI.get_number('Number discarded:')
        choice = UI.get_from_list(['S', 'D'], 'Stack or Deck [S/D]: ')

        #Generating new data for the opponent
        data[opp_name] = start_row[opp_name] - count + 1
        data['Count'] = count
        data['Move'] = opp_name

        #If the opponent took from the stack...
        if choice == 'S':
            data['Take'] = start_row['Place']
            data['From'] = 'Pile'

        #If the opponent took from the deck...
        else:
            data['Take'] = '?'
            data['From'] = 'Deck'

        #Updating the records
        self.records = self.records.append(data, ignore_index=True)

        #Getting the next player
        index = self.players.index(opp_name)
        next = (index + 1) % len(self.players)
        return self.players[next]


    #Playing the move for the player
    def my_move(self):

        #Getting the row for the previous game
        data = {}
        start_row = self.records.iloc[-1]
        for player in self.players: data[player] = start_row[player]

        #TODO: Outputting probabilities

        #Choosing the card to discard
        data['Move'] = self.agent.name
        discard = UI.get_card('Discarded card:')
        data['Place'] = discard

        #Asking if the player took from the deck or the stack
        choice = UI.get_from_list(['S', 'D'], 'Stack or Deck')

        #If the player took from the stack...
        if choice == 'S':
            data['Take'] = start_row['Place']
            data['From'] = 'Pile'

        #If the player took from the deck...
        else:
            data['Take'] = UI.get_card('Card drawn:')
            data['From'] = 'Deck'

        #Getting the player's hand
        hand = self.records[self.agent.name].iloc[-1]
        start_len = len(hand)
        hand = filter(lambda x: x != discard, hand)
        end_len = len(hand)
        count = start_len - end_len
        hand.append(data['Take'])
        hand = sorted(hand)

        #Updating the player's hand
        data[self.agent.name] = hand
        data['Count'] = count

        #Updating the records
        self.records = self.records.append(data, ignore_index=True)

        #Getting the next player
        index = self.players.index(self.agent.name)
        next = (index + 1) % len(self.players)
        return self.players[next]


    #Playing the game of Tonk
    def play(self):

        #Getting the start move
        to_move = self.start_move()

        #While the game is being played
        while to_move != None:

            print '\n' + to_move + '\'s turn'

            #Play moves
            if to_move == self.agent.name:
                to_move = self.my_move()
            else:
                to_move = self.opp_move(to_move)

            print self.records

        return self.records


#------------------------------------------------------------------------------#
# Main Method
#------------------------------------------------------------------------------#

agent = TonkAgent1('WILL')
game = LiveGame(agent, ['WILL', 'BOB'])
print game.play

#------------------------------------------------------------------------------#
#
#------------------------------------------------------------------------------#
