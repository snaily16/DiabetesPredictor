import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score

df = pd.read_csv('diabetes.csv')
df_new = df[(df.BloodPressure!=0) & (df.BMI!=0) & (df.Glucose!=0)]
#feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 
#                 'SkinThickness', 'Insulin', 'BMI', 
#                 'DiabetesPedigreeFunction', 'Age']

feature_names = ['Glucose', 'BloodPressure', 
                 'Insulin', 'BMI', 
                 'Age']
features = df_new[feature_names]
label = df_new.Outcome
X_train, X_test, y_train, y_test = train_test_split(features, label, stratify=df_new.Outcome, test_size=0.3, random_state=42)

regr = LogisticRegression()
regr.fit(X_train, y_train)
#print (regr.predict([[1,93,70,31,0,30.4,0.315,23]]))
pickle.dump(regr, open('model.pkl', 'wb'))

ans = regr.predict(X_test)
print ('MSE: ',mean_squared_error(y_test, ans))
print ('Accuracy: ',accuracy_score(y_test, ans))