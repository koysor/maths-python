import streamlit as st

st.set_page_config(page_title="LaTeX Examples", page_icon="📐", layout="wide")
st.header("LaTeX Examples")

st.write(
    "LaTeX is a markup language used for typesetting and often used for presenting "
    "mathematical and scientific documents. For reference purposes this page contains "
    "examples of mathematical notation expressed in LaTeX code."
)
st.write(
    "The LaTeX code is displayed in a code block, and the rendered LaTeX output is displayed below it."
)


def latex_print(latex_code):
    st.code(latex_code, language="latex")
    st.latex(latex_code)


tab_syntax, tab_famous = st.tabs(["Syntax Reference", "Famous Equations"])

# =============================================================================
# Tab 1: Syntax Reference
# =============================================================================
with tab_syntax:

    # ── 1. Subscripts, Superscripts and Greek Letters ────────────────────
    st.markdown("#### Subscripts, Superscripts and Greek Letters")

    st.write(
        r"Subscripts in math mode are written as $a_b$ and superscripts are written as $a^b$. "
        r"These can be combined and nested to write expressions such as"
    )
    latex_code = r"""
T^{i_1 i_2 \dots i_p}_{j_1 j_2 \dots j_q} = T(x^{i_1},\dots,x^{i_p},e_{j_1},\dots,e_{j_q})
"""
    latex_print(latex_code)

    st.write(r"The symbols _ and ^ can also be combined in the same expression:")
    latex_code = r"""
a_1^2 + a_2^2 = a_3^2
"""
    latex_print(latex_code)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### Lowercase Greek Letters")
        latex_code = r"""
\alpha \beta \gamma \delta \epsilon \zeta \eta \theta \lambda \mu \rho \sigma \omega
"""
        latex_print(latex_code)
    with col2:
        st.markdown("##### Uppercase Greek Letters")
        latex_code = r"""
\Gamma \Delta \Theta \Lambda \Sigma \Phi \Psi \Omega
"""
        latex_print(latex_code)

    st.divider()

    # ── 2. Fractions and Square Roots ────────────────────────────────────
    st.markdown("#### Fractions and Square Roots")

    st.write(
        r"We write fractions using $\frac{a}{b}$. "
        r"Use `\tfrac` for text-size (smaller) fractions and `\dfrac` for display-size (larger) fractions."
    )
    latex_code = r"""
\frac{e-1}{e} \qquad \text{Text-size: } (x + \tfrac{b}{2})^{2} \qquad \text{Display-size: } h = -\dfrac{b}{2a}
"""
    latex_print(latex_code)

    st.write(r"Square roots use `\sqrt{...}`, and nth roots use `\sqrt[n]{...}`:")
    latex_code = r"""
\sqrt{x^2+1} \qquad \sqrt[3]{8} = 2 \qquad \sqrt[n]{x}
"""
    latex_print(latex_code)

    st.divider()

    # ── 3. Integrals and Summations ──────────────────────────────────────
    st.markdown("#### Integrals and Summations")

    st.write(
        r"We write integrals using $\int$ and place limits using superscripts and subscripts:"
    )
    latex_code = r"""
\int_0^1 \frac{dx}{e^x} = \frac{e-1}{e}
"""
    latex_print(latex_code)

    st.write(
        r"The command `\limits` changes the way the limits are displayed. "
        r"With `\limits` they appear on top and bottom; without, they appear beside the symbol:"
    )
    latex_code = r"""
\int\limits_0^1 x^2 + y^2 \, dx \qquad \text{vs.} \qquad \int_0^1 x^2 + y^2 \, dx
"""
    latex_print(latex_code)

    st.write(r"Evaluation brackets for definite integrals:")
    latex_code = r"""
\int_2^5 (6x + 1) \, dx = [3x^2 + x]_2^5
"""
    latex_print(latex_code)

    st.write(r"Double summation:")
    latex_code = r"""
\sigma_p^2 = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j \sigma_{ij}
"""
    latex_print(latex_code)

    st.write(r"Product with limits:")
    latex_code = r"""
\prod_{i=1}^{n} x_i = x_1 \cdot x_2 \cdots x_n
"""
    latex_print(latex_code)

    st.divider()

    # ── 4. Limits and Derivatives ────────────────────────────────────────
    st.markdown("#### Limits and Derivatives")

    st.write(r"Limit of a function using `\lim`:")
    latex_code = r"""
\lim_{h \to 0 } \frac{f(x+h)-f(x)}{h}
"""
    latex_print(latex_code)

    st.write(r"Leibniz operator applied to an expression:")
    latex_code = r"""
\frac{d}{dx} (x^n) = n \cdot x^{n-1}
"""
    latex_print(latex_code)

    st.write(r"Prime notation and nth derivative:")
    latex_code = r"""
f'(x), \quad f''(x), \quad f^{(n)}(a)
"""
    latex_print(latex_code)

    st.write(r"Partial derivatives using `\partial`:")
    latex_code = r"""
\frac{\partial f}{\partial x} \qquad \frac{\partial^2 f}{\partial x^2} \qquad \frac{\partial^2 f}{\partial x \, \partial y}
"""
    latex_print(latex_code)

    st.divider()

    # ── 5. Operators and Functions ────────────────────────────────────────
    st.markdown("#### Operators and Functions")

    st.write(r"Common operators are prefixed with a backslash:")
    latex_code = r"""
\sin(\beta), \cos(\alpha), \log(x) \int \oint \sum \prod \pi
"""
    latex_print(latex_code)

    st.markdown("##### Exponential (`\\exp`):")
    latex_code = r"""
f(x) = \frac{1}{x \sigma \sqrt{2\pi}} \exp\left(-\frac{(\ln x - \mu)^2}{2\sigma^2}\right)
"""
    latex_print(latex_code)

    st.markdown("##### Natural Logarithm (`\\ln`):")
    latex_code = r"""
\frac{d}{dx}\, \ln(x) = \frac{1}{x}
"""
    latex_print(latex_code)

    st.markdown("##### Logarithm with Base (`\\log_a`):")
    latex_code = r"""
\log_a{b} = x \iff a^x = b
"""
    latex_print(latex_code)

    st.markdown("##### Determinant (`\\det`):")
    latex_code = r"""
\det(A - \lambda I) = 0
"""
    latex_print(latex_code)

    st.markdown("##### Maximum (`\\max`):")
    latex_code = r"""
\text{Payoff} = \max(S_T - K, 0)
"""
    latex_print(latex_code)

    st.divider()

    # ── 6. Brackets and Parentheses ──────────────────────────────────────
    st.markdown("#### Brackets and Parentheses")

    st.write(
        r"Use `\left` and `\right` for auto-sizing brackets that grow to fit their contents:"
    )
    latex_code = r"""
F = G \left( \frac{m_1 m_2}{r^2} \right)
"""
    latex_print(latex_code)

    st.write(r"Use `\left[` and `\right]` for auto-sizing square brackets:")
    latex_code = r"""
S_T = S_0 \exp\left[\left(r - \frac{\sigma^2}{2}\right)T + \sigma W_T\right]
"""
    latex_print(latex_code)

    st.write(r"For manual sizing, use `\big`, `\Big`, `\bigg`, `\Bigg`:")
    latex_code = r"""
\big( \Big( \bigg( \Bigg( \qquad \big] \Big] \bigg] \Bigg] \qquad \big\{ \Big\{ \bigg\{ \Bigg\{
"""
    latex_print(latex_code)

    st.divider()

    # ── 7. Multi-line Equations and Matrices ─────────────────────────────
    st.markdown("#### Multi-line Equations and Matrices")

    st.markdown("##### Aligned Equations (`align*`):")
    st.write(
        r"The `align*` environment aligns multi-line equations on the `&` symbol. The `*` suppresses equation numbering."
    )
    latex_code = r"""
\begin{align*}
    \frac{dy}{dx} &= \frac{dy}{du} \cdot \frac{du}{dx} \\
    \\
    &= f'(g(x)) \cdot g'(x)
\end{align*}
"""
    latex_print(latex_code)

    st.markdown("##### Piecewise Functions (`cases`):")
    st.write(r"The `cases` environment is used for piecewise-defined functions:")
    latex_code = r"""
f(x) = \begin{cases}
    1 & \text{if } x > 0 \\
    0 & \text{if } x = 0 \\
   -1 & \text{if } x < 0
\end{cases}
"""
    latex_print(latex_code)

    st.markdown("##### Numbered Equation (`equation`):")
    latex_code = r"""
\begin{equation}
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
\end{equation}
"""
    latex_print(latex_code)

    st.markdown("##### Matrix (`bmatrix`):")
    st.write(
        r"Use `bmatrix` for square-bracketed matrices. Columns are separated by `&` and rows by `\\`."
    )
    latex_code = r"""
I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
"""
    latex_print(latex_code)

    st.write(r"Matrices with ellipses for large dimensions:")
    latex_code = r"""
\boldsymbol{\Sigma} = \begin{bmatrix}
\sigma_1^2 & \sigma_{12} & \cdots & \sigma_{1n} \\
\sigma_{21} & \sigma_2^2 & \cdots & \sigma_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{n1} & \sigma_{n2} & \cdots & \sigma_n^2
\end{bmatrix}
"""
    latex_print(latex_code)

    st.divider()

    # ── 8. Font Styles ───────────────────────────────────────────────────
    st.markdown("#### Font Styles")

    st.markdown("##### Blackboard Bold (`\\mathbb`):")
    st.write(
        r"Used for number sets ($\mathbb{R}$, $\mathbb{Z}$) and the expectation operator ($\mathbb{E}$)."
    )
    latex_code = r"""
\mathbb{E}[X] = \int_{-\infty}^{\infty} x f(x) \, dx
"""
    latex_print(latex_code)

    st.markdown("##### Calligraphic (`\\mathcal`):")
    st.write(r"Commonly used for the normal distribution notation.")
    latex_code = r"""
X \sim \mathcal{N}(\mu, \sigma^2)
"""
    latex_print(latex_code)

    st.markdown("##### Bold Math (`\\mathbf`) and Bold Symbol (`\\boldsymbol`):")
    st.write(
        r"Use `\mathbf` for bold Latin letters (vectors/matrices) and `\boldsymbol` for bold Greek letters."
    )
    latex_code = r"""
\sigma_p^2 = \mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}
"""
    latex_print(latex_code)

    st.markdown("##### Text in Math Mode (`\\text`):")
    st.write(r"Use `\text{...}` for upright text inside mathematical expressions.")
    latex_code = r"""
P(\text{exactly } k \text{ defaults}) = \binom{n}{k} p^k (1-p)^{n-k}
"""
    latex_print(latex_code)

    st.divider()

    # ── 9. Symbols and Notation ──────────────────────────────────────────
    st.markdown("#### Symbols and Notation")

    st.markdown("##### Accents: `\\vec`, `\\hat`, `\\bar`")
    st.write(
        r"Use `\vec` for vector arrows, `\hat` for estimators, and `\bar` for sample means:"
    )
    latex_code = r"""
\vec{v} = \begin{bmatrix} x \\ y \\ z \end{bmatrix} \qquad \hat{\beta} = (X^\top X)^{-1} X^\top y \qquad \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
"""
    latex_print(latex_code)

    st.markdown("##### Transpose (`\\top`):")
    latex_code = r"""
\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}
"""
    latex_print(latex_code)

    st.markdown("##### Distributed As (`\\sim`):")
    latex_code = r"""
X \sim \text{Binomial}(n, p)
"""
    latex_print(latex_code)

    st.markdown("##### Infinity (`\\infty`):")
    latex_code = r"""
\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
"""
    latex_print(latex_code)

    st.markdown("##### Cancellation (`\\cancel`):")
    st.write(
        r"Note: `\cancel` requires the `cancel` package in standard LaTeX (`\usepackage{cancel}`). "
        r"KaTeX (used by Streamlit) supports it natively."
    )
    latex_code = r"""
\frac{\cancel{e^{3x}}}{(e^{3x} +1)^2} \left(\frac{1}{3\cancel{e^{3x}}}\right)
"""
    latex_print(latex_code)

    st.markdown("##### Arrows:")
    latex_code = r"""
f(x) = 79 \rightarrow f'(x) = 0 \qquad \log_a{b} = x \iff a^x = b
"""
    latex_print(latex_code)

    st.markdown("##### Underbrace and Overbrace:")
    st.write(r"Use `\underbrace` and `\overbrace` to annotate parts of an expression:")
    latex_code = r"""
\underbrace{n \cdot (n-1) \cdot (n-2) \cdots 1}_{n!} \qquad \overbrace{1 + 2 + \cdots + n}^{\frac{n(n+1)}{2}}
"""
    latex_print(latex_code)

    st.markdown("##### Set Notation:")
    latex_code = r"""
x \in A \qquad A \subset B \qquad A \cup B \qquad A \cap B \qquad \emptyset
"""
    latex_print(latex_code)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### Comparison and Relation Symbols")
        latex_code = r"""
a \leq b \qquad a \geq b \qquad a \neq b \qquad a \approx b
"""
        latex_print(latex_code)
    with col2:
        st.markdown("##### Arithmetic Symbols")
        latex_code = r"""
a \cdot b \qquad a \times b \qquad a \div b
"""
        latex_print(latex_code)

    st.divider()

    # ── 10. Spacing and Ellipses ─────────────────────────────────────────
    st.markdown("#### Spacing and Ellipses")

    st.write(
        r"LaTeX provides several spacing commands for fine control inside math mode:"
    )
    latex_code = r"""
|\,| \quad \text{thin } \texttt{\textbackslash,} \qquad |\;| \quad \text{medium } \texttt{\textbackslash;} \qquad |\quad| \quad \texttt{\textbackslash quad} \qquad |\qquad| \quad \texttt{\textbackslash qquad}
"""
    latex_print(latex_code)

    st.write(r"Spacing in context:")
    latex_code = r"""
\int f(x) \, dx \qquad e^{\ln x} = x \quad (x > 0) \qquad \ln(e^x) = x \quad (\text{all } x)
"""
    latex_print(latex_code)

    st.write(
        r"Use `\cdots` (centred), `\ldots` (baseline), `\vdots` (vertical), and `\ddots` (diagonal)."
    )
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### Horizontal Ellipses")
        latex_code = r"""
a_1 + a_2 + \cdots + a_n \qquad a_1, a_2, \ldots, a_n
"""
        latex_print(latex_code)
    with col2:
        st.markdown("##### Vertical and Diagonal Ellipses")
        latex_code = r"""
\begin{bmatrix} 1 \\ \vdots \\ n \end{bmatrix} \qquad \begin{bmatrix} 1 & & \\ & \ddots & \\ & & n \end{bmatrix}
"""
        latex_print(latex_code)


