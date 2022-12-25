from sklearn.base import BaseEstimator, TransformerMixin
from gensim.models import Word2Vec
import pandas as pd
import numpy as np
skipgram = Word2Vec.load('../w2v_pretrained/w2vtrain300.bin')


class TextToVec(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        W2Vec_Data = pd.DataFrame()
        for i in X:
            Sentence = np.zeros(300)
            WordsVocab = str(i).split()
            for word in WordsVocab:
                try:
                    Sentence = Sentence+skipgram.wv[word]
                except:
                    Sentence = Sentence+np.zeros(300)
            Sentence = Sentence/len(WordsVocab)
            W2Vec_Data = W2Vec_Data.append(pd.DataFrame([Sentence]))
        X = W2Vec_Data
        return X
