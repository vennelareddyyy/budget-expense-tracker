import streamlit as st

st.title("Personal Finance Analyzer")

income = st.number_input("Enter your monthly income", min_value=0)

st.subheader("Add an Expense")

expense_name = st.text_input("Expense name")
expense_amount = st.number_input("Expense amount", min_value=0)

if "expenses" not in st.session_state:
    st.session_state.expenses = []

if st.button("Add Expense"):
    st.session_state.expenses.append((expense_name, expense_amount))

st.subheader("Your Expenses")

total_expense = 0

for name, amount in st.session_state.expenses:
    st.write(name, "-", amount)
    total_expense += amount

remaining = income - total_expense

st.subheader("Remaining Balance")
st.write(remaining)