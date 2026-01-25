import streamlit as st


st.set_page_config(layout="wide")
st.markdown("### Calculus Rules")


table_md = """
| **Rule Name**         | **Differentiation**                                 | **Integration**                                              | **Relation**                       |
|-----------------------|-----------------------------------------------------|--------------------------------------------------------------|------------------------------------|
| Power Rule            | $\\frac{d}{dx}[x^n] = nx^{n-1}$                      | $\\int x^n\\,dx = \\frac{x^{n+1}}{n+1} + C,\\ n \\ne -1$     | Inverse of power rule              |
| Constant Rule         | $\\frac{d}{dx}[c] = 0$                               | $\\int 0\\,dx = C$                                            | Deriv. of constant is 0            |
| Constant Multiple     | $\\frac{d}{dx}[c f(x)] = c f'(x)$                   | $\\int c f(x)\\,dx = c \\int f(x)\\,dx$                      | Linear in constant                 |
| Sum Rule              | $\\frac{d}{dx}[f + g] = f' + g'$                     | $\\int(f + g)\\,dx = \\int f\\,dx + \\int g\\,dx$            | Addition rule is linear            |
| Difference Rule       | $\\frac{d}{dx}[f - g] = f' - g'$                     | $\\int(f - g)\\,dx = \\int f\\,dx - \\int g\\,dx$            | Subtraction rule is linear         |
| Product Rule          | $\\frac{d}{dx}[fg] = f'g + fg'$                      | $\\int u\\,dv = uv - \\int v\\,du$                           | Integration by parts               |
| Quotient Rule         | $\\frac{d}{dx}\\left[\\frac{f}{g}\\right] = \\frac{f'g - fg'}{g^2}$ | No simple rule                                | No clean inverse                  |
| Chain Rule            | $\\frac{d}{dx}[f(g(x))] = f'(g(x)) \\cdot g'(x)$    | Use $u$-substitution                                          | Reverse of chain rule              |
| Exponential Rule      | $\\frac{d}{dx}[e^x] = e^x$                           | $\\int e^x\\,dx = e^x + C$                                   | Perfect inverse                    |
| Logarithmic Rule      | $\\frac{d}{dx}[\\ln x] = \\frac{1}{x}$              | $\\int \\frac{1}{x}\\,dx = \\ln\\vert x\\vert + C$ | Inverse with absolute value        |
| Trig Rule (sin)       | $\\frac{d}{dx}[\\sin x] = \\cos x$                  | $\\int \\cos x\\,dx = \\sin x + C$                           | Direct inverse                     |
| Trig Rule (cos)       | $\\frac{d}{dx}[\\cos x] = -\\sin x$                 | $\\int \\sin x\\,dx = -\\cos x + C$                          | Direct inverse                     |
| Trig Rule (tan)       | $\\frac{d}{dx}[\\tan x] = \\sec^2 x$                | $\\int \\sec^2 x\\,dx = \\tan x + C$                         | Direct inverse                     |
"""

# Render the table with math
st.markdown(table_md)

st.markdown(
    """
These rules are fundamental in calculus for finding derivatives and integrals of functions. The differentiation rules help in finding the rate of change, while the integration rules assist in finding the area under curves or the accumulation of quantities.
"""
)
