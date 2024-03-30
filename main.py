import streamlit as st
# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
        "Upload": 0.002,#1gb=0.002tons CO2
        "Down": 0.002,#1gb=0.002 tons CO2
        "Delete": -0.001,#1gb=0.001 tons CO2
    }

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Green Carbon Calculator")

# Streamlit app code
st.title("Digital Carbon Calculator")
# User inputs
col1, col2 = st.columns(2)
with col1:
    st.subheader("Average Data Upload per day")
    upload = st.slider("Upload", 0.0, 100.0, key="upload_input")

    st.subheader("Average Data Download per day")
    download = st.slider("Download", 0.0, 100.0, key="download_input")
with col2:
    st.subheader("Average Data Deleted per day")
    delete = st.slider("Delete", 0.0, 100.0, key="delete_input")
# Normalize inputs
if upload > 0:
    upload= upload * 365  # Convert daily distance to yearly
if download > 0:
    download = download * 365  # Convert monthly electricity to yearly
if delete > 0:
    delete = delete * 365  # Convert weekly waste to yearly

# Calculate carbon emissions
upload_emissions = EMISSION_FACTORS["Upload"] * upload
download_emissions = EMISSION_FACTORS["Down"] * download
delete_emissions = EMISSION_FACTORS["Delete"] * delete

# Convert emissions to tonnes and round off to 2 decimal points
upload_emissions = round(upload_emissions, 2)
download_emissions = round(download_emissions, 2)
delete_emissions = round(delete_emissions, 2)

# Calculate total emissions
total_emissions = round(
    upload_emissions + download_emissions + delete_emissions, 2
)

if st.button("Calculate CO2 Emissions"):

    # Display results
    st.header("Results-:")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"⬆️ Uploaad: {upload_emissions} tonnes CO2 per year")
        st.info(f"⬇️ Download: {download_emissions} tonnes CO2 per year")
        st.info(f"🗑️ Delete: {delete_emissions} tonnes CO2 per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
        st.warning(f"To offset {total_emissions} amount of carbon emissions, it would require planting {round(total_emissions*40)} trees🌳.")

