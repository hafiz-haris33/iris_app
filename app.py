import streamlit as st
import pickle
import numpy as np

# Load trained model
with open('iris_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
st.title("🌸 Iris Flower Prediction App")
st.write("Enter flower measurements below:")

# Inputs
sepal_length = st.number_input("Sepal Length", 0.0, 10.0)
sepal_width = st.number_input("Sepal Width", 0.0, 10.0)
petal_length = st.number_input("Petal Length", 0.0, 10.0)
petal_width = st.number_input("Petal Width", 0.0, 10.0)

# Predict button
if st.button("Predict"):
    data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    result = model.predict(data)
    class_names = ['Setosa', 'Versicolor', 'Virginica']
    st.success(f"Prediction: {class_names[result[0]]}")