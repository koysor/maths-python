import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Completing the Square", page_icon="📐", layout="wide")
st.header("Completing the Square")

st.write("""Completing the square is a method for rewriting a quadratic expression
$$ax^{2} + bx + c$$ in a form that reveals it as (almost) a perfect square,
typically $$a(x - h)^{2} + k$$. This makes it easier to solve quadratic equations
and to read properties like the vertex of a parabola.""")

st.info(
    """**Parabola** — A parabola is the U-shaped curve produced by graphing a quadratic
function. It is symmetrical about a vertical line called the *axis of symmetry*.

**Vertex of a Parabola** — The vertex is the single point where the parabola
changes direction — its minimum point when the parabola opens upwards ($a > 0$)
or its maximum point when it opens downwards ($a < 0$). In vertex form
$a(x - h)^{2} + k$, the vertex is simply the point $(h,\\, k)$."""
)


# ── Core Idea ───────────────────────────────────────────────────────────────────

st.markdown("#### Core Idea")

st.write(r"""The first two terms of a quadratic, $x^{2} + bx$, can be turned into
the start of a perfect square $(x + \tfrac{b}{2})^{2}$ by adding
$(\tfrac{b}{2})^{2}$.  We then subtract that same amount to keep the
expression equal.""")

latex_code = (
    r"x^{2} + bx = \left(x + \frac{b}{2}\right)^{2} - \left(\frac{b}{2}\right)^{2}"
)
st.code(latex_code, language="latex")
st.latex(latex_code)

st.write(r"""This identity has a neat geometric interpretation.  The expression
$x^{2} + bx$ represents the area of a **rectangle** with width $x$ and height
$x + b$.  By rearranging that same area we can form a **square** of side
$x + \tfrac{b}{2}$, but to keep the areas equal we must subtract the small
corner square of side $\tfrac{b}{2}$.""")

# ── Geometric diagram ──────────────────────────────────────────────────────────

x_len = 3.0
b_len = 2.0
half_b = b_len / 2

fig_geo, (ax_rect, ax_sq) = plt.subplots(1, 2, figsize=(10, 4.5))

# ── Left: rectangle  x(x + b) = x² + bx ─────────────────────────────────────

# x² portion (bottom)
ax_rect.add_patch(
    plt.Rectangle(
        (0, 0),
        x_len,
        x_len,
        facecolor="#4A90D9",
        edgecolor="black",
        linewidth=1.5,
        alpha=0.7,
    )
)
ax_rect.text(
    x_len / 2,
    x_len / 2,
    "$x^2$",
    ha="center",
    va="center",
    fontsize=14,
    fontweight="bold",
)

# bx portion (top)
ax_rect.add_patch(
    plt.Rectangle(
        (0, x_len),
        x_len,
        b_len,
        facecolor="#F5A623",
        edgecolor="black",
        linewidth=1.5,
        alpha=0.7,
    )
)
ax_rect.text(
    x_len / 2,
    x_len + b_len / 2,
    "$bx$",
    ha="center",
    va="center",
    fontsize=14,
    fontweight="bold",
)

# Width label (bottom)
ax_rect.annotate(
    "",
    xy=(x_len, -0.4),
    xytext=(0, -0.4),
    arrowprops=dict(arrowstyle="<->", color="black", lw=1.5),
)
ax_rect.text(x_len / 2, -0.7, "$x$", ha="center", va="center", fontsize=13)

# Height label – x portion (right)
ax_rect.annotate(
    "",
    xy=(x_len + 0.4, x_len),
    xytext=(x_len + 0.4, 0),
    arrowprops=dict(arrowstyle="<->", color="#4A90D9", lw=1.5),
)
ax_rect.text(
    x_len + 0.7,
    x_len / 2,
    "$x$",
    ha="center",
    va="center",
    fontsize=13,
    color="#4A90D9",
)

# Height label – b portion (right)
ax_rect.annotate(
    "",
    xy=(x_len + 0.4, x_len + b_len),
    xytext=(x_len + 0.4, x_len),
    arrowprops=dict(arrowstyle="<->", color="#D4760A", lw=1.5),
)
ax_rect.text(
    x_len + 0.7,
    x_len + b_len / 2,
    "$b$",
    ha="center",
    va="center",
    fontsize=13,
    color="#D4760A",
)

