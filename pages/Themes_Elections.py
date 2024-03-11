import streamlit as st
import os
import sys

#from spt_preproc import PreprocText
#tp = PreprocText()

#from sentence_transformers import SentenceTransformer
#encoder = SentenceTransformer('intfloat/multilingual-e5-large')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','sub_modules', 'Themes_Elections')))
 
from Themes_Elections import Elections_theme_classify

st.title('Elections predictor')


txt = st.text_area(
    "Text to analyze",
    "Совсем скоро состоятся выборы президента Российской Федерации!",
    )

#st.write(f'You wrote {len(txt)} characters.')

#st.write(tp.clean_text(txt))

st.text_area('Результат:', Elections_theme_classify(txt))


