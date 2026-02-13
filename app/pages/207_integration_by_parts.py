import streamlit as st

st.set_page_config(layout="wide")
st.markdown("### Integration by Parts")


col1, col2 = st.columns([4, 3])

with col1:

    st.write(
        "Integrations by partys is used to integrate the product of two functions."
    )

    latex_code = r"""
    \int u \frac{dv}{dx} \, dx = uv - \int v \frac{du}{dx} \, dx
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)
    st.write(
        "Where $$u$$ and $$v$$ are functions of $$x$$.  The function $$u$$ is chosen to be the function which is easier to differentiate."
    )
    st.write(r"$$u \frac{dv}{dx}$$ is the function which is being integrated.")
    st.write(
        r"We must determine which part of the function is $$u$$ and which part is $$\frac{dv}{dx}$$."
    )

    st.write("Example use integration by parts to find the integral:")
    latex_code = r"""
    \int x \sin{3x} \, dx
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    latex_code = r"""
    u = x \\
    \frac{dv}{dx} = \sin{3x} \\
    \frac{du}{dx} = 1 \\
    v = -\frac{1}{3} \cos{3x}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)
    st.write(
        "We can now substitute these values into the integration by parts formula."
    )

    st.write("Then:")
    latex_code = r"""
    \int x \sin{3x} \, dx \\
    = (x)(-\frac{1}{3} \cos{3x}) - \int (-\frac{1}{3} \cos{3x})(1) \, dx \\
    = -\frac{1}{3} x \cos{3x} + \frac{1}{3} \int \cos{3x} \, dx \\
    = -\frac{1}{3} x \cos{3x} + \frac{1}{9} \sin{3x} + C
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

with col2:
    st.video(
        "https://www.youtube.com/watch?v=_62XWRgZwGA&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=110&pp=iAQB"
    )
