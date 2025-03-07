import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("💰 Personal Finance Tracker")  
st.sidebar.header("Add a Transaction")  

category = st.sidebar.selectbox("Category", ["Income", "Food", "Transport", "Shopping", "Bills", "Other"])  
amount = st.sidebar.number_input("Amount ($)", min_value=0.0, format="%.2f")  
date = st.sidebar.date_input("Date")  

if st.sidebar.button("Add Transaction"):  
    st.success(f"Transaction Added: {category} - ${amount} on {date}")  

# Load or create transaction data  
try:
    df = pd.read_csv("transactions.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])

# Append new transaction  
if st.sidebar.button("Save Transaction"):
    new_data = pd.DataFrame({"Date": [date], "Category": [category], "Amount": [amount]})
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv("transactions.csv", index=False)
    st.sidebar.success("Transaction Saved!")

st.subheader("📜 Transaction History")  
st.dataframe(df)

st.subheader("📊 Expense Breakdown")  
if not df.empty:
    fig, ax = plt.subplots()
    df.groupby("Category")["Amount"].sum().plot(kind="pie", autopct="%1.1f%%", ax=ax)
    st.pyplot(fig)

