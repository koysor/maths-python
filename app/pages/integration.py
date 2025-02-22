import streamlit as st


st.set_page_config(layout="wide")
st.markdown("### Integration")

summary_integration = """
Integration is the opposite of differentiation.
\nFor a given function f(x), integration is used to find the area under the curve of the function between two points on the x-axis.
"""
st.info(summary_integration)


st.markdown("#### Indefinite Integration")

st.write("""Indefinite integration, the opposite of differentiation, 
is used to determine the original function which was differentiated in order to obtain the current function.""")


st.markdown("#### Definite Integration")

st.write("""Definite integration is used to obtain a numerical answer for the area under the curve of a function between two points on the x-axis.""")

col1, col2 = st.columns([4,3])

with col1:
    latex_code = """
    \int_{2}^{5} (6x + 1) \,dx
    """
    st.latex(latex_code)

    st.write("Integrate to obtain the integral:")

    latex_code = """
    [3x^2 + x]{2}^{5}
    """
    st.latex(latex_code)

with col2:
    st.video("https://www.youtube.com/watch?v=Sp_KWTdBRsE&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=101&pp=iAQB")


