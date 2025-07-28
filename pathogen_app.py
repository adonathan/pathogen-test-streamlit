import streamlit as st
import pandas as pd

# Title of the app
st.title("Pathogen Contributing Factors Explorer")

# File uploader for Excel files
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file:
    # Read the Excel file using openpyxl engine
    df = pd.read_excel(uploaded_file, engine='openpyxl')

    # Display the uploaded data
    st.subheader("Uploaded Data")
    st.dataframe(df)

    # Ensure the first column contains pathogen names
    pathogen_names = df.iloc[:, 0].dropna().unique()
    selected_pathogen = st.selectbox("Select a pathogen", pathogen_names)

    # Extract the row corresponding to the selected pathogen
    row = df[df.iloc[:, 0] == selected_pathogen].iloc[0]

    # Get the contributing factor columns and their values
    factor_columns = df.columns[1:]
    factor_values = row[1:]

    # Categorize the factors
    primary_factors = [factor_columns[i] for i, val in enumerate(factor_values) if val == 1]
    secondary_factors = [factor_columns[i] for i, val in enumerate(factor_values) if val == 2]
    tertiary_factors = [factor_columns[i] for i, val in enumerate(factor_values) if val == 3]

    # Display the categorized factors
    st.subheader("Contributing Factors")
    st.markdown(f"**Primary Factors (1):** {', '.join(primary_factors) if primary_factors else 'None'}")
    st.markdown(f"**Secondary Factors (2):** {', '.join(secondary_factors) if secondary_factors else 'None'}")
    st.markdown(f"**Tertiary Factors (3):** {', '.join(tertiary_factors) if tertiary_factors else 'None'}")
else:
    st.info("Please upload an Excel file to begin.")
