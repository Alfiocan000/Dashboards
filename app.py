import streamlit as st
import pandas as pd
import numpy as np

st.title('My First Streamlit Dashboard')

st.write("Here's a simple example of a Streamlit app")

# Create a random dataframe
df = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c'])

st.line_chart(df)

# Add some interactive widgets
if st.checkbox('Show dataframe'):
    st.write(df)

number = st.slider('Pick a number', 0, 100)
st.write(f'You selected: {number}')
