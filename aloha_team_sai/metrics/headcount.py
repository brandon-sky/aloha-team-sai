import streamlit as st

# Define the presence on O'ahu, Maui and Kauai
oahu_presence = 0
maui_presence = 0
kauai_presence = 2
big_presence = 0

oahu_delta = 0
maui_delta = 0
kauai_delta = 2
big_delta = 0


def HeadCounter():
    # Display the presence on the three islands in one row
    st.write("🇩🇪 Germans on Hawai'i")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Kauai", value=kauai_presence, delta=kauai_delta)
    with col2:
        st.metric(label="O'ahu", value=oahu_presence, delta=oahu_delta)
    with col3:
        st.metric(label="Maui", value=maui_presence, delta=maui_delta)
    with col4:
        st.metric(label="Big Island", value=big_presence, delta=big_delta)
    
    st.image("images/map_islands.jpg")
    return 