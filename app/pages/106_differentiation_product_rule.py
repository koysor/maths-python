import streamlit as st

st.set_page_config(layout="wide")
st.markdown("### Differentiation Product Rule")


col1, col2 = st.columns([4, 3])

with col1:
    st.write(
        "The **Product Rule** allows you to differentiate two functions which are multiplied together."
    )
    st.write(
        "An example of a formula that can be differentiated using the Product Rule is:"
    )

    latex_code = r"""
    y = e^x (x^2 - 2)
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("Where **u** represents the part of the above function:")

    latex_code = r"""
    u = e^x
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("Where **v** represents the part of the above function:")

    latex_code = r"""
    v = (x^2 - 2)
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("The **Product Rule** is")
    latex_code = r"""
    \frac{dy}{dx} = u \cdot \frac{dv}{dx} + v \cdot \frac{du}{dx}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("Worked example:")

    latex_code = r"""
    y = x^4 \ln 3x
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    latex_code = r"""
    u = x^4 \\
    v = \ln 3x \\
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("Differentiate **u** and **v** separately.")
    latex_code = r"""
    \frac{du}{dx} = 4x^3 \\ 
    \frac{dv}{dx} = \frac{1}{x} \\ 
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("Resulting in:")
    latex_code = r"""
    \frac{dy}{dx} = u \cdot \frac{dv}{dx} + v \cdot \frac{du}{dx} \\
    = x^4 \cdot \frac{1}{x} + \ln 3x \cdot 4x^3 \\
    = x^3 + 4x^3 \ln 3x
    = x^3(1 + 4 \ln 3x)
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

with col2:
    st.video(
        "https://www.youtube.com/watch?v=51j5A5JrCwA&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=92&pp=iAQB"
    )
