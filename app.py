import streamlit as st
import sklearn
import plotly
import numpy as np

x = np.linspace(1, 5, 10)
y = np.linspace(1, 5, 100)
st.title("Giải phương trình bậc nhất")

a = st.number_input(label="Tham số a")
b = st.number_input(label="Tham số b")

solve = st.button(label="Giải")

if solve:
    result = round((-b / a), 2)
    st.success("Phương trình có 1 nghiệm : " + str(result))
