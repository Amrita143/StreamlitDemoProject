import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App title
st.title('Graph Plotting App')

# User input
x_values = st.sidebar.slider('Select X range', 0.00, 100.00, (10.50, 50.50))
y_function = st.sidebar.selectbox('Select Y function', ['sin', 'cos', 'tan'])

st.write(f'Plotting {y_function}(x) from {x_values[0]} to {x_values[1]}')
# Generate data
x = np.linspace(x_values[0], x_values[1], 100)
if y_function == 'sin':
    y = np.sin(x)
elif y_function == 'cos':
    y = np.cos(x)
else:
    y = np.tan(x)

# Plot
plt.figure(figsize=(5, 3))
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
st.pyplot(plt)

