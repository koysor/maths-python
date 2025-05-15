import streamlit as st


st.set_page_config(layout="wide")
st.markdown("####Integration by Substitution")


col1, col2 = st.columns([4, 3])

with col1:
    st.write("Substitution is used to turn a complicated integral into a simpler one.")
    st.write(
        "Also known as the **Reverse Chain Rule** or **u-substitution** is used to simplify an integral, particularly when the integral contains a **composite** function."
    )

    st.write("Example, find the integral using substitution $$\,u = e^{3x}$$:")
    latex_code = r"""
    \int \frac{e^{3x}}{(e^{3x} +1)^2} \,dx
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

with col2:
    st.video(
        "https://www.youtube.com/watch?v=l9s0ROOBocA&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=109&t=204s&pp=iAQB"
    )

st.info(
    r"1. Find $$\frac{du}{dx}$$ and write an expression for $$dx$$ in the form $$f(x) ~ du$$."
)
st.write(r"$$u = e^{3x}$$")
st.write("Therefore:")
st.write(r"$$\frac{du}{dx} = 3e^{3x}$$")
st.write(
    r"$$dx$$ is equivalent to $$(\frac{1}{3e^{3x}}) ~ du$$.  Note that $$dx$$ is treated symbolically to be rearranged for substitution."
)
st.write(
    r"$$(\frac{1}{3e^{3x}}) ~ du$$ is now ex expression in the form of $$f(x) ~ du$$."
)

st.info("2. Swap $$dx$$ for $$f(x) ~ du$$ in the integral and simplify if possible.")
latex_code = r"""
\int \frac{e^{3x}}{(e^{3x} +1)^2} \,dx 
= \int \frac{\cancel{e^{3x}}}{(e^{3x} +1)^2} \left(\frac{1}{3\cancel{e^{3x}}}\right) ~ du
= \int \frac{1}{3(e^{3x} +1)^2} ~ du
"""
st.code(latex_code, language="latex")
st.latex(latex_code)

st.info("3. Substitute every $$x$$ to get an integral involving only $$u$$ and $$du$$.")
latex_code = r"""
= \int \frac{1}{3(u +1)^2} ~ du = \int \frac{1}{3} (u + 1)^{-2} ~ du
"""
st.code(latex_code, language="latex")
st.latex(latex_code)
st.write("The new integral should now be simpler to solve.")

st.info("4. Integrate with respect to $$u$$.")
latex_code = r"""
= \frac{1}{3} (u + 1)^{-1} + C
"""
st.code(latex_code, language="latex")
st.latex(latex_code)

st.info("5. Reverse the substitution to get the final answer in terms of x.")
latex_code = r"""
= - \frac{1}{3} (e^{3x} + 1)^{-1} + C
"""
st.code(latex_code, language="latex")
st.latex(latex_code)
