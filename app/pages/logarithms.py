import streamlit as st

st.set_page_config(layout="wide")
st.markdown("### Logarithms")
st.write("Logarithms, or logs, are a way of expressing numbers in terms of their powers.")

col1, col2 = st.columns(2)

with col1:

    latex_code = r"""
    \log_a{b} = x \iff a^x = b
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.info("$$a$$ is the base of the logarithm, $$b$$ is the number you want to find the log of, and $$x$$ is the exponent to which the base must be raised to produce that number.")

with col2:

    col1, col2 = st.columns(2)

    with col1:
        a = st.number_input("Enter a value for a:", value=2, step=1)

    with col2:
        b = st.number_input("Enter a value for b:", value=8, step=1)
        
    latex_code = f"""
    \\log_{a}{b} = x \\iff {a}^x = {b}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)