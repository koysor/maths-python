import streamlit as st


st.set_page_config(layout="wide")
st.markdown("### Integration")


col1, col2 = st.columns([4, 3])

with col1:
    summary_integration = """
    Integration is the opposite of differentiation.
    \nFor a given function f(x), integration is used to find the area under the curve of the function between two points on the x-axis.
    """
    st.info(summary_integration)

with col2:
    st.video(
        "https://www.youtube.com/watch?v=ni1DFNQnFJw&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=101"
    )


st.markdown("#### Indefinite Integration")

st.write(
    """Indefinite integration, the opposite of differentiation, 
is used to determine the **original function** which was differentiated in order to obtain the current function."""
)

st.write("Rule to integrate terms which are written in the form of $$ax^n$$:")

latex_code = r"""
\int ax^n \,dx = \frac{a}{n+1}x^{n+1} + C
"""
st.latex(latex_code)
st.write("$$\int$$ is the symbol for integration.")
st.write("We increase the power of x by 1 and then divide by the new power.")
st.write(
    "Add C which is the constant of integration.  When we differentiate, any constant terms will disapper.  Therefore many functions have the same derivative."
)
st.write(
    "When we integrate, we need to add a constant term to the function to account for this."
)

st.write("Working example of indefinite integration:")

latex_code = r"""
\int 6x + 1 \,dx \\
"""
st.latex(latex_code)

st.write("We can split the integral into two parts:")
st.latex(
    r"""
\int 6x \,dx = \frac{6}{1+1}x^{1+1} \\
= 3x^2       
"""
)

st.latex(
    r"""
\int 1 \,dx = x \\
"""
)

latex_code = r"""
\frac{6}{1+1}x^{1+1} + 1 + C \\
= 3x^2 + x + C  
"""
st.latex(latex_code)


st.markdown("#### Definite Integration")

st.write(
    """Definite integration is used to obtain a **numerical answer** for the area under the curve of a function between two points on the x-axis."""
)

col1, col2 = st.columns([4, 3])

with col1:
    st.write("Example of a definite integral: Integrate (6x + 1) from 2 to 5.")
    latex_code = """
    \int_{2}^{5} (6x + 1) \,dx
    """
    st.latex(latex_code)

    st.write(
        "Integrate to obtain the integral.  The limits are displayed next to the square brackets."
    )

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
    st.video(
        "https://www.youtube.com/watch?v=Sp_KWTdBRsE&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=101&pp=iAQB"
    )


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

col1, col2 = st.columns([4, 3])

with col1:
    st.write(
        "This version of the **Chain Rule** can be used to find the gradient of a curve which is defined by **parametric equations**."
    )

    latex_code = r"""
    \frac{dy}{dx} = \frac{dy}{dt} \div \frac{dx}{dt}
    """
    st.latex(latex_code)

with col2:
    st.video(
        "https://www.youtube.com/watch?v=p6YBlqon8TE&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=102&pp=iAQB"
    )


st.markdown("#### Integration with Exponentials and Logarithms")

col1, col2 = st.columns([4, 3])

with col1:
    pass

with col2:
    st.video(
        "https://www.youtube.com/watch?v=i3uX8VTZz6s&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=104&pp=iAQB"
    )


st.markdown("#### Integrating Trigonometric Functions")

col1, col2 = st.columns([4, 3])

with col1:
    pass

with col2:
    st.video(
        "https://www.youtube.com/watch?v=XKXWTaL8JUY&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=105&pp=iAQB"
    )


st.markdown("#### Reverse Chain Rule")

col1, col2 = st.columns([4, 3])

with col1:
    pass

with col2:
    st.video(
        "https://www.youtube.com/watch?v=q8o5zVQiajM&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=107&pp=iAQB"
    )


st.markdown("#### Integration by Substitution")

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

st.info(r"1. Find $$\frac{du}{dx}$$ and write an expression for $$dx$$ in the form $$f(x) ~ du$$.")
st.write(r"$$u = e^{3x}$$")
st.write("Therefore:")
st.write(r"$$\frac{du}{dx} = 3e^{3x}$$")
st.write(r"$$dx$$ is equivalent to $$(\frac{1}{3e^{3x}}) ~ du$$.  Note that $$dx$$ is treated symbolically to be rearranged for substitution.")
st.write(r"$$(\frac{1}{3e^{3x}}) ~ du$$ is now ex expression in the form of $$f(x) ~ du$$.")

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


st.markdown("#### Integration by Parts")

col1, col2 = st.columns([4, 3])

with col1:

    st.write("Integrations by partys is used to integrate the product of two functions.")
    
    latex_code = r"""
    \int u \frac{dv}{dx} \, dx = uv - \int v \frac{du}{dx} \, dx
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)
    st.write(
        "Where $$u$$ and $$v$$ are functions of $$x$$.  The function $$u$$ is chosen to be the function which is easier to differentiate."
    )
    st.write(r"$$u \frac{dv}{dx}$$ is the function which is being integrated.")
    st.write(r"We must determine which part of the function is $$u$$ and which part is $$\frac{dv}{dx}$$.")

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


st.markdown("#### Numerical Integration")

col1, col2 = st.columns([4, 3])

with col1:
    st.write(
        "Numerical integration is used to calculate an approximate value of an integral of a function by using making discreate."
    )

with col2:
    st.video(
        "https://www.youtube.com/watch?v=ba6j_9f_5e4&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=118"
    )
