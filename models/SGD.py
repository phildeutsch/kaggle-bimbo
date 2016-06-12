import pandas as pd
from sklearn.linear_model import SGDClassifier

# Get data
import data

# Select variables to use
common_names = list(set(data.train.columns.values) & set(data.test.columns.values))
common_names.remove('Semana')

X_train = data.train.loc[data.train['Semana']==3][common_names]
y_train = data.train.loc[data.train['Semana']==3]['Demanda_uni_equil']
X_test = data.test[common_names]

# Fit SGD classifier
clf = SGDClassifier(loss="hinge", penalty="l2")
clf.fit(X_train, y_train)

# Get results
y = pd.DataFrame({'Demanda_uni_equil' : clf.predict(X_test)})
submission = pd.concat([data.test['id'], y], axis=1)
submission.to_csv('submission.csv', index=False)
