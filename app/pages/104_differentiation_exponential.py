import streamlit as st


st.set_page_config(layout="wide")
st.markdown("### Differentiating Exponential Functions")


col1, col2 = st.columns([4, 3])

with col1:
    function_type = st.radio(
        label="Function Type:", options=["Exponential", "Natural Logarithm"]
    )
    st.write(function_type)

    if function_type == "Exponential":
        st.write(
            "The derivative of an exponential function is the same as the function itself."
        )
        latex_code = r"""
        \frac{d}{dx} (\exp x) = e^x
        """
        st.code(latex_code, language="latex")
        st.latex(latex_code)

        code_snippet = """
import streamlit as st
import sympy as sp
x = sp.symbols('x')
# Define the function
f = sp.exp(x)
# Differentiate
f_derivative = sp.diff(f, x)
st.write('The derivative of $$e^x$$ is:')
st.write(f_derivative)"""

        st.code(code_snippet)
        exec(code_snippet)

    elif function_type == "Natural Logarithm":
        st.write(
            "The derivative of a natural logarithm function is the reciprocal of the function."
        )
        latex_code = r"""
        \frac{d}{dx} (ln x) = \frac{1}{x}
        """
        st.code(latex_code, language="latex")
        st.latex(latex_code)

        code_snippet = """
import streamlit as st
import sympy as sp
x = sp.symbols('x')
# Define the function
f = sp.ln(x)
# Differentiate
f_derivative = sp.diff(f, x)
st.write('The derivative of $$ln(x)$$ is:')
st.write(f_derivative)"""

        st.code(code_snippet)
        exec(code_snippet)

with col2:
    st.video(
        "https://www.youtube.com/watch?v=MTGKaRwVh7M&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=89&pp=iAQB"
    )