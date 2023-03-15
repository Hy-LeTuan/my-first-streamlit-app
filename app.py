import streamlit as st
import sklearn
import pickle
import numpy as np

filename = "model.pickle"
model = pickle.load(open(filename, "rb"))

st.title("Revenue prediction")

temperature = np.array(st.number_input(label="Input temperature"))

temperature = temperature.reshape(-1, 1)

predict = st.button(label="Predict")

st.text("Revenue prediction")

if predict:
    revenue = model.predict(temperature)
    st.success(str(*revenue[0]))
