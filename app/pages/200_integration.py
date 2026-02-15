import streamlit as st

st.set_page_config(page_title="Integration", page_icon="📐", layout="wide")
st.header("Integration")


col1, col2 = st.columns([4, 3])

with col1:
    summary_integration = """
    Integration is the **opposite** of differentiation.
    \nFor a given function $$f(x)$$, integration is used to find the area under the curve of the function between two points on the x-axis.
    """
    st.info(summary_integration)

with col2:
    st.video(
        "https://www.youtube.com/watch?v=ni1DFNQnFJw&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=101"
    )


st.markdown("####  Indefinite and Definite Integration")

st.write(
    "In **Indefinite Integration**, the purpose is to find a general form of the original function whose derivative is the integrand.  "
    "No limits of integration are specified and the result is a function plus a constant of integration, $$C$$."
)

st.write(
    "In **Definite Integration**, No $$+ C$$ is added, because the constant of integration is not needed.  "
    "Limits of integration are given and the result is a number, representing the area under the curve between those limits."
)


st.markdown("#### Indefinite Integration")

st.write(
    """Indefinite integration, the opposite of differentiation, 
is used to determine the **original function** which was differentiated in order to obtain the current function."""
)

st.write("Rule to integrate terms which are written in the form of $$ax^n$$:")

latex_code = r"""
\int ax^n \,dx = \frac{a}{n+1}x^{n+1} + C
"""
st.code(latex_code, language="latex")
st.latex(latex_code)
st.write("$$\int$$ is the symbol for integration.")
st.write("We increase the power of x by 1 and then divide by the new power.")
st.write(
    "Add $$C$$ which is the constant of integration.  When we differentiate, any constant terms will disapper.  Therefore many functions have the same derivative."
)
st.write(
    "When we integrate, we need to add a constant term to the function to account for this."
)

st.write("Working example of indefinite integration:")

latex_code = r"""
\int 6x + 1 \,dx \\
"""
st.code(latex_code, language="latex")
st.latex(latex_code)

st.write("We can split the integral into two parts:")
st.write("Term 1:")
latex_code = r"""
\begin{align*}
    \int 6x \,dx &= \frac{6}{1+1}x^{1+1} \\
    ~\\
    &= 3x^2
\end{align*}"""
st.code(latex_code, language="latex")
st.latex(latex_code)

st.write("Term 2:")
latex_code = r"""
\int 1 \,dx = x \\
"""
st.code(latex_code, language="latex")
st.latex(latex_code)

st.write("Combine the two terms and add the constant of integration C:")
latex_code = r"""
\begin{align*}
&= \frac{6}{1+1}x^{1+1} + x + C \\
~\\
&= 3x^2 + x + C
\end{align*}
"""
st.code(latex_code, language="latex")
st.latex(latex_code)


st.markdown("#### Definite Integration")

st.write(
    """Definite integration is used to obtain a **numerical answer** for the area under the curve of a function between two points on the x-axis."""
)

col1, col2 = st.columns([4, 3])

with col1:
    st.write("Example of a definite integral: Integrate (6x + 1) from 2 to 5.")
    latex_code = """
    \int_{2}^{5} (6x + 1) \,dx
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write(
        "Integrate to obtain the integral.  The limits are displayed next to the square brackets."
    )

    latex_code = """
    = [3x^2 + x]_2^5
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    latex_code = r"""
    \begin{align*}
        &= (3 \times 5^2 + 5) - (3 \times 2^2 + 2) \\
        ~ \\
        &= 80 - 14 \\
        ~ \\
        &= 66
    \end{align*}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("")

with col2:
    st.video(
        "https://www.youtube.com/watch?v=Sp_KWTdBRsE&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=101&pp=iAQB"
    )
