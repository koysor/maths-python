import streamlit as st

st.set_page_config(
    page_title="Differentiation Quotient Rule", page_icon="📐", layout="wide"
)
st.header("Differentiation Quotient Rule")


col1, col2 = st.columns([4, 3])

with col1:
    st.write(
        "When one function is divided by another function, the Quotient Rule is used to differentiate them."
    )
    st.write("The Golden rule, if:")

    latex_code = r"""
    y = \frac{u}{v}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("And **u** and **v** are both functions of x, then:")

    latex_code = r"""
    \frac{dy}{dx} = \frac{v \cdot \frac{du}{dx} - u \cdot \frac{dv}{dx}}{v^2}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("Worked example:")
    latex_code = r"""
    \begin{align*}
        y &= \frac{\sin 5x}{x^2} \\
        ~ \\
        u &= \sin 5x \\
        ~ \\
        v &= x^2 \\
    \end{align*}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("Differentiate **u** and **v** separately.")
    latex_code = r"""
    \begin{align*}
        \frac{du}{dx} &= 5 \cos 5x \\
        ~ \\
        \frac{dv}{dx} &= 2x \\
    \end{align*}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("Resulting in:")
    latex_code = r"""
    \begin{align*}
        \frac{dy}{dx} &= \frac{v \cdot \frac{du}{dx} - u \cdot \frac{dv}{dx}}{v^2} \\ 
        ~ \\
        &= \frac{x^2(5\cos 5x) - (\sin 5x)(2x)}{(x^2)^2} \\
    \end{align*}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("The final result is:")
    latex_code = r"""
    = \frac{5x \cos 5x - 2 \sin 5x}{x^3}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)


with col2:
    st.video(
        "https://www.youtube.com/watch?v=Cj9hiHBt1ss&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=94&t=8s&pp=iAQB"
    )


st.markdown("##### Alternatively use the Power Rule")

latex_code = r"""u = \frac {3}{x} = 3x^{-1}"""
st.code(latex_code, language="latex")
st.latex(latex_code)
