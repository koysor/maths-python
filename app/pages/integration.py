import streamlit as st


st.set_page_config(layout="wide")
st.markdown("### Integration")


col1, col2 = st.columns([4,3])

with col1:
    summary_integration = """
    Integration is the opposite of differentiation.
    \nFor a given function f(x), integration is used to find the area under the curve of the function between two points on the x-axis.
    """
    st.info(summary_integration)

with col2:
    st.video("https://www.youtube.com/watch?v=ni1DFNQnFJw&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=101")


st.markdown("#### Indefinite Integration")

st.write("""Indefinite integration, the opposite of differentiation, 
is used to determine the original function which was differentiated in order to obtain the current function.""")


st.markdown("#### Definite Integration")

st.write("""Definite integration is used to obtain a numerical answer for the area under the curve of a function between two points on the x-axis.""")

col1, col2 = st.columns([4,3])

with col1:
    st.write("Example of a definite integral: Integrate (6x + 1) from 2 to 5.")
    latex_code = """
    \int_{2}^{5} (6x + 1) \,dx
    """
    st.latex(latex_code)

    st.write("Integrate to obtain the integral.  The limits are displayednext to the square brackets.")

    latex_code = """
    = [3x^2 + x]_2^5
    """
    st.latex(latex_code)

    latex_code = r"""
    = (3 \times 5^2 + 5) - (3 \times 2^2 + 2)
    = 80 - 14
    = 66
    """
    st.latex(latex_code)

    st.write("")

with col2:
    st.video("https://www.youtube.com/watch?v=Sp_KWTdBRsE&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=101&pp=iAQB")


st.markdown("#### Integration Example with SymPy")

st.write("To calculate the definite integral:")

latex_code = """
\int_{2}^{5} (6x + 1) \,dx
"""
st.latex(latex_code)

st.write("The SymPy library in Python can be used...")

code_snippet = """
from sympy import symbols, integrate

x = symbols("x")

f = 6*x + 1

# Calculate the definite integral from 2 to 5
st.write(integrate(f, (x, 2, 5)))
"""

st.code(code_snippet)
exec(code_snippet)


st.markdown("#### Parametric Integrals")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("https://www.youtube.com/watch?v=p6YBlqon8TE&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=102&pp=iAQB")


st.markdown("#### Integration with Exponentials and Logarithms")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("https://www.youtube.com/watch?v=i3uX8VTZz6s&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=104&pp=iAQB")


st.markdown("#### Integrating Trigonometric Functions")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("https://www.youtube.com/watch?v=XKXWTaL8JUY&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=105&pp=iAQB")


st.markdown("#### Reverse Chain Rule")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("https://www.youtube.com/watch?v=q8o5zVQiajM&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=107&pp=iAQB")


st.markdown("#### Integration by Substitution")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("https://www.youtube.com/watch?v=l9s0ROOBocA&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=109&t=204s&pp=iAQB")


st.markdown("#### Integration by Parts")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("https://www.youtube.com/watch?v=_62XWRgZwGA&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=110&pp=iAQB")


st.markdown("#### Numerical Integration")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("")





st.markdown("#### ")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("")


st.markdown("#### ")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("")


st.markdown("#### ")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("")
    


st.markdown("#### ")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("")