ax_rect.set_xlim(-1, x_len + 1.5)
ax_rect.set_ylim(-1.2, x_len + b_len + 0.5)
ax_rect.set_aspect("equal")
ax_rect.axis("off")
ax_rect.set_title("$x^2 + bx$\n(rectangle)", fontsize=13, pad=10)

# ── Right: (x + b/2)² − (b/2)²  (square minus corner) ──────────────────────

side = x_len + half_b

# Bottom-left block: x × x
ax_sq.add_patch(
    plt.Rectangle(
        (0, 0),
        x_len,
        x_len,
        facecolor="#4A90D9",
        edgecolor="black",
        linewidth=1.5,
        alpha=0.7,
    )
)
ax_sq.text(
    x_len / 2,
    x_len / 2,
    "$x^2$",
    ha="center",
    va="center",
    fontsize=14,
    fontweight="bold",
)

# Bottom-right strip: (b/2) × x
ax_sq.add_patch(
    plt.Rectangle(
        (x_len, 0),
        half_b,
        x_len,
        facecolor="#F5A623",
        edgecolor="black",
        linewidth=1.5,
        alpha=0.7,
    )
)
ax_sq.text(
    x_len + half_b / 2,
    x_len / 2,
    r"$\frac{b}{2}\!x$",
    ha="center",
    va="center",
    fontsize=11,
    fontweight="bold",
)

# Top-left strip: x × (b/2)
ax_sq.add_patch(
    plt.Rectangle(
        (0, x_len),
        x_len,
        half_b,
        facecolor="#F5A623",
        edgecolor="black",
        linewidth=1.5,
        alpha=0.7,
    )
)
ax_sq.text(
    x_len / 2,
    x_len + half_b / 2,
    r"$\frac{b}{2}\!x$",
    ha="center",
    va="center",
    fontsize=11,
    fontweight="bold",
)

# Top-right corner: (b/2)² — the subtracted piece
ax_sq.add_patch(
    plt.Rectangle(
        (x_len, x_len),
        half_b,
        half_b,
        facecolor="#E74C3C",
        edgecolor="black",
        linewidth=1.5,
        alpha=0.4,
        hatch="///",
    )
)
ax_sq.text(
    x_len + half_b / 2,
    x_len + half_b / 2,
    r"$\left(\!\frac{b}{2}\!\right)^{\!2}$",
    ha="center",
    va="center",
    fontsize=9,
    fontweight="bold",
    color="#C0392B",
)

# Bottom dimension labels: x then b/2
ax_sq.annotate(
    "",
    xy=(x_len, -0.4),
    xytext=(0, -0.4),
    arrowprops=dict(arrowstyle="<->", color="black", lw=1.5),
)
ax_sq.text(x_len / 2, -0.7, "$x$", ha="center", va="center", fontsize=13)

ax_sq.annotate(
    "",
    xy=(side, -0.4),
    xytext=(x_len, -0.4),
    arrowprops=dict(arrowstyle="<->", color="black", lw=1.5),
)
ax_sq.text(
    x_len + half_b / 2,
    -0.7,
    r"$\frac{b}{2}$",
    ha="center",
    va="center",
    fontsize=13,
)

# Left dimension labels: x then b/2
ax_sq.annotate(
    "",
    xy=(-0.4, x_len),
    xytext=(-0.4, 0),
    arrowprops=dict(arrowstyle="<->", color="black", lw=1.5),
)
ax_sq.text(-0.8, x_len / 2, "$x$", ha="center", va="center", fontsize=13)

ax_sq.annotate(
    "",
    xy=(-0.4, side),
    xytext=(-0.4, x_len),
    arrowprops=dict(arrowstyle="<->", color="black", lw=1.5),
)
ax_sq.text(
    -0.8,
    x_len + half_b / 2,
    r"$\frac{b}{2}$",
    ha="center",
    va="center",
    fontsize=13,
)

ax_sq.set_xlim(-1.5, side + 0.5)
ax_sq.set_ylim(-1.2, side + 0.5)
ax_sq.set_aspect("equal")
ax_sq.axis("off")
ax_sq.set_title(
    r"$\left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2$"
    + "\n(square minus corner)",
    fontsize=13,
    pad=10,
)

fig_geo.tight_layout()
st.pyplot(fig_geo)

st.write(r"""The blue region ($x^{2}$) is common to both shapes.  In the rectangle,
the orange strip has area $bx$.  In the square, that same $bx$ area is split
into two strips of $\tfrac{b}{2}\,x$ each, placed on adjacent sides.
Completing the big square introduces the red corner of area
$\left(\tfrac{b}{2}\right)^{2}$, which must be subtracted to keep the total
area equal.""")


