
#------------------------------------------------------------------------------#
# Imports
#------------------------------------------------------------------------------#

import pandas as pd
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.metrics import accuracy_score

#------------------------------------------------------------------------------#
# Training Classifier
#------------------------------------------------------------------------------#

df = pd.read_csv('simulate.csv')

xs = df[['asum', 'acount', 'bcount', 'turn']]
ys = df['win']

SPLIT = int(0.7 * len(xs))
xs_train, xs_test = xs[:SPLIT], xs[SPLIT:]
ys_train, ys_test = ys[:SPLIT], ys[SPLIT:]

#Creating random forest
lr = LogisticRegression(random_state=0); lr.fit(xs_train, ys_train);
rf = RandomForestClassifier(random_state=0); rf.fit(xs_train, ys_train);
gbm = GradientBoostingClassifier(random_state=0); gbm.fit(xs_train, ys_train);

#Getting model scores
accuracy_score(ys_test, lr.predict(xs_test))
accuracy_score(ys_test, rf.predict(xs_test))
accuracy_score(ys_test, gbm.predict(xs_test))



#Saving output
pickle.dump(gbm, open('TonkPredictor.p', 'wb'))

x = pd.DataFrame([10,3,5,1], index=xs.columns).transpose()
gbm.predict_proba(x)

#------------------------------------------------------------------------------#
#
#------------------------------------------------------------------------------#

