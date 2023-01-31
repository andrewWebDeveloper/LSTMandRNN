# -*- coding: utf-8 -*-
"""LSTM_AND_RNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19LPYZVY0W6nlr2FpRTaCR_eHiX-c6MUo
"""

#importing the necessary libraries and dependencies
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from numpy import array
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras import optimizers
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

df=pd.read_csv("/content/city_day.csv")
df1=pd.read_csv("/content/city_hour.csv")
df2=pd.read_csv("/content/station_day.csv")

df1.head()

df2.head()



df.head(100)

print(df.describe())

df.isnull().sum()

df['PM2.5'].fillna(method = 'bfill',inplace = True )
df['PM10'].fillna(method = 'bfill',inplace = True )
df['NO'].fillna(method = 'ffill',inplace = True )
df['NO2'].fillna(method = 'ffill',inplace = True )
df['NOx'].fillna(method = 'ffill',inplace = True )
df['NH3'].fillna(method = 'bfill',inplace = True )
df['CO'].fillna(method = 'ffill',inplace = True )
df['SO2'].fillna(method = 'ffill',inplace = True )
df['O3'].fillna(method = 'ffill',inplace = True )
df['Benzene'].fillna(method = 'ffill',inplace = True )
df['Toluene'].fillna(method = 'ffill',inplace = True )
df['Xylene'].fillna(method = 'ffill',inplace = True )
df['AQI'].fillna(method = 'bfill',inplace = True )
df['AQI_Bucket'].fillna(method = 'bfill',inplace = True )

df1['PM2.5'].fillna(method = 'bfill',inplace = True )
df1['PM10'].fillna(method = 'bfill',inplace = True )
df1['NO'].fillna(method = 'ffill',inplace = True )
df1['NO2'].fillna(method = 'ffill',inplace = True )
df1['NOx'].fillna(method = 'ffill',inplace = True )
df1['NH3'].fillna(method = 'bfill',inplace = True )
df1['CO'].fillna(method = 'ffill',inplace = True )
df1['SO2'].fillna(method = 'ffill',inplace = True )
df1['O3'].fillna(method = 'ffill',inplace = True )
df1['Benzene'].fillna(method = 'ffill',inplace = True )
df1['Toluene'].fillna(method = 'ffill',inplace = True )
df1['Xylene'].fillna(method = 'ffill',inplace = True )
df1['AQI'].fillna(method = 'bfill',inplace = True )
df1['AQI_Bucket'].fillna(method = 'bfill',inplace = True )

df2['PM2.5'].fillna(method = 'bfill',inplace = True )
df2['PM10'].fillna(method = 'bfill',inplace = True )
df2['NO'].fillna(method = 'ffill',inplace = True )
df2['NO2'].fillna(method = 'ffill',inplace = True )
df2['NOx'].fillna(method = 'ffill',inplace = True )
df2['NH3'].fillna(method = 'bfill',inplace = True )
df2['CO'].fillna(method = 'ffill',inplace = True )
df2['SO2'].fillna(method = 'ffill',inplace = True )
df2['O3'].fillna(method = 'ffill',inplace = True )
df2['Benzene'].fillna(method = 'ffill',inplace = True )
df2['Toluene'].fillna(method = 'ffill',inplace = True )
df2['Xylene'].fillna(method = 'ffill',inplace = True )
df2['AQI'].fillna(method = 'bfill',inplace = True )
df2['AQI_Bucket'].fillna(method = 'bfill',inplace = True )

df.isnull().sum()

def city_wise_pollution_based(quality,color):
    a=df[[quality, 'City']].groupby(['City']).median().sort_values(quality, ascending = False)
    a.plot.bar(color=color,figsize=(12,4))
    plt.legend(fontsize=20)
    plt.xticks(fontsize=15)
    plt.title("amount of concentaion of quality - CITY BASED "+"( " + quality + " )")
    plt.show()

city_wise_pollution_based('PM2.5','#CD6155')
city_wise_pollution_based('PM10','teal')
city_wise_pollution_based('NO2','#2980B9')
city_wise_pollution_based('NH3','#B9770E')
city_wise_pollution_based('CO','#283747')
city_wise_pollution_based('SO2','#99004d')
city_wise_pollution_based('O3','#002db3')
city_wise_pollution_based('Benzene','#00b38f')
city_wise_pollution_based('Toluene','#1f7a1f')
city_wise_pollution_based('Xylene','#662200')
print("plots")

df["AQI_Bucket"]=df["AQI_Bucket"].replace({'Poor':4, 'Very Poor':5, 'Severe':6,'Moderate':3,'Satisfactory':2, 'Good':1})
df1["AQI_Bucket"]=df1["AQI_Bucket"].replace({'Poor':4, 'Very Poor':5, 'Severe':6,'Moderate':3,'Satisfactory':2, 'Good':1})
df2["AQI_Bucket"]=df2["AQI_Bucket"].replace({'Poor':4, 'Very Poor':5, 'Severe':6,'Moderate':3,'Satisfactory':2, 'Good':1})

df["AQI_Bucket"].unique()  
df1["AQI_Bucket"].unique()   
df2["AQI_Bucket"].unique()

df.head()

df.info()

x=df.drop(columns=["Date","City",'AQI_Bucket'],axis=1)
y=df['AQI_Bucket']

x1=df1.drop(columns=["Datetime","City",'AQI_Bucket'],axis=1)
y1=df1['AQI_Bucket']

x2=df2.drop(columns=["Date","StationId",'AQI_Bucket'],axis=1)
y2=df2['AQI_Bucket']

x.info()

y.head()

from sklearn.model_selection import train_test_split
from keras.optimizers import SGD
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, GRU, Bidirectional
from keras.optimizers import SGD
import math
from sklearn.metrics import mean_squared_error

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=11)
y_train.shape,X_train.shape,y_test.shape,X_test.shape

X_train1, X_test1, y_train1, y_test1 = train_test_split(x1, y1, test_size=0.30, random_state=11)
y_train1.shape,X_train1.shape,y_test1.shape,X_test1.shape

X_train2, X_test2, y_train2, y_test2 = train_test_split(x2, y2, test_size=0.30, random_state=11)
y_train2.shape,X_train2.shape,y_test2.shape,X_test2.shape

"""LSTM IMPLEMENTION

"""

modellstm = Sequential()
modellstm.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1],1)))
modellstm.add(Dropout(0.2))
modellstm.add(LSTM(units=50, return_sequences=True))
modellstm.add(Dropout(0.2))
modellstm.add(LSTM(units=50, return_sequences=True))
modellstm.add(Dropout(0.2))
modellstm.add(LSTM(units=50))
modellstm.add(Dropout(0.2))
modellstm.add(Dense(units=1))

modellstm.compile(optimizer='rmsprop',loss='mean_squared_error',metrics=['accuracy'])
modellstm.fit(X_train,y_train,epochs=10,batch_size=32)

modellstm.compile(optimizer='rmsprop',loss='mean_squared_error',metrics=['accuracy'])
modellstm.fit(X_train1,y_train1,epochs=10,batch_size=32)

modellstm.compile(optimizer='rmsprop',loss='mean_squared_error',metrics=['accuracy'])
modellstm.fit(X_train2,y_train2,epochs=10,batch_size=32)

X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0],X_test.shape[1],1))
predicted = modellstm.predict(X_test)
predicted