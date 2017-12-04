from TonkAgent1 import TonkAgent1
from HumanAgent import HumanAgent
from SimulatedGame import SimulatedGame

#------------------------------------------------------------------------------#
# Main Method
#------------------------------------------------------------------------------#

a = HumanAgent('Will')
b = TonkAgent1('Alexa')

game = SimulatedGame([b,a])
print game.play()


#print a.convert_hand('(1,2,3,4,5)')
#game = TonkGame({'Alice': '123', 'Bob': 'xyz'})
