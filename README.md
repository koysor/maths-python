# maths-python

An educational interactive web application that provides Python code snippets for mathematics and statistics. The application covers topics including calculus (differentiation and integration), stochastic calculus, linear algebra, and probability distributions. Each topic presents mathematical theory alongside executable Python code examples using libraries like SymPy, NumPy, SciPy, and Matplotlib.

Built with Streamlit, the application organises content into navigable pages where users can explore mathematical concepts through LaTeX-rendered equations and interactive visualisations. Users can adjust parameters with sliders and inputs to see how mathematical operations behave with different values, making it a useful reference for learning computational mathematics.

The codebase follows a modular architecture where each Python file in the `app/pages/` directory automatically becomes a page in the application. This makes it straightforward to add new mathematical topics by creating new page files following the established patterns.

## Key Technologies

### Symbolic and Numerical Computing

| Library          | Purpose                                                                                               |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| **SymPy**  | Computer algebra system for symbolic differentiation, integration, equation solving, and LaTeX output |
| **NumPy**  | Array operations, linear algebra, random number generation for numerical examples                     |
| **SciPy**  | Probability distributions, numerical integration, advanced linear algebra, special functions          |
| **pandas** | DataFrame structures for organising and presenting computational results                              |

### Visualisation

| Library              | Purpose                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------- |
| **Matplotlib** | Function plots, distribution visualisations, 3D surface plots for multivariable calculus |
| **Streamlit**  | Interactive web application with LaTeX rendering and parameter adjustment widgets        |

### Development Tools

| Tool                          | Purpose                                                |
| ----------------------------- | ------------------------------------------------------ |
| **JupyterLab / Marimo** | Interactive notebook environments for exploratory work |
| **pytest**              | Testing framework                                      |
| **Black / Ruff**        | Code formatting and linting                            |
| **pre-commit**          | Git hooks for automated code quality checks            |
| **NetworkX**            | Graph and network analysis for exploratory work        |

## Pre-commit Hooks

This repository uses [pre-commit](https://pre-commit.com/) to run code quality checks automatically before each commit.

### Setup

```bash
uv add pre-commit --dev  # Install pre-commit (already in dev dependencies)
uv run pre-commit install  # Install git hooks
```

### Configured Hooks

| Hook               | Purpose                                     |
| ------------------ | ------------------------------------------- |
| **black**          | Auto-formats Python code                    |
| **ruff**           | Lints Python code for common issues         |
| **detect-secrets** | Prevents secrets from being committed       |

### Usage

Hooks run automatically on `git commit`. To run manually:

```bash
uv run pre-commit run --all-files  # Run on all files
uv run pre-commit autoupdate       # Update hook versions
```

## Live Application

- **AWS EC2:** https://koysor.duckdns.org/maths/

## Docker Deployment

The application is containerised using Docker and deployed as part of a multi-container environment.

### Resource Limits

To ensure stability on resource-constrained environments (like AWS EC2 t2.micro), the following memory limits are enforced in production:

- **Memory Limit:** 180MB
- **Swap Limit:** 256MB

These limits prevent the application from consuming excessive system resources, which could impact other services on the same host.

### Local Build and Run

```bash
# Build the image
docker build -f docker/Dockerfile -t maths-python .

# Run the container
docker run -d -p 8505:8501 --name maths-python maths-python
```