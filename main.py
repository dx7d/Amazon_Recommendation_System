import streamlit as st
import recommend
import pandas as pd

st.title('Amazon Recommender System')
st.subheader('This Model takes Product ID from the user as the input and returns top 10 Recommended Item\'s') 
#a = recommend.result('B00065ANY2')

text = st.text_input('Enter ProductID: (eg: B00065ANY2)')

a = recommend.result(text)

for i,j in a.items():
    st.markdown(f'{i} - {j}')

    