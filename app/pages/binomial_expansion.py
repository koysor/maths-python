import streamlit as st


st.set_page_config(layout="wide")
st.markdown("### Binomial Expansion")
st.write(
    "The Binomial Expansion allows us to expand expressions such as $$(a + b)^n$$ without multiplying them out."
)

st.write("The Binomial Expansion is given by the formula:")
latex_code = r"""
(a + b)^n = a^n + \binom{n}{1} a^{n-1} b + \binom{n}{2} a^{n-2} b^2 + \ldots + \binom{n}{k} a^{n-k} b^k + \ldots + b^n
= \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k
"""
st.code(latex_code, language="latex")
st.latex(latex_code)

st.write("Where:")
st.write("- \(a\) and \(b\) are the terms being expanded.")
st.write("- \(n\) is a non-negative integer.")
latex_code = r"""
\binom{n}{k}
"""

st.write("And:")
st.code(latex_code, language="latex")
st.latex(latex_code)
st.write(
    "- Is the binomial coefficient, which represents the number of ways to choose \(k\) elements from a set of \(n\) elements."
)


st.markdown(r"#### $$\binom{n}{k}$$ in Python:")

n = st.number_input("Enter the value of n:", min_value=1, value=5)
k = st.number_input("Enter the value of k:", min_value=1, value=2)

st.write(
    f"The math.comb function tells us how many ways we can choose {k} objects from a set of {n} objects."
)

code_snippet = f"""
import streamlit as st
import math

answer = math.comb({n}, {k})
st.write(f"The number of ways to choose {k} objects from a set of {n} objects is:")
st.write(answer)
"""
st.code(code_snippet, language="python")
exec(code_snippet)
st.write(
    r"In this example, we use the `math` library to compute the binomial coefficient $$\binom{5}{2}$$."
)
st.write(
    "The output will show the value of the binomial coefficient, which is 10 in this case."
)


st.markdown("#### Symbolically with SymPy in Python:")

code_snippet = f"""
import streamlit as st
import sympy as sp

# Define symbols
a, b = sp.symbols('a b')

# Expand (a + b)^{n}
expansion = sp.expand((a + b)**{n})

st.write(expansion)
"""

st.code(code_snippet, language="python")
exec(code_snippet)
st.write(
    f"In this example, we use the SymPy library to compute the Binomial Expansion of the expression $$(a + b)^{n}$$."
)
st.write("The output will show the expanded form of the expression.")
