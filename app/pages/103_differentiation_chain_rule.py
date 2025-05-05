import streamlit as st


st.set_page_config(layout="wide")
st.markdown("### Differentiation Chain Rule")


col1, col2 = st.columns([4, 3])

with col1:
    st.write(
        "The chain rule is used to differentiate **composite functions**.  It allows you to differentiate a function nested within another function.  It is useful because it tells us how changes in the inner function affect the outer function."
    )
    latex_code = r"""
    y = f(g(x))
    """
    st.latex(latex_code)

    st.write("Example:")
    st.write("Substitute the inside function with u.")
    latex_code = r"""
    y = \sqrt{x^3 + 1} \\
    u = x^3 + 1 \\
    y = \sqrt{u} = u^{1/2}
    """
    st.latex(latex_code)

    st.write("Treat u as a single variable and differentiate.")
    latex_code = r"""
    \frac{dy}{du} = \frac{1}{2}u^{-1/2}
    """
    st.latex(latex_code)

    st.write("Replace u with the inside function.")
    latex_code = r"""
    \frac{dy}{du} = \frac{1}{2}(x^3 + 1)^{-1/2} \\
    = \frac{1}{2\times\sqrt{x^3 + 1}}
    """
    st.latex(latex_code)

    st.write("Multiply the result by the derivative of u.")
    latex_code = r"""
    \frac{du}{dx} = 3x^2 \\
    \frac{dy}{dx} = \frac{dy}{du} \times \frac{du}{dx} \\
    \frac{dy}{dx} = \frac{3x^2}{2\times\sqrt{x^3 + 1}}
    """
    st.latex(latex_code)

    code_snippet = """
from sympy import symbols, diff

x = symbols("x")
y = (x**3 + 1)**(1/2)

# Compute the derivative using chain rule
dy_dx = diff(y, x)

st.write(dy_dx)
    """
    st.code(code_snippet)
    exec(code_snippet)

    st.write(
        "The output from the sympy.diff function is consistent with the workings above but rearranged, e.g. with the 3/2 faction replaced with 1.5 in the numerator."
    )

with col2:
    st.video(
        "https://www.youtube.com/watch?v=9IAUw5brhf4&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=87&pp=iAQB"
    )