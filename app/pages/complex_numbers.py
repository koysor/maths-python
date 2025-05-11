import streamlit as st

st.set_page_config(layout="wide")
st.markdown("### Complex Numbers")

st.write(
    "A **Complex Number** is a number that has two parts.  A real part and an imaginary part."
)

col1, col2 = st.columns(2)

with col1:

    code_snippet = """
import streamlit as st

# Example of a complex number - automically coverted to complex type by Python
a = 3 + 4j

st.write('The complex number is represented as: ', a)
st.write('The real part is: ', a.real)
st.write('The imaginary part is: ', a.imag)
st.write('The absolute value is: ', abs(a))
    """
    st.code(code_snippet, language="python")
    exec(code_snippet)

with col2:

    code_snippet = """
import matplotlib.pyplot as plt
import streamlit as st

# Complex number
z = 3 + 4j

# Plot
plt.figure(figsize=(6, 6))
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)
plt.plot(z.real, z.imag, 'bo')  # blue dot
plt.text(z.real + 0.2, z.imag, f'{z}', fontsize=12)

# Axis labels
plt.xlabel('Real')
plt.ylabel('Imaginary')

# Grid and limits
plt.grid(True)
plt.xlim(-1, 6)
plt.ylim(-1, 6)
plt.title('Complex Number on the Complex Plane')
plt.gca().set_aspect('equal')

st.pyplot(plt.gcf())
"""
    st.code(code_snippet, language="python")
    exec(code_snippet)

st.markdown("### Absolute Value of Complex Numbers")

st.write(
    "N.B. The **absolute value** of a complex number is the distance from the origin in the complex plane."
)
st.write(
    "The **real part** is the x-coordinate and the **imaginary part** is the y-coordinate."
)
st.write(
    "For example, the complex number $$3 + 4j$$ is represented as the point (3, 4) in the complex plane."
)
st.write("The **absolute value** of a complex number is calculated using the formula:")

latex_code = r"""
|a + bj| = \sqrt{a^2 + b^2}
"""
st.code(latex_code, language="latex")
st.latex(latex_code)

st.write(
    "In the example above, the absolute value of $$3 + 4j$$ is calculated as follows:"
)
latex_code = r"""
|3 + 4j| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
"""
st.code(latex_code, language="latex")
st.latex(latex_code)


st.write("The absolute value of a complex number is always a **real number**.")


st.markdown("### Usage of Complex Numbers")

st.write(
    "Complex numbers are useful as they allow us to solve problems that can't be handled with just real numbers."
)
st.write(
    "For example, equations like $$x^2 + 1 = 0$$ have **no real solutions**, but they do have **complex solutions**, $$x = i$$ and $$x = -i$$."
)

st.write(
    "A **real solution** is solution to an equation that is a **real number** in that is lies somewhere on the **real number line**."
)
st.write(
    "And it does not include any **imaginary numbers**, e.g. $$i$$ where $$i = \sqrt(-1)$$ ."
)
