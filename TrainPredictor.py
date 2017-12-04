from Tonk import *
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.DataFrame({'turn': [], 'a': [], 'b': []})
for i in xrange(30000): #30000
    if i % 100 == 0:
        print str(round((float(i) / 30000) * 100, 2)) + '%'
    df = df.append(play_tonk())

tonk = Tonk()
df['asum'] = df['a'].apply(tonk.eval_hand)
df['acount'] = df['a'].apply(len)
df['bsum'] = df['b'].apply(tonk.eval_hand)
df['bcount'] = df['b'].apply(len)
df['win'] = df['asum'] < df['bsum']


from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

training_inputs = df[['asum', 'acount', 'bcount', 'turn']]
training_outputs = df[['win']]

#Creating random forest
rf = RandomForestRegressor(n_estimators=100, random_state=121295)
rf.fit(training_inputs, training_outputs.values.ravel())

predicted = rf.predict(training_inputs)
print predicted
#accuracy = accuracy_score(training_outputs, predicted)
#print accuracy

import pickle
pickle.dump(rf, open('TonkPredictor.p', 'wb'))

print 'Finished!'
