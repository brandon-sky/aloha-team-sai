import streamlit as st


def meta_info(side_bar: bool = False):
    config = {
        "page_title": "#AlohaTeamSai",
        "page_icon": "🍍",
        "menu_items": {"About": "Lord have mercy. ChatGPT was the main contributor."},
    }
    if side_bar:
        config["initial_sidebar_state"] = "expanded"

    st.set_page_config(**config)
    st.warning("Update: Brandon landet erst am 8.April auf Hawai'i.")
    return
