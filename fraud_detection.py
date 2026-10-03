import streamlit as st
import pandas as pd
import joblib
model = joblib.load("fraud_detection_model.pkl")
st.title("Fraud Detection Prediction App")
st.markdown("Please enter the transaction details and use the predict button to check if the transaction is fraudulent or not.")
st.divider()

transaction_type = st.selectbox("Transaction Type", ["CASH_OUT", "PAYMENT", "CASH_IN", "TRANSFER", "DEBIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0, step=100.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=1000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

if st.button("Predict"):

    balanceDiffDrig = oldbalanceOrg - newbalanceOrig
    balanceDiffDest = newbalanceDest - oldbalanceDest

    input_data = pd.DataFrame({
        "type": [transaction_type],
        "amount": [amount],
        "oldbalanceOrg": [oldbalanceOrg],
        "newbalanceOrig": [newbalanceOrig],
        "oldbalanceDest": [oldbalanceDest],
        "newbalanceDest": [newbalanceDest],
        "balanceDiffDrig": [balanceDiffDrig],
        "balanceDiffDest": [balanceDiffDest]
    })

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction Result: '{int(prediction)}'")

    if prediction == 1:
        st.error("The transaction is predicted to be fraudulent.")
    else:
        st.success("The transaction is predicted to be legitimate.")