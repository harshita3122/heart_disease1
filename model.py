import pandas as pd
import matplotlib.pyplot as plt
import pickle
daatset=pd.read_csv(r"C:\Users\harshita\Desktop\New folder\heart.csv")
x=daatset.iloc[:,0:13]
y=daatset.iloc[:,13:14]

from sklearn.linear_model import LogisticRegression
regressor=LogisticRegression()
regressor.fit(x,y)
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[55,1,0,125,212,0,1,168,0,1,2,2,3]]))
