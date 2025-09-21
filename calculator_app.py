import streamlit as st

# Set page configuration
st.set_page_config(page_title="Streamlit Calculator", page_icon="🧮")

st.title("🧮 Simple Streamlit Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Choose operation
operation = st.radio(
    "Choose an operation:",
    ("Add", "Subtract", "Multiply", "Divide")
)

# Calculate
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"The result of {num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"The result of {num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"The result of {num1} × {num2} = {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of {num1} ÷ {num2} = {result}")
        else:
            st.error("🚨 Division by zero is undefined!")