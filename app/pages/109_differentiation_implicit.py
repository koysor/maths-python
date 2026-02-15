import streamlit as st

st.set_page_config(page_title="Differentiation Implicit", page_icon="📐", layout="wide")
st.header("Differentiation Implicit")


col1, col2 = st.columns([4, 3])

with col1:
    st.write(
        "**Implicit Differentiation** is a technique used to find the derivative of a function which is not explcitly expressed as **$$y = f(x)$$**. Instead, the function is given in an implicit form, such as **$$F(x, y) = 0$$**. In this case, we can use implicit differentiation to find the derivative of **$$y$$** with respect to **$$x$$**."
    )

    st.write("**Example:**")
    st.latex(r"""
        \begin{align*}
            x^2 + y^2 &= 25 \\

        \end{align*}
    """)

    st.write("**Step 1:** Differentiate both sides with respect to **$$x$$**.")
    latex_code = r"""
        \frac{d}{dx}(x^2) + \frac{d}{dx}(y^2) = \frac{d}{dx}(25)
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("**Step 2:** Apply derivatives.")
    latex_code = r"""
        2x + 2y \frac{dy}{dx} = 0
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("**Step 3:** Solve for **$$\\frac{dy}{dx}$$**.")
    latex_code = r"""
        2y \frac{dy}{dx} = -2x \\
        ~ \\
        \frac{dy}{dx} = -\frac{x}{y}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write(
        "The final result provides the **slope of the tangent line** at any point on the curve defined by the implicit equation. This is useful for finding the slope of curves that are not easily expressed in explicit form."
    )
    st.write(
        "**Note:** The implicit differentiation process is similar to the standard differentiation process, but it requires the use of the chain rule when differentiating terms involving **$$y$$**."
    )

with col2:
    st.video(
        "https://www.youtube.com/watch?v=FPFrDxl8GxQ&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=98&pp=iAQB"
    )