# ── General Formula ─────────────────────────────────────────────────────────────

st.markdown("#### General Formula")

st.write(r"Any quadratic $ax^{2} + bx + c$ with $a \neq 0$ can be rewritten as:")

latex_code = (
    r"ax^{2} + bx + c = a\!\left(x + \frac{b}{2a}\right)^{2} + c - \frac{b^{2}}{4a}"
)
st.code(latex_code, language="latex")
st.latex(latex_code)

st.write(r"""Where:
- $$h = -\dfrac{b}{2a}$$ is the $$x$$-coordinate of the vertex
- $$k = c - \dfrac{b^{2}}{4a}$$ is the $$y$$-coordinate of the vertex
- The vertex form is $$a(x - h)^{2} + k$$
""")


# ── Interactive Section ─────────────────────────────────────────────────────────

st.divider()
st.markdown("#### Interactive Example")

st.write(
    "Enter the coefficients of a quadratic expression to see the completing-the-square"
    " process step by step."
)

col_input, col_spacer, col_result = st.columns([2, 1, 4])

with col_input:
    a_val = st.number_input("Coefficient a (x² term)", value=3, step=1, key="cts_a")
    b_val = st.number_input("Coefficient b (x term)", value=6, step=1, key="cts_b")
    c_val = st.number_input(
        "Coefficient c (constant term)", value=1, step=1, key="cts_c"
    )

    if a_val == 0:
        st.warning("Coefficient *a* must not be zero for a quadratic expression.")
        st.stop()

# ── Symbolic computation ────────────────────────────────────────────────────────

x = sp.Symbol("x")
original_expr = a_val * x**2 + b_val * x + c_val

h = sp.Rational(-b_val, 2 * a_val)
k = c_val - sp.Rational(b_val**2, 4 * a_val)
vertex_form = a_val * (x - h) ** 2 + k

with col_result:

    # Step 1 – Original expression
    st.markdown("**Step 1 — Original expression**")
    latex_original = sp.latex(original_expr)
    st.code(latex_original, language="latex")
    st.latex(latex_original)

    # Step 2 – Factor out a (if a ≠ 1)
    if a_val != 1:
        st.markdown(f"**Step 2 — Factor out {a_val} from the first two terms**")
        inner_b = sp.Rational(b_val, a_val)
        latex_factor = (
            f"{sp.latex(sp.Integer(a_val))}"
            r"\!\left("
            f"{sp.latex(x**2 + inner_b * x)}"
            r"\right)"
            f" + {sp.latex(sp.Integer(c_val))}"
        )
        st.code(latex_factor, language="latex")
        st.latex(latex_factor)
        next_step = 3
    else:
        next_step = 2

    # Step – Half the coefficient of x, square it, add and subtract
    half_b_over_a = sp.Rational(b_val, 2 * a_val)
    square_term = half_b_over_a**2

    st.markdown(
        f"**Step {next_step} — Half the coefficient of x inside the bracket is"
        f" $${sp.latex(half_b_over_a)}$$, square it to get $${sp.latex(square_term)}$$**"
    )

    # Show the completing-the-square algebra
    inner_b = sp.Rational(b_val, a_val)
    a_times_sq = sp.Integer(a_val) * square_term
    constant_combined = sp.Integer(c_val) - a_times_sq

    def _signed_latex(val):
        """Return ' + <val>' or ' - <|val|>' for LaTeX."""
        if val >= 0:
            return f" + {sp.latex(val)}"
        return f" - {sp.latex(-val)}"

    inner_poly = sp.latex(x**2 + inner_b * x)
    sq_str = sp.latex(square_term)
    pf_sq = sp.latex((x + half_b_over_a) ** 2)

    if a_val != 1:
        a_str = sp.latex(sp.Integer(a_val))
        c_signed = _signed_latex(sp.Integer(c_val))

        # Add and subtract square_term inside the bracket
        st.latex(
            f"{a_str}"
            r"\!\left("
            f"{inner_poly} + {sq_str} - {sq_str}"
            r"\right)"
            f"{c_signed}"
        )

        # Rewrite as perfect square inside the bracket
        st.latex(f"{a_str}" r"\!\left(" f"{pf_sq} - {sq_str}" r"\right)" f"{c_signed}")

        # Distribute a and show separate constants
        st.latex(
            f"{a_str}{pf_sq}"
            f"{_signed_latex(-a_times_sq)}"
            f"{_signed_latex(sp.Integer(c_val))}"
        )

        # Combine constants
        st.latex(f"{a_str}{pf_sq}" f"{_signed_latex(constant_combined)}")
    else:
        c_signed = _signed_latex(sp.Integer(c_val))

        # Add and subtract square_term
        st.latex(f"{inner_poly} + {sq_str} - {sq_str}" f"{c_signed}")

        # Rewrite as perfect square
        st.latex(f"{pf_sq} - {sq_str}" f"{c_signed}")

        # Combine constants
        st.latex(f"{pf_sq}" f"{_signed_latex(constant_combined)}")

    next_step += 1

    # Step – Write in vertex form
    st.markdown(f"**Step {next_step} — Write in vertex form**")
    latex_vertex = sp.latex(vertex_form)
    st.code(latex_vertex, language="latex")
    st.latex(latex_vertex)

    st.write(
        f"The vertex of the parabola is at $$\\left({sp.latex(h)},\\; {sp.latex(k)}\\right)$$."
    )


