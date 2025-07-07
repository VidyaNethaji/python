import streamlit as st
import pandas as pd
import os

st.title("🧵 Kaithari Nesavu - Customer Feedback Form")
st.write("We’d love to hear your thoughts! Please take a moment to answer these quick questions.")

# Define the CSV file path
csv_file = "feedback_data.csv"

# Question 1
q1 = st.radio(
    "1. How did you hear about Kaithari Nesavu?",
    ["Instagram", "Google Search", "Friend/Family", "Other"]
)

# Question 2
q2 = st.radio(
    "2. What do you love most about our sarees?",
    ["Quality & Fabric", "Design & Colors", "Traditional Touch", "Affordable Pricing"]
)

# Question 3
q3 = st.radio(
    "3. Which type of saree do you prefer the most?",
    ["Mul Cotton", "Silk Cotton", "Pure Silk", "Cotton Blend"]
)

# Question 4
q4 = st.radio(
    "4. How often do you purchase handloom or traditional sarees?",
    ["Once a month", "Every 3–6 months", "Once a year", "Rarely"]
)

# Question 5
q5 = st.radio(
    "5. Would you recommend Kaithari Nesavu to others?",
    ["Definitely", "Maybe", "Not sure", "No"]
)

# Submit button
if st.button("Submit"):
    # Create a new DataFrame row
    new_data = pd.DataFrame([{
        "Heard From": q1,
        "Love Most": q2,
        "Preferred Type": q3,
        "Purchase Frequency": q4,
        "Would Recommend": q5
    }])

    # Check if the file exists, then append or create
    if os.path.exists(csv_file):
        existing_data = pd.read_csv(csv_file)
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        updated_data = new_data

    # Save to CSV
    updated_data.to_csv(csv_file, index=False)

    st.success("🙏 Thank you for your valuable feedback!")
    st.balloons()
