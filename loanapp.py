
import streamlit as st
import pickle
import numpy as np

# ============================================================
# LOAD MODEL
# ============================================================

with open("/content/loan_model.pkl", "rb") as f:
    model = pickle.load(f)

# ============================================================
# LOAD SCALER
# ============================================================

with open("/content/loan_scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# ============================================================
# TITLE
# ============================================================

st.title("🏦 Loan Approval Prediction App")

st.write("Enter Applicant Details")

# ============================================================
# USER INPUTS
# ============================================================

# Gender

Gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

Gender = 1 if Gender == "Male" else 0


# Married

Married = st.selectbox(
    "Marital Status",
    ["No", "Yes"]
)

Married = 1 if Married == "Yes" else 0


# Dependents

Dependents = st.selectbox(
    "Number of Dependents",
    [0, 1, 2, 3]
)


# Education

Education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

Education = 0 if Education == "Graduate" else 1


# Self Employed

Self_Employed = st.selectbox(
    "Self Employed",
    ["No", "Yes"]
)

Self_Employed = 1 if Self_Employed == "Yes" else 0


# Applicant Income

ApplicantIncome = st.number_input(
    "Applicant Monthly Income",
    min_value=0
)


# Coapplicant Income

CoapplicantIncome = st.number_input(
    "Coapplicant Monthly Income",
    min_value=0
)


# Loan Amount

LoanAmount = st.number_input(
    "Loan Amount",
    min_value=0
)


# Loan Term

Loan_Amount_Term = st.number_input(
    "Loan Amount Term",
    min_value=0
)


# Credit History

Credit_History = st.selectbox(
    "Credit History",
    ["Bad", "Good"]
)

Credit_History = 1 if Credit_History == "Good" else 0


# Property Area

Property_Area = st.selectbox(
    "Property Area",
    ["Rural", "Semiurban", "Urban"]
)

if Property_Area == "Rural":
    Property_Area = 0

elif Property_Area == "Semiurban":
    Property_Area = 1

else:
    Property_Area = 2


# ============================================================
# PREPARE INPUT DATA
# ============================================================

features = np.array([[
    Gender,
    Married,
    Dependents,
    Education,
    Self_Employed,
    ApplicantIncome,
    CoapplicantIncome,
    LoanAmount,
    Loan_Amount_Term,
    Credit_History,
    Property_Area
]])

# ============================================================
# SCALE INPUT
# ============================================================

features = scaler.transform(features)

# ============================================================
# PREDICT BUTTON
# ============================================================

if st.button("Predict Loan Status"):

    result = model.predict(features)

    if result[0] == 1:

        st.success("✅ Loan Approved")

    else:

        st.error("❌ Loan Not Approved")
