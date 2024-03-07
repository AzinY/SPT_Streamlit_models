import sys
sys.path.append('/Users/az/Python Files/SPT/DSTeam/Azin/Streamlit/sub_modules/Themes_Elections')


import streamlit as st
from spt_preproc import PreprocText
tp = PreprocText()

#from sentence_transformers import SentenceTransformer
#encoder = SentenceTransformer('intfloat/multilingual-e5-large')

from Themes_Elections import Elections_theme_classify

st.title('Elections predictor')


txt = st.text_area(
    "Text to analyze",
    "Совсем скоро состоятся выборы президента Российской Федерации!",
    )

#st.write(f'You wrote {len(txt)} characters.')

#st.write(tp.clean_text(txt))

st.text_area('Результат:', Elections_theme_classify(txt))


