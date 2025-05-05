import streamlit as st


st.set_page_config(layout="wide")
st.markdown("### Differentiation Power Rule")


st.markdown("#### The Power Rule")

col1, col2 = st.columns([4, 3])

with col1:

    st.write(
        """The Power Rule is a basic rule of differentiation that allows you to differentiate polynomial functions.
    It states that if you have a function of the form:"""
    )

    latex_code = r"""
    f(x) = x^n
    """
    st.latex(latex_code)
    st.write(
        """where $$n$$ is a constant, then the derivative of $$f(x)$$ with respect to $$x$$ is given by:"""
    )

    latex_code = r"""
    \frac{d}{dx} (x^n) = n \cdot x^{n-1}
    """
    st.latex(latex_code)

    n = st.number_input("Enter a value for n:", value=2, step=1)

    code_snippet = f"""
import streamlit as st
import sympy as sp
x = sp.symbols('x')
# Define the function
f = x**{n}
# Differentiate
f_derivative = sp.diff(f, x)
st.write('The derivative of $$x^{n}$$ is:')
st.write(f_derivative)
"""
    st.code(code_snippet)
    exec(code_snippet)

    st.write(
        "The output from the sympy.diff function is consistent with the workings above but rearranged."
    )