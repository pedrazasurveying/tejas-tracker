import streamlit as st
import pandas as pd
import pydeck as pdk
from geopy.geocoders import Nominatim

st.set_page_config(page_title="Tejas Project Tracker", layout="wide")
st.title("📍 Tejas Surveying Project Tracker")

data = pd.DataFrame([
    {
        "job_number": "44-2253",
        "project_name": "Triumph Christian Center",
        "client": "Connard Melton",
        "type": "Topographic Survey",
        "year": 2022,
        "address": "6601 FM 762 Rd, Richmond, TX",
        "lat": 29.537075,
        "lon": -95.758190,
        "one_drive_link": "https://onedrive.live.com/your-link-here"
    },
    {
        "job_number": "44-2516",
        "project_name": "Gutowsky 76 Acres",
        "client": "Momin Development",
        "type": "Topo + Boundary",
        "year": 2024,
        "address": "Bamore Rd & Klauke Rd, Rosenberg, TX",
        "lat": 29.540218,
        "lon": -95.783694,
        "one_drive_link": "https://onedrive.live.com/your-link-here"
    }
])

# Map display
st.subheader("📍 Project Locations")
st.map(data[["lat", "lon"]])

# Table display
st.subheader("🗂️ Project Metadata")
st.dataframe(data.drop(columns=["lat", "lon"]))
