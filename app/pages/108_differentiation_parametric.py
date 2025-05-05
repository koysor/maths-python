import streamlit as st

st.set_page_config(layout="wide")
st.markdown("### Differentiation Parametric")


col1, col2 = st.columns([4, 3])

with col1:
    st.write(
        """This version of the **Chain Rule** is used to find the derivative of a function that is defined by **parametric equations**."""
    )
    st.write(
        """The formula gives you the derivative **in terms of t** and not in terms of x or y."""
    )
    st.write(
        "You need to know the value of **t** for a particular point on the curve to find the gradient of the curve at that point."
    )

    st.write("Golden rule:")
    latex_code = r"""
    \frac{dy}{dx} = \frac{dy}{dt} \div \frac{dx}{dt}
    """
    st.latex(latex_code)

    st.write("Worked example:")
    latex_code = r"""
    x = \sin^2t \\
    y = 2 \tan t \\
    0 \leq t \geq \frac{\pi}{2}
    """
    st.latex(latex_code)

    st.write("In order to find the derivative in terms of t:")
    latex_code = r"""
    \frac{dx}{dt} = 2 \sin t \cos t \\
    \frac{dy}{dt} = 2 \sec^2 t
    """
    st.latex(latex_code)

    st.write("Resulting in:")
    latex_code = r"""
    \frac{dy}{dx} = \frac{dy}{dt} \div \frac{dx}{dt} = \frac{2\sec^2 t}{2\sin t \cos t} \\
    = \frac{1}{\sin t \cos^3 t} \\
    """
    st.latex(latex_code)

    code_snippet = """
import streamlit as st
import sympy as sp

t = sp.symbols('t')
x = sp.sin(t)**2
y = 2 * sp.tan(t)

# Differentiate
dx_dt = sp.diff(x, t)
dy_dt = sp.diff(y, t)

st.write('The derivative of x with respect to t is:')
st.write(dx_dt)
st.write('The derivative of y with respect to t is:')
st.write(dy_dt)
st.write('The derivative of y with respect to x is:')
st.write(dy_dt/dx_dt)
    """
    st.code(code_snippet)
    exec(code_snippet)

    st.write(
        "The output from the sympy.diff function is consistent with the workings above but rearranged."
    )

with col2:
    st.video(
        "https://www.youtube.com/watch?v=wFFaBh2jG-8&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=97&pp=iAQB"
    )