import streamlit as st
import pandas as pd

df = pd.read_csv("tests/output/results.csv")
st.title("Lemmatizer Evaluation Results")
st.dataframe(df)
st.bar_chart(df['filename'].value_counts())