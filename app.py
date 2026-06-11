import streamlit as st


# 1. Page Title
st.title("WELLCOME TO MY HOME PAGE")
st.write("Enter values and click the Calculate button.")


# 2. Input Form
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)


# 3. Arithmetic Operation Selection
operation = st.selectbox(
    "Select an operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
)


# 4. Calculate Button and Processing
if st.button("Calculate"):
    result = 0
    error_message = None


    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (×)":
        result = num1 * num2
    elif operation == "Division (÷)":
        if num2 != 0:
            result = num1 / num2
        else:
            error_message = "Error: Division by zero is not allowed!"


    # 5. Display Result
    if error_message:
        st.error(error_message)
    else:
        st.success(f"Result: {result}")