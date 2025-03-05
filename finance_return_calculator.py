import streamlit as st

# Set up the app title
st.title("Finance Return Calculator")

# User input for principal amount
principal = st.number_input("Enter the principal amount (₹):", min_value=0.0, step=1.0)

# User input for rate of return
rate_of_return = st.number_input("Enter the annual rate of return (%):", min_value=0.0, step=0.1)

# User input for time period
time_period = st.number_input("Enter the time period (in years):", min_value=0, step=1)

# Calculate the total amount and returns
if st.button("Calculate"):
    if principal and rate_of_return and time_period:
        total_amount = principal * ((1 + rate_of_return / 100) ** time_period)
        returns = total_amount - principal
        
        # Display results
        st.success(f"Total Amount after {time_period} years: ₹{total_amount:,.2f}")
        st.info(f"Total Returns: ₹{returns:,.2f}")
    else:
        st.warning("Please fill in all inputs to calculate.")

# Add a footer
st.text("Createdc using Streamlit")