# =============================================================================
# Tab 2: Famous Equations
# =============================================================================
with tab_famous:

    with st.expander("Black-Scholes Equation — option pricing PDE", expanded=True):
        latex_code = r"""
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - rV = 0
"""
        latex_print(latex_code)

    with st.expander("Itô's Lemma — stochastic chain rule"):
        latex_code = r"""
dX_t = \mu(X_t, t) dt + \sigma(X_t, t) dW_t \\[1em]
df = \left( \frac{\partial f}{\partial t} + \mu \frac{\partial f}{\partial x} + \frac{1}{2} \sigma^2 \frac{\partial^2 f}{\partial x^2} \right) dt + \sigma \frac{\partial f}{\partial x} dW_t.
"""
        latex_print(latex_code)

    with st.expander("Euler's Formula — complex exponential"):
        latex_code = r"""
e^{i\theta} = \cos\theta + i\sin\theta
"""
        latex_print(latex_code)

    with st.expander("Binomial Coefficient — combinatorics"):
        latex_code = r"""
\binom{n}{k} = \frac{n!}{k!(n-k)!}
"""
        latex_print(latex_code)

    with st.expander("Mass-Energy Equivalence — special relativity"):
        latex_code = r"""
E=mc^2
"""
        latex_print(latex_code)

    with st.expander("Newton's Law of Gravitation — gravitational force"):
        latex_code = r"""
F = G \left( \frac{m_1 m_2}{r^2} \right)
"""
        latex_print(latex_code)


# =============================================================================
# References (outside tabs)
# =============================================================================
st.divider()
st.markdown("#### References")

st.markdown("""
- [Learn LaTeX in 30 Minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)
- [Mathematical Expressions](https://www.overleaf.com/learn/latex/Mathematical_expressions)
- [Brackets and Parentheses](https://www.overleaf.com/learn/latex/Brackets_and_Parentheses)
- [Subscripts and Superscripts](https://www.overleaf.com/learn/latex/Subscripts_and_superscripts)
- [Fractions and Binomials](https://www.overleaf.com/learn/latex/Fractions_and_Binomials)
- [Operators](https://www.overleaf.com/learn/latex/Operators)
- [Greek Letters and Math Symbols](https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols)
- [Comprehensive LaTeX Symbol List (PDF)](https://gb.mirrors.cicku.me/ctan/info/symbols/comprehensive/symbols-a4.pdf)
""")
