import streamlit as st
from sympy.parsing.latex import parse_latex

st.set_page_config(layout="wide")
st.markdown("### LaTeX Examples")

st.write(
    "LaTex is a markup language used for typsetting and often used for presenting mathematical and scientific documents.  \r\nFor reference purposes this page contians examples of mathematical notation expressed in LaTeX code."
)
st.write(
    "The LaTeX code is displayed in a code block, and the rendered LaTeX output is displayed below it."
)


def latex_to_sympy_and_print(latex_code):
    st.code(latex_code, language="latex")
    st.latex(latex_code)
    sympy_expression = parse_latex(latex_code)
    st.code(sympy_expression, language="sympy")


st.markdown("#### The Black-Scholes equation:")

latex_code = r"""
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - rV = 0
"""
latex_to_sympy_and_print(latex_code)


st.markdown("#### Itô's Lemma:")

latex_code = r"""
dX_t = \mu(X_t, t) dt + \sigma(X_t, t) dW_t \\
~\\
df = \left( \frac{\partial f}{\partial t} + \mu \frac{\partial f}{\partial x} + \frac{1}{2} \sigma^2 \frac{\partial^2 f}{\partial x^2} \right) dt + \sigma \frac{\partial f}{\partial x} dW_t.
"""
latex_to_sympy_and_print(latex_code)


st.markdown("#### Euler's Formula:")

latex_code = r"""
e^{i\theta} = \cos\theta + i\sin\theta"""
latex_to_sympy_and_print(latex_code)


st.markdown("#### Binomial Coefficient:")

latex_code = r"""
\binom{n}{k} = \frac{n!}{k!(n-k)!}
"""
latex_to_sympy_and_print(latex_code)


st.markdown("#### Square root:")

latex_code = r"""
\sqrt{x^2+1}
"""
latex_to_sympy_and_print(latex_code)


st.markdown("#### Mass-energy equivalence:")

latex_code = r"""
E=mc^2
"""
latex_to_sympy_and_print(latex_code)


st.markdown("#### Subscripts and Superscripts:")

st.write(
    r"Subscripts in math mode are written as $a_b$ and superscripts are written as $a^b$. These can be combined and nested to write expressions such as"
)
latex_code = r"""
T^{i_1 i_2 \dots i_p}_{j_1 j_2 \dots j_q} = T(x^{i_1},\dots,x^{i_p},e_{j_1},\dots,e_{j_q})
"""
latex_to_sympy_and_print(latex_code)


st.markdown("#### Integrals and Fractions:")

st.write(
    r"We write integrals using $\int$ and fractions using $\frac{a}{b}$. Limits are placed on integrals using superscripts and subscripts:"
)
latex_code = r"""
\int_0^1 \frac{dx}{e^x} =  \frac{e-1}{e}
"""
latex_to_sympy_and_print(latex_code)


st.markdown("#### Limits:")

st.write(
    r"The command \limits changes the way the limits are displayed in the integral, if not present the limits would be next to the integral symbol instead of being on top and bottom:"
)
latex_code = r"""
\int\limits_0^1 x^2 + y^2 dx 
"""
latex_to_sympy_and_print(latex_code)


latex_code = """
\int_0^1 x^2 + y^2 dx
"""
latex_to_sympy_and_print(latex_code)

st.write("The symbols _ and ^ can also be combined in the same expression")
latex_code = """
a_1^2 + a_2^2 = a_3^2
"""
latex_to_sympy_and_print(latex_code)


st.markdown("#### Lower case Greek letters:")

latex_code = r"""
\alpha \beta \gamma \rho \sigma \delta \epsilon \omega
"""
latex_to_sympy_and_print(latex_code)


st.markdown("#### Upper case Greek letters:")

latex_code = """
\Alpha \Beta \Gamma \Rho \Sigma \Delta \Epsilon \Omega
"""
latex_to_sympy_and_print(latex_code)
st.write("https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols")


st.markdown("#### Mathematical Operators:")

st.write(r"Prefixed with a backslash:")
latex_code = r"""
\sin(\beta), \cos(\alpha), \log(x) \int \oint \sum \prod \pi
"""
latex_to_sympy_and_print(latex_code)


st.markdown("#### Bracket and Parentheses Sizing:")

st.write(
    r"The size of brackets and parentheses can be manually set, or they can be resized dynamically"
)
latex_code = r"""
F = G \left( \frac{m_1 m_2}{r^2} \right)
"""
latex_to_sympy_and_print(latex_code)

st.markdown("#### Limits:")

latex_code = r"""
\lim_{h \to 0 } \frac{f(x+h)-f(x)}{h}
"""
latex_to_sympy_and_print(latex_code)


st.markdown("#### References")

st.write(
    "Learn LaTeX in 30 Minutes - https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes"
)
st.write(
    "Mathematical Expressions - https://www.overleaf.com/learn/latex/Mathematical_expressions"
)
st.write(
    "Brackets and Parentheses - https://www.overleaf.com/learn/latex/Brackets_and_Parentheses"
)
st.write(
    "Subscripts and Superscripts - https://www.overleaf.com/learn/latex/Subscripts_and_superscripts"
)
st.write(
    "Fractions and Binomials - https://www.overleaf.com/learn/latex/Fractions_and_Binomials"
)
st.write("Operators - https://www.overleaf.com/learn/latex/Operators")
st.write(
    "LaTeX Symbols - https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols"
)
st.write(
    " - https://gb.mirrors.cicku.me/ctan/info/symbols/comprehensive/symbols-a4.pdf"
)
