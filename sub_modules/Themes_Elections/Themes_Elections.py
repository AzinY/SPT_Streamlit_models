

import pickle
import pandas as pd
#from spt_preproc import PreprocText
#tp = PreprocText()
from sentence_transformers import SentenceTransformer
encoder = SentenceTransformer('intfloat/multilingual-e5-large')

with open('LR_Elections_Theme.pickle', 'rb') as f:
    clf = pickle.load(f)
    
with open('pca_transformer.pickle', 'rb') as f:
    pca = pickle.load(f)
    
    
    
    
def Elections_theme_classify(texts):

    if isinstance(texts, str):
        #emb = encoder.encode(tp.clean_text(texts))
        emb = encoder.encode(texts)
        
        prediction = clf.predict(pca.transform([emb]))
        
        return list(map(lambda x: 'Верно!' if x==1 else 'Не верно!', prediction))[0]
    
    return 'Введите Текст!'
