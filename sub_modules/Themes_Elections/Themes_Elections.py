
import os
import pickle
import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer


@st.cache
def load_model():
	  return SentenceTransformer('intfloat/multilingual-e5-large')


encoder = load_model()

@st.cache
def load_clf():
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__),'LR_Elections_Theme.pickle')), 'rb') as f:
       return pickle.load(f)

clf = load_clf()

@st.cache
def load_pca():
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__),'pca_transformer.pickle')), 'rb') as f:
        return pickle.load(f)
pca = load_pca() 
    
    
    
def Elections_theme_classify(texts):

    if isinstance(texts, str):
        #emb = encoder.encode(tp.clean_text(texts))
        emb = encoder.encode(texts)
        
        prediction = clf.predict(pca.transform([emb]))
        
        return list(map(lambda x: 'Верно!' if x==1 else 'Не верно!', prediction))[0]
    
    return 'Введите Текст!'

