import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split

df=pd.read_csv('prajwaldeploy_df.csv')

df.drop('Unnamed: 0',axis=1,inplace=True)

x=df.drop('Price',axis=1)
print(x.head())

y=df['Price']

#splitting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 50)



from catboost import CatBoostRegressor

cat=CatBoostRegressor()
cat.fit(X_train,y_train)

y_predict=cat.predict(X_test)

#Use pickle to save our model so that we can use it later

from typing import BinaryIO
import pickle
import pickle
# Saving model
pickle.dump(cat, open('prajwalmodel.pkl','wb'))
model=pickle.load(open('prajwalmodel.pkl','rb'))
print(y_predict)

