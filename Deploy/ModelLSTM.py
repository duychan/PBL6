from keras.models import load_model
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

from sklearn.base import BaseEstimator, TransformerMixin
model_LSTM = load_model('LSTM_model.h5')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
class LSTM_Model(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        X = tokenizer.texts_to_sequences(X)
        X = pad_sequences(X, maxlen=600, truncating='post', padding='post')
        y_predict=model_LSTM.predict(X)
        ypre=[]
        for i in y_predict:
            if i>0.5:
                ypre.append('real')
            else:
                ypre.append('fake')
        X=ypre
        return X
    def predict(self, X):
        X = tokenizer.texts_to_sequences(X)
        X = pad_sequences(X, maxlen=600, truncating='post', padding='post')
        y_predict=model_LSTM.predict(X)
        ypre=[]
        for i in y_predict:
            if i>0.5:
                ypre.append('real')
            else:
                ypre.append('fake')
        X=ypre
        return X
    def predict_proba(self, X):
        X = tokenizer.texts_to_sequences(X)
        X = pad_sequences(X, maxlen=600, truncating='post', padding='post')

        y_predict=model_LSTM.predict(X)
        y_pro=[]
        for i in y_predict:
            y_pro.append([1-i[0],i[0]])
        X=y_pro     
        return X