# ── SymPy verification ─────────────────────────────────────────────────────────

st.divider()
st.markdown("#### Python Verification with SymPy")

code_snippet = f"""\
import sympy as sp

x = sp.Symbol("x")
expr = {a_val}*x**2 + {b_val}*x + {c_val}

# Compute vertex form components
a, b, c = {a_val}, {b_val}, {c_val}
h = sp.Rational(-b, 2*a)
k = c - sp.Rational(b**2, 4*a)
vertex_form = a * (x - h)**2 + k

st.write("Original:", expr)
st.write("Vertex form:", vertex_form)
st.write("Vertex: (h, k) =", f"({{h}}, {{k}})")
st.write("Expanded back:", sp.expand(vertex_form))
st.write("Equivalent:", sp.simplify(expr - vertex_form) == 0)
"""

col1, _ = st.columns([4, 2])
with col1:
    st.code(code_snippet, language="python")
    exec(code_snippet)


# ── Solving the equation ────────────────────────────────────────────────────────

st.divider()
st.markdown("#### Solving the Equation")

st.write(
    f"Setting $${sp.latex(original_expr)} = 0$$ and solving using the vertex form:"
)

solutions = sp.solve(original_expr, x)

if solutions:
    for i, sol in enumerate(solutions):
        latex_sol = f"x_{{{i+1}}} = {sp.latex(sol)}"
        st.code(latex_sol, language="latex")
        st.latex(latex_sol)

    if all(sp.im(sol) == 0 for sol in solutions):
        st.write("Both roots are real.")
    else:
        st.write("The roots are complex (the parabola does not cross the x-axis).")
else:
    st.write("No solutions found.")


# ── Plot ────────────────────────────────────────────────────────────────────────

st.divider()
st.markdown("#### Graph of the Parabola")

h_float = float(h)
k_float = float(k)

x_range = max(abs(h_float) + 5, 10)
x_vals = np.linspace(h_float - x_range, h_float + x_range, 500)
y_vals = float(a_val) * (x_vals - h_float) ** 2 + k_float

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_vals, y_vals, color="blue", label=f"${sp.latex(original_expr)}$")
ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)

# Mark vertex
ax.plot(h_float, k_float, "ro", markersize=8, label=f"Vertex ({h_float}, {k_float})")

# Mark real roots
real_solutions = [sol for sol in solutions if sp.im(sol) == 0]
for sol in real_solutions:
    sol_float = float(sol)
    ax.plot(sol_float, 0, "gx", markersize=10, markeredgewidth=2)

# Draw axis of symmetry
ax.axvline(
    h_float,
    color="red",
    linestyle="--",
    alpha=0.5,
    label=f"Axis of symmetry x = {h_float}",
)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Quadratic Parabola")
ax.legend()
ax.grid(True, alpha=0.3)

st.pyplot(fig)


# ── Why it is useful ────────────────────────────────────────────────────────────

st.divider()
st.markdown("#### Why Completing the Square is Useful")

st.write("""
- **Solving quadratics** when factorisation is difficult
- **Deriving the quadratic formula** — the proof uses completing the square on the general form $$ax^{2} + bx + c = 0$$
- **Graphing parabolas** — the vertex form directly gives the vertex $$(h, k)$$ and direction of opening
- **Calculus** — appears in Gaussian integrals and other integration techniques
""")
