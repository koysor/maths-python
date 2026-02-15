import streamlit as st

st.set_page_config(
    page_title="Differentiation of Parametric Equations", page_icon="📐", layout="wide"
)
st.header("Differentiation of Parametric Equations")


st.markdown("##### What is a Parametric Equation?")
st.write(
    """A **parametric equation** is an equation that expresses a set of related variables as functions of an **independent variable**, called a parameter - which is often denoted as **$$t$$**.
    \r\nE.g."""
)

latex_code = r"""
x = f(t) \\
y = g(t) \\
"""
st.code(latex_code, language="latex")
st.latex(latex_code)

st.write(
    "These are two **separate functions** that depend on the same parameter **$$t$$**."
)


st.markdown("#### Differentiating a Parametric Equation")

col1, col2 = st.columns([4, 3])

with col1:
    st.write(
        """This version of the **Chain Rule** is used to find the derivative of a function that is defined by **parametric equations**."""
    )
    st.write(
        """The formula gives you the derivative **in terms of $$t$$** and not in terms of $$x$$ or $$y$$."""
    )
    st.write(
        "You need to know the value of **$$t$$** for a particular point on the curve to find the gradient of the curve at that point."
    )

    st.write("Golden rule:")
    latex_code = r"""
    \frac{dy}{dx} = \frac{dy}{dt} \div \frac{dx}{dt}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("Worked example:")
    latex_code = r"""
    x = \sin^2t \\
    ~ \\
    y = 2 \tan t \\
    ~ \\
    0 \leq t \geq \frac{\pi}{2}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("In order to find the derivative in terms of $$t$$:")
    latex_code = r"""
    \frac{dx}{dt} = 2 \sin t \cos t \\
    ~ \\
    \frac{dy}{dt} = 2 \sec^2 t
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("Resulting in:")
    latex_code = r"""
    \frac{dy}{dx} = \frac{dy}{dt} \div \frac{dx}{dt} \\
    ~ \\
    = \frac{2\sec^2 t}{2\sin t \cos t} \\
    ~ \\
    = \frac{1}{\sin t \cos^3 t} \\
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.header("With SymPy")

    with open("app/pages/code_snippets/differentiation_parametric.py", "r") as f:
        code_snippet = f.read()

    st.code(code_snippet)
    exec(code_snippet)

    st.write(
        "The output from the sympy.diff function is consistent with the workings above but rearranged."
    )

with col2:
    st.video(
        "https://www.youtube.com/watch?v=wFFaBh2jG-8&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=97&pp=iAQB"
    )
