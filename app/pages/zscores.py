import streamlit as st
from scipy.stats import zscore

st.set_page_config(layout="wide")
st.markdown("### Z-Scores")

st.write(
    "A Z-score indicates how many standard deviations an element is from the mean."
)

st.write("Example:")

data = [10, 20, 30, 40, 50]
st.write(data)

z_scores = zscore(data)
st.write(list(z_scores))
