import streamlit as st
import mymodel as m

st.write("""
# Sales Model
Below is a sales prediction example for customers.
""")
window = st.slider("Forecast Window (days)")
st.write(m.run(window=window))
