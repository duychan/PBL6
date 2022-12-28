from fastapi.middleware.cors import CORSMiddleware
import pickle
from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import numpy as np

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Content(BaseModel):
    content: str


@app.get("/")
def home():
    return {"home": "ok"}


@app.post("/predict_svm/")
async def pred(content: Content):
    SVM_model = pickle.load(open("../Model_SVM/model_svm.sav", "rb"))
    output = SVM_model.predict(content.content)
    conf = np.max(SVM_model.predict_proba(content.content))
    return {"result": (output[0]) if output is not None else None, "confidence": np.round(conf * 100, 2)}


@app.post("/predict_knn/")
async def pred(content: Content):
    KNN_model = pickle.load(open("../Model_KNN/Word2Vec_pickle_KNN.pkl", "rb"))
    output = KNN_model.predict(content.content)
    conf = np.max(KNN_model.predict_proba(content.content))
    return {"result": (output[0]) if output is not None else None, "confidence": np.round(np.max(conf) * 100, 2)}


@app.post("/predict_nb/")
async def pred(content: Content):
    NB_model = pickle.load(open("../Model_NB/Word2Vec_pickle_NB.pkl", "rb"))
    output = NB_model.predict(content.content)
    conf = np.max(NB_model.predict_proba(content.content))
    return {"result": (output[0]) if output is not None else None, "confidence": np.round(np.max(conf) * 100, 2)}



@app.post("/predict_lstm/")
async def pred(content: Content):
    LSTM_model = pickle.load(open("../Model_LSTM/LSTM_pickle.pkl", "rb"))
    output = LSTM_model.predict(content.content)
    conf = np.max(LSTM_model.predict_proba(content.content))
    return {"result": (output[0]) if output is not None else None, "confidence": np.round(np.max(conf) * 100, 2)}

