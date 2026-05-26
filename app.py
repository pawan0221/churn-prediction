import streamlit as st
import pandas as pd
import joblib

model = joblib.load("churn_decision_tree.joblib")

st.set_page_config(page_title="Churn Predictor", page_icon="📡")
st.title("📡 Telecom Customer Churn Predictor")
st.markdown("Fill in the customer details below to predict if they will churn.")

col1, col2 = st.columns(2)
with col1:
    age = st.slider("Age", 18, 70, 35)
    usage_gb = st.number_input("Data Usage (GB)", 0.0, 50.0, 10.0)
    complaints = st.slider("Number of Complaints", 0, 5, 1)
with col2:
    tenure_months = st.slider("Tenure (months)", 1, 60, 12)
    plan_type = st.selectbox("Plan Type", ["Prepaid", "Postpaid"])

plan_enc = 1 if plan_type == "Postpaid" else 0
input_df = pd.DataFrame([[age, usage_gb, complaints, tenure_months, plan_enc]],
                        columns=["age","usage_gb","complaints","tenure_months","plan_type_enc"])

if st.button("🔍 Predict Churn"):
    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]
    if pred == 1:
        st.error(f"⚠️ This customer is likely to CHURN (Confidence: {prob:.0%})")
    else:
        st.success(f"✅ This customer is likely to STAY (Confidence: {1-prob:.0%})")
