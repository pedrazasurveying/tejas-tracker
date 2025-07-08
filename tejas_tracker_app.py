import streamlit as st
import pandas as pd
import pydeck as pdk
from geopy.geocoders import Nominatim
import os

os.environ["MAPBOX_API_KEY"] = "pk.eyJ1IjoicGVkcmF6YXN1cnZleWluZyIsImEiOiJjbWN0eDFveG8wOGhpMm1vdHkyeTNzemlkIn0.y-mIMtwv_f_L4-BB6aW9qw"

st.set_page_config(page_title="Tejas Project Tracker", layout="wide")
st.title("Tejas Surveying Project Tracker")

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

# Address search bar
search_term = st.text_input("🔍 Search an address to center the map")

default_view = {
    "latitude": data["lat"].mean(),
    "longitude": data["lon"].mean(),
    "zoom": 11
}

st.subheader("Project Locations")

st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v10",
    initial_view_state=pdk.ViewState(
        latitude=default_view["latitude"],
        longitude=default_view["longitude"],
        zoom=default_view["zoom"]
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=data,
            get_position='[lon, lat]',
            get_radius=100,
            get_fill_color='[255, 0, 0, 160]',
            pickable=True
        )
    ],
    tooltip={
        "html": "<b>{project_name}</b><br/>Type: {type}<br/>Client: {client}<br/>Year: {year}<br/><a href='{one_drive_link}' target='_blank'>📁 Files</a>",
        "style": {"backgroundColor": "gray", "color": "white"}
    }
))

if search_term:
    try:
        geolocator = Nominatim(user_agent="tejas_tracker")
        location = geolocator.geocode(search_term)
        if location:
            default_view["latitude"] = location.latitude
            default_view["longitude"] = location.longitude
            default_view["zoom"] = 14
        else:
            st.warning("Address not found.")
    except:
        st.error("Geocoding error. Try again later.")
        
# Table display
st.subheader("🗂️ Project Metadata")
st.dataframe(data.drop(columns=["lat", "lon"]))
