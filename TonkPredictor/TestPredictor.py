from Tonk import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

rf = pickle.load(open('TonkPredictor.p', 'rb'))

'''
df = pd.DataFrame({'turn': [], 'a': [], 'b': []})
for i in xrange(100):
    df = df.append(play_tonk())

tonk = Tonk()
df['asum'] = df['a'].apply(tonk.eval_hand)
df['acount'] = df['a'].apply(len)
df['bsum'] = df['b'].apply(tonk.eval_hand)
df['bcount'] = df['b'].apply(len)
df['win'] = df['asum'] < df['bsum']

testing_inputs = df[['asum', 'acount', 'bcount', 'turn']]
testing_outputs = df[['win']]

predicted = rf.predict(testing_inputs)
#accuracy = accuracy_score(testing_outputs, predicted)

#print accuracy
print testing_inputs
'''

def predict(v):
    data = {'asum': [v[0]], 'acount': [v[1]], 'bcount': [v[2]], 'turn': [v[3]]}
    df = pd.DataFrame(data)
    df = df[['asum', 'acount', 'bcount', 'turn']]
    print df
    print rf.predict(df)

#predict([45,5,5,0])
#predict([31,4,5,1])
#predict([30,3,5,2])
#predict([13,2,5,3])

#predict([42,5,5,0])
#predict([24,5,5,1])
#predict([17,4,5,2])

#predict([21,5,4,1])
#predict([16,4,4,2])

#predict([29,5,5,0])
#predict([24,5,5,1])
#predict([24,5,5,2])
#predict([20,4,5,3])
#predict([10,3,5,4])
#predict([32,5,5,0])
#predict([28,5,4,1])
