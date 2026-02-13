import streamlit as st

st.set_page_config(layout="wide")
st.markdown("### Parametric Integration")
st.markdown(
    """Parametric integration is the process of integrating a function that is defined in terms of one or more parameters.
    \nThis is often used in calculus to find the area under a curve or the length of a curve defined by parametric equations."""
)

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
