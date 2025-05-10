import streamlit as st


st.set_page_config(layout="wide")
st.markdown("### Differentiation")

summary_differentiation = """
Differentiation is the process of finding the slope or rate of change of a function at a particular point.
\nThis is also known as the first derivative of a function or the gradient function.
\nThe second derivative is the rate at which the slope or first derivative is changing.
"""
st.info(summary_differentiation)


st.markdown("### Notation")

col1, col2 = st.columns(2)

with col1:
    st.write("""For a function $$y(x)$$""")

with col2:
    st.write("The rate of change of y with respect to x is denoted as:")
    latex_code = r"""
    \frac{dy}{dx}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)
    st.write("I.e. how quicky y changes as x changes.")


st.markdown("### Differentiating from First Principles")

col1, col2 = st.columns([4, 3])

with col1:
    st.write(
        """As the distance between two points on a curve approaches zero, 
    the slope of the line between the two points approaches the slope of the tangent line at a particular point on the curve."""
    )

    latex_code = r"""
    \frac{dy}{dx} = \lim_{h \to 0 } \frac{f(x+h)-f(x)}{h}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

with col2:
    st.video("https://www.youtube.com/watch?v=K8bVclWiEoM")


st.markdown("### Second Derivative")

col1, col2 = st.columns([4, 3])

with col1:
    st.write(
        "The second derivative is the rate at which the slope or first derivative is changing."
    )
    latex_code = r"""
    \frac{d^2y}{dx^2}
    """
    st.latex(latex_code)

with col2:
    st.video("https://www.youtube.com/watch?v=L9hU4xrhEDs")
