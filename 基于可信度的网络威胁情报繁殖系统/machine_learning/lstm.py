import os
import numpy as np

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM


basepath=os.path.abspath(os.path.dirname(__file__))
data = pd.read_csv(basepath+'/train_data.csv')
data= data.sample(frac = 1)
input_len =data.shape[0]
tsteps = 2
lahead = data.shape[1]-2
batch_size = 1000
epochs = 10

row=data.shape[0]
col=data.shape[1]

features=data.iloc[:,1:col-1]
labels=data.iloc[:,col-1]




def split_data(x, y, ratio=1):
    to_train = int(input_len * ratio)
    # tweak to match with batch_size
    to_train -= to_train % batch_size

    x_train = x[:to_train]
    y_train = y[:to_train]
    x_test = x[to_train:]
    y_test = y[to_train:]

    # tweak to match with batch_size
    to_drop = x.shape[0] % batch_size
    if to_drop > 0:
        x_test = x_test[:-1 * to_drop]
        y_test = y_test[:-1 * to_drop]

    # some reshaping
    reshape_3=lambda x: x.values.reshape((x.shape[0], x.shape[1], 1))
    x_train = reshape_3(x_train)
    x_test = reshape_3(x_test)
    reshape_2 = lambda x: x.values.reshape((x.shape[0], 1))
    y_train = reshape_2(y_train)
    y_test = reshape_2(y_test)
    return (x_train, y_train), (x_test, y_test)

def lstm():
    (x_train, y_train), (x_test, y_test) = split_data(features,labels)
    model = Sequential()
    model.add(LSTM(20,
                   input_shape=(lahead, 1),
                   batch_size=batch_size,
                   stateful=False))
    model.add(Dense(1))
    model.compile(loss='mse', optimizer='adam')

    print('Training')
    for i in range(epochs):
        print('Epoch', i + 1, '/', epochs)
        model.fit(x_train,
                  y_train,
                  batch_size=batch_size,
                  epochs=1,
                  verbose=1,
                  shuffle=False)

        model.reset_states()

    model.save('machine_learning/my_model.h5')
    
