# Importing necessary libraries
import streamlit as st

# Streamlit app
def main():
    # Title
    st.title("Find the Largest Number")

    # Input for three numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Logic to find the largest number
    largest_num = max(num1, num2, num3)

    # Display the result
    st.write(f"The largest number is: {largest_num}")

if __name__ == "__main__":
    main()
