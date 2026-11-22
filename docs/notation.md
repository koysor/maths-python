# Notation guide

Every mathematical symbol used in [maths-python](https://github.com/koysor/maths-python) and [quant-finance](https://github.com/koysor/quant-finance), plus the notation of the private study notes that sit alongside them, with what each symbol means.  Where one symbol has several meanings, or one idea has several symbols, the [Overloaded symbols](#overloaded-symbols) section says which to read where.

**How to read the tables.**  The *Used in* column says which public repo uses the symbol: **MP** is maths-python, **QF** is quant-finance.  A dash means the symbol appears only in the private notes.  The *Meaning* column gives the usual meaning; *Notes* gives alternatives and traps.

**Keeping it current.**  This guide must be checked on every code change in maths-python, quant-finance or the private notes.  When a change adds a symbol, drops the last use of one, or gives a symbol a new meaning, update the table here in the same piece of work.  See the "Notation guide" section of each repo's `CLAUDE.md`.

## Contents

- [Writing maths](#writing-maths)
- [General and set notation](#general-and-set-notation)
- [Algebra, functions and logarithms](#algebra-functions-and-logarithms)
- [Calculus](#calculus)
- [Linear algebra](#linear-algebra)
- [Probability and statistics](#probability-and-statistics)
- [Time series and econometrics](#time-series-and-econometrics)
- [Stochastic calculus](#stochastic-calculus)
- [Options, pricing and Greeks](#options-pricing-and-greeks)
- [Volatility surfaces](#volatility-surfaces)
- [Interest rates and fixed income](#interest-rates-and-fixed-income)
- [Portfolio theory and risk](#portfolio-theory-and-risk)
- [Numerical methods](#numerical-methods)
- [Machine learning](#machine-learning)
- [Overloaded symbols](#overloaded-symbols)
- [Differences between repos](#differences-between-repos)

## Writing maths

| Where | Inline | Display |
|---|---|---|
| Streamlit pages (MP, QF apps) | `$...$` in `st.markdown`, or `st.latex(r"...")` | `$$...$$` or `st.latex` |
| marimo and Jupyter notebooks | `$...$` | `$$...$$` |
| quant-finance library docs (Zensical/MathJax) and docstrings | `\( ... \)` | `\[ ... \]` |
| This guide (GitHub Markdown) | `$...$` | `$$...$$` |

Units (years, continuously compounded decimal rates, annualised volatility) and the scaling of the Greeks are defined in quant-finance's [Conventions](https://github.com/koysor/quant-finance/blob/main/docs/conventions.md) page; this guide does not repeat them.

## General and set notation

| Symbol | Meaning | Used in | Notes |
|---|---|---|---|
| $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$ | Natural numbers, integers, rationals, reals, complex numbers | MP | $\mathbb{Q}$ also names the risk-neutral measure; see [Overloaded symbols](#overloaded-symbols) |
| $\mathbb{R}^n$ | $n$-dimensional real vectors | MP | |
| $x \in A$, $x \notin A$ | $x$ is (is not) an element of $A$ | MP | |
| $A \cup B$, $A \cap B$, $A \subset B$ | Union, intersection, subset | — | |
| $A'$ | Complement of event $A$ | — | Also the transpose of a matrix; see [Linear algebra](#linear-algebra) |
| $\emptyset$, $\mathcal{S}$ | Empty set; sample space | — | $\mathcal{S}$ is also a state space in reinforcement learning |
| $\forall$, $\exists$ | For all, there exists | — | |
| $\Rightarrow$, $\iff$ | Implies, if and only if | MP | |
| $\approx$, $\propto$, $\equiv$ | Approximately equal, proportional to, identically equal / equivalent | MP, QF | |
| $\ll$, $\gg$ | Much less than, much greater than | — | |
| $\infty$ | Infinity | MP, QF | |
| $\sum$, $\prod$ | Sum, product | MP, QF | |
| $n!$, $\binom{n}{k}$ | Factorial; binomial coefficient, $\frac{n!}{k!(n-k)!}$ | MP, QF | |
| $\lvert x \rvert$ | Absolute value | MP, QF | |
| $\lfloor x \rfloor$, $\lceil x \rceil$ | Floor, ceiling | — | |
| $\max$, $\min$, $\arg\max$, $\arg\min$, $\sup$, $\inf$ | Maximum, minimum, the argument achieving them, supremum, infimum | MP, QF | |
| $x^+$, $(x)^+$ | $\max(x, 0)$ | — | Payoffs are usually written with $\max$ in QF |
| $x^*$ | Optimal value of $x$ | QF | $w^*$ is the optimal weight |
| $a \bmod n$ | Remainder after dividing $a$ by $n$ | — | |

## Algebra, functions and logarithms

| Symbol | Meaning | Used in | Notes |
|---|---|---|---|
| $f(x)$, $g(x)$ | Functions of $x$ | MP, QF | |
| $f^{-1}$ | Inverse function | — | Not $1/f$ |
| $f \circ g$ | Composition, $f(g(x))$ | — | |
| $e$ | Euler's number, $2.71828\ldots$ | MP, QF | |
| $\exp(x)$ | $e^x$ | MP, QF | |
| $\ln x$ | Natural logarithm (base $e$) | MP, QF | |
| $\log x$, $\log_b x$ | Logarithm; to base $b$ | MP | Unsubscripted $\log$ means $\ln$ in the finance material |
| $i$ | Imaginary unit, $i^2 = -1$ | MP | Also an index; see [Overloaded symbols](#overloaded-symbols) |
| $z = a + bi$, $\bar{z}$, $\lvert z \rvert$ | Complex number, its conjugate, its modulus | MP | |
| $\sin, \cos, \tan, \sec, \mathrm{cosec}, \cot$ | Trigonometric functions | MP | |
| $\arcsin, \arctan$, $\sin^{-1}$ | Inverse trigonometric functions | — | $\sin^{-1}x$ means $\arcsin x$, not $1/\sin x$ |
| $\sinh, \cosh, \tanh$ | Hyperbolic functions | — | |
| $\pi$ | $3.14159\ldots$ | MP, QF | Also a policy in reinforcement learning |
| $a, b, c$ | Coefficients of a polynomial, e.g. $ax^2 + bx + c$ | MP | |
| $a^x$, $a$ | Exponential with constant base $a$ | — | $\frac{d}{dx}a^x = a^x \ln a$ |
| $C$ | Constant of integration | MP | Also a call price; see [Overloaded symbols](#overloaded-symbols) |
| $c_1$, $c_2$ | Constants of integration, when there are several | — | |

## Calculus

| Symbol | Meaning | Used in | Notes |
|---|---|---|---|
| $\frac{dy}{dx}$, $f'(x)$, $\dot{x}$ | First derivative | MP | $\dot{x}$, a derivative with respect to time, appears only in the private notes |
| $\frac{d^2y}{dx^2}$, $f''(x)$ | Second derivative | MP | |
| $\frac{\partial f}{\partial x}$, $f_x$, $\partial_x f$ | Partial derivative | MP, QF | Subscripts such as $V_S$, $w_\tau$, $w_y$ are partial derivatives |
| $\frac{\partial^2 f}{\partial x\,\partial y}$ | Mixed partial derivative | MP | |
| $\nabla f$, $\nabla_x f$ | Gradient (vector of partial derivatives) | — | |
| $\int f(x)\,dx$, $\int_a^b f(x)\,dx$ | Indefinite and definite integral | MP | |
| $\iint$ | Double integral | — | |
| $\lim_{x \to a}$ | Limit | MP | |
| $\delta x$ | A small (finite) increment of $x$ | QF | $\delta t$ is a small time step |
| $\Delta x$ | A finite change in $x$ | MP, QF | $\Delta t$ is a time step; $\Delta$ is also the option delta |
| $h$ | Step size in a finite difference | MP | |
| $h(x)$ | A smooth test function in a derivation | — | Not the step size $h$ |
| $O(h^n)$ | Order of the error, $\le c\,h^n$ for small $h$ | MP, QF | |
| $u, v$ | Parts in integration by parts, $\int u\,dv = uv - \int v\,du$; the substitution variable | MP | |
| $x(t), y(t)$ | Parametric curve | MP | |
| $L(x, y, \lambda)$, $\mathcal{L}$ | Lagrangian | MP | |
| $\lambda$ | Lagrange multiplier | MP | |
| $\xi$ | Similarity variable in a PDE, e.g. $\xi = y/\sqrt{t}$ | — | |
| $u(x, t)$, $v(x, t)$ | Unknown functions in a PDE, before and after a substitution | — | $a$ and $b$ are constant coefficients in $u_t = u_{xx} + a u_x + b u$ |
| $\alpha, \beta$ | Constants in the substitution $u = e^{\alpha x + \beta t}v$ | — | Chosen to reduce a PDE to the heat equation $v_t = v_{xx}$ |
| $w(z, t)$, $z = x + at$ | Unknown function and position in a moving frame | — | |

## Linear algebra

| Symbol | Meaning | Used in | Notes |
|---|---|---|---|
| $\mathbf{a}, \mathbf{v}, \vec{v}$ | Vector | MP, QF | Bold lower case |
| $\hat{\mathbf{a}}$ | Unit vector, $\mathbf{a}/\lVert\mathbf{a}\rVert$ | MP | A hat also marks an estimate |
| $\lVert \mathbf{a} \rVert$ | Euclidean norm (length) | MP | |
| $\mathbf{a} \cdot \mathbf{b}$, $\mathbf{a}^\top \mathbf{b}$ | Dot product | MP, QF | |
| $\mathbf{a} \times \mathbf{b}$ | Cross product | MP | |
| $A, B, \mathbf{A}$ | Matrix | MP, QF | |
| $a_{ij}$, $C_{ij}$ | Entry in row $i$, column $j$ | MP, QF | |
| $A^\top$, $A'$ | Transpose | MP, QF | QF uses $^\top$; the private notes often use $'$, e.g. $w'\Sigma w$ |
| $A^{-1}$ | Inverse | MP, QF | |
| $\det(A)$, $\lvert A \rvert$ | Determinant | MP | |
| $\mathrm{adj}(A)$ | Adjugate | — | |
| $\mathrm{tr}(A)$ | Trace | — | |
| $\mathrm{diag}(\sigma)$ | Diagonal matrix with $\sigma$ on the diagonal | MP, QF | |
| $I$, $I_n$ | Identity matrix | MP | Also an information set; see [Time series](#time-series-and-econometrics) |
| $\mathbf{0}$, $\mathbf{1}$ | Vector of zeros; vector of ones | MP | $\mathbf{1}_{A}$ is also an indicator; see [Probability](#probability-and-statistics) |
| $\lambda$, $\mathbf{v}$ | Eigenvalue and eigenvector, $A\mathbf{v} = \lambda\mathbf{v}$ | MP | |
| $\Lambda$, $Q$ | Diagonal matrix of eigenvalues; matrix of eigenvectors, $A = Q \Lambda Q^\top$ | — | |
| $L$, $U$ | Lower and upper triangular factors (Cholesky, LU) | — | |
| $\mathbf{x} = A^{-1}\mathbf{b}$ | Solution of $A\mathbf{x} = \mathbf{b}$ | MP | |

## Probability and statistics

| Symbol | Meaning | Used in | Notes |
|---|---|---|---|
| $X, Y, Z$ | Random variables | MP, QF | $Z$ is usually standard normal |
| $x, y$ | Values (realisations) of $X, Y$ | MP, QF | |
| $P(A)$, $\Pr(A)$, $\mathrm{P}(A)$ | Probability of event $A$ | MP, QF | Not the same as the measure $\mathbb{P}$ |
| $P(A \mid B)$ | Conditional probability | — | |
| $\mathbb{E}[X]$, $E[X]$, $E(X)$ | Expectation | MP, QF | Preferred: $\mathbb{E}[X]$ |
| $\mathbb{E}[X \mid \mathcal{F}_t]$ | Conditional expectation given information at time $t$ | — | |
| $\mathrm{Var}(X)$, $\text{Var}[X]$ | Variance | MP, QF | Written `\operatorname{Var}` in quant-finance and `\text{Var}` elsewhere |
| $\mathbb{V}[X]$ | Variance | — | The lecture-note form of $\mathrm{Var}[X]$ |
| $\mathrm{Cov}(X, Y)$ | Covariance | MP, QF | |
| $\mu$ | Mean | MP, QF | Also drift; see [Stochastic calculus](#stochastic-calculus) |
| $\sigma$, $\sigma^2$ | Standard deviation, variance | MP, QF | Also volatility |
| $\sigma_{ij}$, $\sigma_{XY}$ | Covariance of $i$ and $j$ | MP, QF | |
| $\rho$, $\rho_{XY}$, $\rho_{ij}$ | Correlation coefficient | MP, QF | Also the option Greek rho |
| $\bar{x}$, $s$ | Sample mean, sample standard deviation | MP, QF | $\bar{\phi}$ is the sample mean of draws of $\phi$ |
| $\hat{\theta}$ | Estimate of parameter $\theta$ | — | e.g. $\hat{\beta}$ |
| $n$ | Sample size; number of trials | MP, QF | |
| $X \sim D$ | $X$ has distribution $D$ | MP, QF | |
| $\mathcal{N}(\mu, \sigma^2)$ | Normal distribution | MP | QF writes $N(0, \Delta t)$; see [Differences](#differences-between-repos) |
| $\phi(x)$ | Standard normal PDF | MP | QF writes $n(x)$; MP writes $f(x)$ where $\phi$ is the random variable |
| $\phi$, $\phi_i$ | Standard normal random variable; its $i$-th realisation | MP | $\phi \sim \mathcal{N}(0, 1)$; not the density $\phi(x)$ |
| $\Phi(x)$, $N(x)$ | Standard normal CDF | MP, QF | $N$ in pricing formulas, $\Phi$ in statistics |
| $\Phi^{-1}$, $N^{-1}$ | Inverse normal CDF (quantile) | MP | MP writes $\Phi^{-1}$ |
| $z$, $z_\alpha$ | $z$-score; normal quantile at level $\alpha$ | MP | |
| $\mathrm{LogN}(\mu, \sigma^2)$ | Lognormal distribution | — | |
| $\mathrm{Bin}(n, p)$, $p$ | Binomial distribution; success probability | MP | $p$ is also a probability in a tree |
| $\mathrm{Po}(\lambda)$, $\lambda$ | Poisson distribution; its rate | MP | |
| $k$, $\theta$ | Shape and scale of a gamma distribution | — | Density proportional to $x^{k-1}e^{-x/\theta}$ |
| $U[0, 1]$, $u$ | Uniform distribution; a draw from it | MP | $\phi = \Phi^{-1}(u)$ in inverse transform sampling |
| $a, b$ | Endpoints of an interval, as in $P(a \le \phi \le b)$ | MP | Also polynomial coefficients |
| $t_\nu$, $\nu$ | Student's $t$ distribution; degrees of freedom | MP | |
| $\chi^2_k$ | Chi-squared distribution with $k$ degrees of freedom | — | |
| $f(x)$, $F(x)$ | PDF, CDF | MP, QF | $f_{\mathbb{Q}}$ is the risk-neutral density |
| $\mathbf{1}_{A}$, $\mathbf{1}_{\lbrace S_T \ge K \rbrace}$ | Indicator: 1 if $A$ holds, else 0 | — | |
| $\boldsymbol{\mu}$, $\Sigma$, $\boldsymbol{\Sigma}$ | Mean vector; covariance matrix | MP, QF | |
| $\mathbf{R}$, $R$ | Correlation matrix, $\Sigma = DRD$ | MP, QF | Also a return; see [Overloaded symbols](#overloaded-symbols) |
| $H_0$, $H_1$ | Null and alternative hypotheses | — | |
| $\alpha$ | Significance level, or confidence level for VaR | — | Also Jensen's alpha and a GARCH coefficient |
| $\kappa$ | Kurtosis, $\mathbb{E}[(X-\mu)^4]/\sigma^4$ | — | Also a mean-reversion speed and a cost rate |
| $S$, $K$ (in $\text{JB}$) | Skewness, kurtosis in the Jarque–Bera statistic | — | Clashes with spot and strike |
| $\text{JB}$, $\text{LR}$ | Jarque–Bera statistic; likelihood ratio statistic | — | |
| $L(\theta)$, $\ell(\theta)$ | Likelihood, log-likelihood | — | |
| $\zeta$ | $1/\nu$, tail-heaviness parameter | — | |
| $\psi_i$ | Uniform random variates; a sampling density | — | |

## Time series and econometrics

| Symbol | Meaning | Used in | Notes |
|---|---|---|---|
| $r_t$ | Return at time $t$ | — | Also the short rate |
| $\varepsilon_t$, $u_t$ | Error or shock term | — | |
| $\mathcal{I}_{t-1}$ | Information set up to $t-1$ | — | |
| $h_t$, $\sigma_t^2$ | Conditional variance | — | |
| $\omega, \alpha, \beta$ | GARCH(1,1): $\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2$ | — | |
| $\gamma$ | GJR-GARCH leverage coefficient | — | |
| $V$ | Long-run variance, $\omega/(1 - \alpha - \beta)$ | — | Also an option value |
| $L$ | Lag operator, $L r_t = r_{t-1}$ | — | |
| $X$, $\beta$, $\hat{\beta}$ | Regressor matrix, coefficients and their estimate | — | |
| $\Omega$ | Residual covariance in GLS | — | Also the view uncertainty in Black–Litterman |
| $\mathbb{R}^2$, $R^2$ | Coefficient of determination | — | |

## Stochastic calculus

| Symbol | Meaning | Used in | Notes |
|---|---|---|---|
| $W_t$, $W(t)$ | Brownian motion (Wiener process) | MP, QF | Preferred letter.  $B_t$ appears occasionally |
| $dW_t$, $dX$ | Brownian increment | MP, QF | $dX$ is the lecture-note letter for the same thing; see [Differences](#differences-between-repos) |
| $W^{\mathbb{Q}}_t$ | Brownian motion under $\mathbb{Q}$ | — | |
| $\mathbb{P}$ | Real-world (physical) measure | — | |
| $\mathbb{Q}$ | Risk-neutral measure | QF | |
| $\mathbb{E}^{\mathbb{Q}}[\cdot]$ | Expectation under $\mathbb{Q}$ | — | |
| $\frac{d\mathbb{Q}}{d\mathbb{P}}$, $\Lambda$, $Z_t$ | Radon–Nikodym derivative; its density process | — | |
| $\theta_t$ | Girsanov kernel (market price of risk) | — | |
| $\mathcal{F}_t$ | Filtration: the information known at time $t$ | — | |
| $M_t$ | Martingale | — | |
| $dS = \mu S\,dt + \sigma S\,dW_t$ | Geometric Brownian motion | MP, QF | |
| $\mu$ | Drift | MP, QF | |
| $\sigma$ | Volatility (diffusion coefficient) | MP, QF | |
| $A(\cdot)$, $B(\cdot)$ | Drift and diffusion of a general SDE, $dG = A\,dt + B\,dX$ | — | Sometimes the other way round, $dS = A\,dW_t + B\,dt$: read which differential each multiplies |
| $G$ | A generic diffusion process | — | $A$, $B$, $C$ can also be constants inside a particular SDE |
| $\delta W$ | Brownian increment over a finite step $\delta t$ | — | |
| $\psi = \sqrt{dt}\,\phi$ | Standard normal draw scaled to one time step | — | Mean $0$, variance $dt$ |
| $F(W_t, t)$ | Function of Brownian motion and time in Itô's lemma | — | $q(t)$ is an arbitrary function of time added to $F$ |
| $\overline{F}(W_t)$, $G(W_\tau)$ | Boundary term and integrand of the time integral when a stochastic integral is rewritten | — | $\int_0^t f(W_\tau)\,dW_\tau = \overline{F}(W_t) + \int_0^t G(W_\tau)\,d\tau$ |
| $F_t$, $G_t$; $F_0$, $G_0$ | A process defined as a function of $W_t$ and $t$; its starting value | — | $F_t$ is not a forward price here |
| $Y = f(Z)$ | A process $Z$ and its transform $Y$ | — | e.g. $Z = \log y$, so $Y = e^Z = y$; $Z$ is not a normal draw here |
| $\alpha$, $\beta$, $\delta$ | Drift constant, mean-reversion speed and diffusion constant of a log process | — | $d(\log y) = (\alpha - \beta\log y)\,dt + \delta\,dW_t$ |
| $m(t)$ | Mean of a stochastic process at time $t$ | — | Found by averaging its SDE, e.g. $dm/dt = \tfrac{1}{2}(\ln a)^2 m$ for $a^{W_t}$ |
| $\int_0^t H_\tau\,dW_\tau$ | Stochastic (Itô) integral of the integrand $H$ | — | $\tau$ is the running time; each $H_{t_i}$ is taken at the start of its step |
| $W_i$ | Brownian motion after $i$ time steps | — | $W_{i+1} - W_i$ is the next increment |
| $(dW)^2 = dt$ | Itô multiplication rule | — | |
| $-\tfrac{1}{2}\sigma^2$ | Itô correction | QF | |
| $p(y, t; y', t')$ | Transition probability density | — | Used in Fokker–Planck and backward Kolmogorov equations |
| $p(r, t)$, $p_\infty(r)$ | Probability density of a process; its steady state | — | |
| $u(r, t)$, $w(r, t)$ | Drift and diffusion in the Fokker–Planck equation | — | $dr = u\,dt + w\,dW_t$ |
| $J$ | Probability flux | — | $J = up - \tfrac{1}{2}\partial_r(w^2 p)$; zero at a no-flow boundary |
| $\nu$, $\beta$ | Scale and power of a rate-dependent diffusion | — | $w = \nu r^\beta$ |
| $c^2$ | Diffusion coefficient of a random walk | — | |
| $\gamma$, $\kappa$ | Mean-reversion speed | — | Vasicek: $dr = \gamma(\bar{r} - r)\,dt + \sigma\,dX$, or $\kappa(\theta - r)$ |
| $\bar{r}$, $\theta$ | Long-run mean level | — | |
| $\phi$, $\varepsilon$ | Standard normal draw in a discretised SDE, e.g. $\sigma\phi\sqrt{\delta t}$ | MP | QF writes $Z$ |

## Options, pricing and Greeks

| Symbol | Meaning | Used in | Notes |
|---|---|---|---|
| $S$, $S_t$, $S_0$ | Underlying price; at time $t$; today | MP, QF | |
| $S_T$ | Underlying price at expiry | QF | |
| $S_i$ | Underlying price after $i$ time steps | — | |
| $K$ | Strike | QF | |
| $T$ | Expiry; in QF also the time to expiry in years | QF | See $\tau$ |
| $t$ | Current time | MP, QF | |
| $\tau = T - t$ | Time to expiry | — | QF uses $T$ for this |
| $r$ | Risk-free rate, continuously compounded | QF | |
| $q$ | Continuous dividend yield | QF | Also a position quantity in payoffs |
| $\sigma$ | Volatility | QF | $\sigma_{\text{imp}}$ implied, $\sigma_{\text{loc}}$ local |
| $V$, $V(S, t)$ | Option value (generic) | QF | |
| $C$, $P$ | Call and put prices | QF | |
| $c$, $p$ | Call and put premiums paid | QF | $p$ is also a probability |
| $d_1, d_2$ | Black–Scholes terms, $d_{1,2} = \frac{\ln(S/K) + (r - q \pm \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$ | QF | |
| $\phi$ | $+1$ for a call, $-1$ for a put | QF | Also the normal PDF and a normal draw |
| $\phi_i$, $q_i$ | Sign and quantity of leg $i$ of a strategy | QF | |
| $\Pi$ | Value of a hedged portfolio, e.g. $\Pi = V - \Delta S$ | QF | Also Black–Litterman equilibrium returns |
| $\Delta$ | Delta, $\partial V/\partial S$ | QF | Also the hedge ratio held |
| $\Gamma$ | Gamma, $\partial^2 V/\partial S^2$ | QF | |
| $\Theta$ | Theta, $\partial V/\partial t$ | QF | |
| $\mathcal{V}$ | Vega, $\partial V/\partial \sigma$ | QF | Not $\nu$ |
| $\rho$ | Rho, $\partial V/\partial r$ | QF | Also correlation |
| $\delta_{BS}$ | Black–Scholes delta, lower case to keep it apart from a price change $\Delta S$ | — | |
| $\text{Payoff}(S_T)$ | Payoff at expiry | QF | e.g. $\max(S_T - K, 0)$ |
| $u$, $d$ | Up and down factors in a binomial tree | MP, QF | $d$ is also a differential |
| $p$ | Risk-neutral probability of an up move | QF | |
| $D_T$, $F_T$ | Discount factor and forward price to $T$ | — | |
| $\kappa$, $\nu$ | Transaction cost rate; shares traded | — | |
| $\Lambda(S)$ | Exotic payoff in static hedging | — | |
| $r_b$, $r_q$ | Interest rates of the base and quote currencies of an FX pair (Garman–Kohlhagen) | — | $r_b$ plays the role of $q$; written this way because "domestic" and "foreign" are used both ways round |

## Volatility surfaces

| Symbol | Meaning | Used in | Notes |
|---|---|---|---|
| $\sigma_{\text{imp}}$, $\sigma^{\text{mkt}}_{ij}$ | Implied volatility; market quote at expiry $T_i$, strike $K_j$ | QF | |
| $\sigma_{\text{loc}}$ | Local volatility (Dupire) | — | |
| $y = \ln(K/F_T)$ | Log-moneyness | — | Also a generic variable |
| $w(T, y) = T\,\sigma_{\text{imp}}^2$ | Total implied variance | — | Also portfolio weights |
| $g$ | Denominator of the Dupire formula in $(w, y)$ form | — | |
| $\text{RR}_{25}$, $\text{BF}_{25}$ | 25-delta risk reversal (call vol minus put vol, a measure of skew) and butterfly (average wing vol minus ATM vol, a measure of curvature) | — | FX quoting convention |

## Interest rates and fixed income

| Symbol | Meaning | Used in | Notes |
|---|---|---|---|
| $r$, $r_t$ | Short rate; risk-free rate | QF | |
| $R$ | Annually compounded rate, $r = \ln(1 + R)$ | QF | |
| $z(T)$ | Zero-coupon (spot) rate to $T$ | QF | |
| $P(T)$, $Z(t; T)$ | Discount factor (zero-coupon bond price), $P(T) = e^{-z(T)T}$ | QF | $P$ is also a put price |
| $\text{PV}$ | Present value | — | |
| $\text{XCCY}$ | Cross-currency basis | — | |

## Portfolio theory and risk

| Symbol | Meaning | Used in | Notes |
|---|---|---|---|
| $\mathbf{w}$, $w_i$ | Portfolio weights, summing to one | MP, QF | |
| $\mu_p$, $\sigma_p$ | Portfolio expected return and volatility | QF | Private notes write $\mu_\Pi$, $\sigma_\Pi$ |
| $R_i$, $R_m$, $R_f$ | Return on asset $i$, the market, the risk-free asset | QF | |
| $\beta_i$ | Beta, $\mathrm{Cov}(R_i, R_m)/\sigma_m^2$ | QF | |
| $\alpha_i$ | Jensen's alpha | QF | |
| $\lambda$ | Risk aversion; a factor risk premium (APT) | — | Also eigenvalue, Lagrange multiplier, Poisson rate |
| $\Pi$, $P$, $Q$, $\Omega$, $\tau$ | Black–Litterman: equilibrium returns, pick matrix, view returns, view uncertainty, prior scaling | — | Every one of these letters means something else elsewhere |
| $\text{VaR}_\alpha$, $\text{ES}$ | Value at Risk at level $\alpha$; Expected Shortfall | — | |
| $L$ | Loss | — | |
| $\text{PD}$, $\text{LGD}$, $\text{EAD}$ | Probability of default, loss given default, exposure at default | — | |
| $\text{IR}$, $\omega_I$ | Information ratio; tracking error | — | |
| $\text{SR}$ | Sharpe ratio, $(\mu_p - R_f)/\sigma_p$ | QF | QF names it in words rather than with a symbol |

## Numerical methods

| Symbol | Meaning | Used in | Notes |
|---|---|---|---|
| $\delta t$, $\Delta t$ | Time step | MP, QF | |
| $n$, $N$ | Number of time steps | QF | |
| $M$ | Number of Monte Carlo paths | QF | Standard error $s/\sqrt{M}$ |
| $Z$ | Standard normal draw | QF | |
| $\varepsilon_1, \varepsilon_2$ | Independent standard normals before Cholesky correlation | — | |
| $h$ | Step in a finite difference | MP | |
| $V_i^j$ | Grid value at asset node $i$, time step $j$ | — | |
| $\text{SE}$ | Standard error | — | |

## Machine learning

| Symbol | Meaning | Used in | Notes |
|---|---|---|---|
| $\theta$ | Model parameters | — | |
| $J(\theta)$, $\mathcal{L}$ | Cost or loss function | — | |
| $\eta$ | Learning rate, $\theta \leftarrow \theta - \eta \nabla J(\theta)$ | — | |
| $\xi_i$ | Slack variables in a soft-margin SVM | — | |
| $\mathcal{S}, \mathcal{A}, P, r, \gamma$ | Markov decision process: states, actions, transitions, reward, discount factor | — | |
| $\pi_\theta$, $Q_\theta(s, a)$ | Policy; action-value function | — | |
| $\text{TP}, \text{FP}, \text{TN}, \text{FN}$ | Confusion matrix counts | — | |

## Overloaded symbols

The same letter means different things in different places.  Read the context.

| Symbol | Meanings |
|---|---|
| $\mathbb{Q}$ | Rational numbers; the risk-neutral measure.  (Plain $Q$: Black–Litterman views; eigenvector matrix; RL action value.) |
| $\mathbb{P}$ vs $P$ | $\mathbb{P}$ is the real-world measure; $P(A)$ is a probability; $P$ is a put price, a discount factor or the Black–Litterman pick matrix |
| $N$ | Standard normal CDF in pricing; the normal distribution in QF's $N(0, \Delta t)$; a count |
| $\phi$ | Standard normal PDF; a standard normal draw; $\pm 1$ call/put sign in QF |
| $\rho$ | Correlation; the Greek rho |
| $\Delta$ / $\delta$ | Option delta; a finite change $\Delta x$; a small increment $\delta t$; a constant diffusion; $\delta_{BS}$ |
| $\Pi$ | Hedged portfolio value; Black–Litterman equilibrium returns; portfolio subscript in $\sigma_\Pi$ |
| $\lambda$ | Eigenvalue; Lagrange multiplier; Poisson rate; risk aversion; APT factor premium |
| $\Lambda$ | Eigenvalue matrix; Radon–Nikodym derivative; exotic payoff |
| $\gamma$ / $\Gamma$ | Mean-reversion speed; GJR leverage; RL discount factor / option gamma |
| $\theta$ / $\Theta$ | Long-run mean; market price of risk; model parameters; a gamma scale / option theta |
| $\kappa$ | Mean-reversion speed; kurtosis; transaction cost rate |
| $\nu$ | Degrees of freedom; shares traded; a drift constant; a diffusion scale.  Vega is $\mathcal{V}$, never $\nu$ |
| $\tau$ | Time to expiry $T - t$; running time inside an integral; Black–Litterman scaling constant |
| $\alpha$, $\beta$ | Significance level; Jensen's alpha and market beta; GARCH coefficients; exponents in a PDE substitution; drift constant and mean-reversion speed; $\beta$ is also a power in a diffusion |
| $\psi$ | Uniform variates or a sampling density; a scaled normal draw $\sqrt{dt}\,\phi$ |
| $a$, $b$ | Polynomial coefficients; constant PDE coefficients; $a$ is also the base of $a^x$ and a constant inside an SDE solution |
| $u$, $v$ | Parts in integration by parts; unknown functions in a PDE; $u$ is also an up factor, an error term and a drift; $v$ is also a variance |
| $T$ | Expiry date; time to expiry in years (QF); sample length in time series |
| $r$ | Risk-free rate; short rate; a return $r_t$; the sample correlation in school statistics |
| $R$ | Return; annually compounded rate; correlation matrix |
| $V$ | Option value; long-run variance in GARCH.  Vega is $\mathcal{V}$ |
| $w$ | Portfolio weight; total implied variance; PDE unknown in a moving frame; a diffusion; a possible value of $W_t$ |
| $C$ | Call price; constant of integration; a matrix product; a constant SDE coefficient |
| $p$ / $c$ | Put premium; probability; risk-neutral up probability / call premium |
| $q$ | Dividend yield; position quantity; an arbitrary function of time; a helper function or integrand |
| $A$, $B$ | Matrices; events; drift and diffusion of an SDE, in either order |
| $F$, $G$ | CDF $F$; forward price $F_T$; functions in Itô's lemma; names of processes; $G$ is also an integrand |
| $J$ | Cost function; probability flux |
| $Z$ | Standard normal draw; a discount factor; a density process; the logarithm of a process |
| $h$, $k$ | Finite-difference step; small moves in a Taylor series; a test function $h(x)$; $k$ is also a gamma shape |
| $d$ | Down factor in a tree; differential in $dx$ |
| $S$, $K$ | Spot, strike; skewness and kurtosis inside the Jarque–Bera statistic |
| $i$ | Imaginary unit; an index |
| $'$ | Derivative $f'(x)$; transpose $w'$; complement $A'$ |

## Differences between repos

Where the repos write the same idea differently.  New work should follow the convention of the repo it lives in; this table is for translating between them.

| Idea | maths-python | quant-finance | Private notes |
|---|---|---|---|
| Time to expiry | — | $T$ (years) | $\tau = T - t$, with $T$ the expiry date |
| Brownian increment | $dW_t$ | $dW_t$ | $dW_t$, and $dX$ in the lecture notes |
| Small time step | $\Delta t$ | $\Delta t$ | $\delta t$ |
| Normal distribution | $\mathcal{N}(\mu, \sigma^2)$ | $N(0, \Delta t)$ | $\mathcal{N}(\mu, \sigma^2)$ |
| Normal PDF | $\phi(x)$, or $f(x)$ where $\phi$ is the random variable | $n(x)$ | $\phi(x)$ |
| Normal CDF | $\Phi(x)$ | $N(x)$ | $N(x)$, with $\Phi$ in statistics |
| Standard normal draw | $\phi$, $\phi_i$ | $Z$ | $\phi$, $\varepsilon$ |
| Transpose | $^\top$ | $^\top$ | $'$ and $^\top$ |
| Portfolio volatility | — | $\sigma_p$ | $\sigma_\Pi$ |
| Mean reversion (Vasicek) | — | — | $\gamma(\bar{r} - r)$ and $\kappa(\theta - r)$ |
| Inline maths delimiters | `$...$` | `\( \)` in docs, `$...$` in apps | `$...$` |
