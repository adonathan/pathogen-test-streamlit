import streamlit as st
import pandas as pd

# Configure the Streamlit page
st.set_page_config(
    page_title="Pathogen Explorer",
    page_icon="🦠",
    layout="wide"
)

# Custom styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f9f9f9;
    }
    h1 {
        color: #2c3e50;
    }
    .stMarkdown {
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("🦠 Pathogen Contributing Factors Explorer")

# Load the Excel file
excel_file = "Pathogen test factors.xlsx"

try:
    df = pd.read_excel(excel_file, engine='openpyxl')

    # Display the uploaded data
    st.subheader("Pathogen Data")
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

except FileNotFoundError:
    st.error(f"Could not find the file '{excel_file}'. Please make sure it is in the same directory as this script.")
except Exception as e:
    st.error(f"An error occurred while loading the Excel file: {e}")
