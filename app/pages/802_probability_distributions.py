import streamlit as st

st.set_page_config(layout="wide")

st.markdown("### Probability Distributions")

st.write(
    "Probability distributions describe how the values of a random variable are distributed. They can be classified into two main categories: discrete and continuous distributions."
)


st.markdown("##### Probability Distribution Function (PDF)")
st.write(
    "The probability distribution function (PDF) describes the likelihood of a random variable taking on a specific value. For discrete random variables, the PDF is represented as a probability mass function (PMF), while for continuous random variables, it is represented as a probability density function (PDF)."
)


st.markdown("##### Cumulative Distribution Functions (CDF)")
st.write(
    "In simplete terms, the CDF sums up the probabillities of all possible outcomes up to a certain point. It gives the probability that a random variable is less than or equal to a certain value."
)
st.write(
    "The cumulative distribution function (CDF) describes the probability that a random variable takes on a value less than or equal to a specific value. It is defined as the integral of the PDF from negative infinity to the specific value."
)
