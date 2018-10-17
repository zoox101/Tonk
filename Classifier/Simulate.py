
#------------------------------------------------------------------------------#
# Imports
#------------------------------------------------------------------------------#

#from Simulation.SimulatedGame import *
#from Agents.AutoAgent import AutoAgent
from Classifier.FastTonk import Tonk, play_tonk
import pandas as pd

#------------------------------------------------------------------------------#
# Simulation
#------------------------------------------------------------------------------#

ITERS = 30000

games = []
for i in range(ITERS):
    if i % 10 == 0:
        print(str(round((float(i) / ITERS) * 100, 2)) + '%')
    games.append(play_tonk())
df = pd.concat(games)


#Adding info to the dataframe
agent = Tonk()
#df['turn'] = pd.Series(df.index)
df['asum'] = df['a'].apply(agent.eval_hand)
df['acount'] = df['a'].apply(len)
df['bsum'] = df['b'].apply(agent.eval_hand)
df['bcount'] = df['b'].apply(len)
df['win'] = df['asum'] < df['bsum']

df.to_csv('simulate_new.csv', index=False)

#------------------------------------------------------------------------------#
#
#------------------------------------------------------------------------------#


