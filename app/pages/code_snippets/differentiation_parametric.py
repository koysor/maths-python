import streamlit as st
import sympy as sp

t = sp.symbols("t")
x = sp.sin(t) ** 2
y = 2 * sp.tan(t)

# Differentiate
dx_dt = sp.diff(x, t)
dy_dt = sp.diff(y, t)

st.write("The derivative of $$x$$ with respect to $$t$$ is:")
st.write(dx_dt)

st.write("The derivative of $$y$$ with respect to $$t$$ is:")
st.write(dy_dt)

st.write("The derivative of $$y$$ with respect to $$x$$ is:")
st.write(dy_dt / dx_dt)
