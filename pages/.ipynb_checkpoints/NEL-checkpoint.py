

import sys
sys.path.append('/Users/az/Python Files/SPT/DSTeam/Azin/Streamlit/sub_modules/NEL')

import streamlit as st
import pickle
import nel_model


with open(f'/Users/az/Python Files/SPT/DSTeam/Azin/Streamlit/sub_modules/NEL/ready_entities_100k.pickle', 'rb') as f:
    entities = pickle.load(f)

st.title('NEL model')


txt = st.text_area(
    "Введите текст",
    "Энтропи́я (от др.-греч. ἐν «в» + τροπή «обращение; превращение») — широко используемый в естественных и точных науках термин (впервые введён в рамках термодинамики как функция состояния термодинамической системы), обозначающий меру необратимого рассеивания энергии или бесполезности энергии (потому что не всю энергию системы можно использовать для превращения в какую-нибудь полезную работу). Для понятия энтропии в данном разделе физики используют название термодинамическая энтропия; термодинамическая энтропия обычно применяется для описания равновесных (обратимых) процессов."
    )

nel = nel_model.NELModel(entities, 'entities').process_text
result_entities = nel(txt)

text_response = ''
for item in result_entities:
    text_response += item[0]
    text_response += '\n'
    text_response += item[1]
    text_response += '\n'
    text_response += '*'*99

st.text_area('Результат', text_response)



