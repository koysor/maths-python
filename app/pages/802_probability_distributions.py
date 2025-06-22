import streamlit as st

st.set_page_config(layout="wide")

st.markdown("### Probability Distributions")

st.write(
    "Probability distributions describe how the values of a random variable are distributed. "
    "They can be classified into two main categories: discrete and continuous distributions."
)


st.markdown("##### Probability Density Function (PDF)")
st.write(
    "A PDF denoted $$f(x)$$ can be used to generate the probability that outcomes of a continuous distribution "
    "lie within a particular range of outcomes."
)


st.markdown("##### Cumulative Distribution Functions (CDF)")
st.write(
    "In simplete terms, the CDF sums up the probabillities of all possible outcomes up to a certain point. "
    "It gives the probability that a random variable is less than or equal to a certain value."
)
