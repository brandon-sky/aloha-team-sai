import folium
import streamlit as st
import pandas as pd

from streamlit_folium import st_folium, folium_static

PATH = "metrics/locations.csv"

def MapInformation():
    df = pd.read_csv(PATH)

    hawaii_map = folium.Map(location=[df.latitude.mean(), df.longitude.mean()], 
                    zoom_start=10, control_scale=True)

    for _,row in df.iterrows():

        iframe = folium.IFrame(str(row["Title"]))
        popup = folium.Popup(iframe, min_width=150, max_width=150)
        icon = folium.Icon(color=row['color'], prefix='fa',icon=row['icon'])
        
        
        folium.Marker(
            location=[row['latitude'],row['longitude']],
            popup = popup, 
            c=row['Title'], 
            icon=icon
            ).add_to(hawaii_map)

    st_data = st_folium(hawaii_map, width=700)
    return 

