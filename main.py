import streamlit as st

# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
    "Upload": 0.002,  # 1 GB = 0.002 tons CO2
    "Down": 0.002,    # 1 GB = 0.002 tons CO2
    "Delete": -0.001  # 1 GB = 0.001 tons CO2
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Green Carbon Calculator")
image_path = r"https://github.com/mridul2139/Green_Carbon/blob/main/LOG-removebg-preview.png"  # Assuming the image is in the same directory as the script
st.image(image_path, width=175)
# Streamlit app code
st.title("Digital Carbon Calculator")

# User inputs
col1, col2 = st.columns(2)
with col1:
    st.subheader("Average Data Upload per day(GB)")
    upload = st.slider("Upload", 0.0, 100.0, key="upload_input")

    st.subheader("Average Data Download per day(GB)")
    download = st.slider("Download", 0.0, 100.0, key="download_input")
with col2:
    st.subheader("Average Data Deleted per day(GB)")
    delete = st.slider("Delete", 0.0, 100.0, key="delete_input")

# Normalize inputs
upload_yearly = upload * 365 if upload > 0 else 0
download_yearly = download * 365 if download > 0 else 0
delete_yearly = delete * 365 if delete > 0 else 0

# Calculate carbon emissions
upload_emissions = EMISSION_FACTORS["Upload"] * upload_yearly
download_emissions = EMISSION_FACTORS["Down"] * download_yearly
delete_emissions = EMISSION_FACTORS["Delete"] * delete_yearly

# Convert emissions to tonnes and round off to 2 decimal points
upload_emissions = round(upload_emissions, 2)
download_emissions = round(download_emissions, 2)
delete_emissions = round(delete_emissions, 2)

# Calculate total emissions
total_emissions = round(upload_emissions + download_emissions + delete_emissions, 2)

if st.button("Calculate CO2 Emissions"):
    # Display results
    st.header("Results-:")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"⬆️ Upload: {upload_emissions} tonnes CO2 per year")
        st.info(f"⬇️ Download: {download_emissions} tonnes CO2 per year")
        st.info(f"🗑️ Delete: {delete_emissions} tonnes CO2 per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
        st.warning(f"To offset {total_emissions} tonnes of carbon emissions, it would require planting {round(total_emissions * 100)} trees🌳.")

# Display the image in your Streamlit app

