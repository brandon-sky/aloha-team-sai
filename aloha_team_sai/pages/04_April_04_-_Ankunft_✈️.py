import streamlit as st
from metrics.meta import meta_info

from data. SchedulePage import ScheduleElement, RecommendBar


def main():
    meta_info()

    st.header("Aloha Waikīkī 🤙🏽🏄🏽🌴")
    st.info("Für Touri-Spots muss man sich nicht schämen...")

    waikiki_info = ScheduleElement(
        text_path="texts/04_waikiki.md", 
        image_path="images/location_waikiki_duke.jpg", 
        caption="Statue von Duke Kahanamoku 3-Mal-Olympia-Sieger und Begründer des modernen Wellenreitens." )
    
    reco = RecommendBar(
        food=[("🍳", "Loco Moco essen"), ("🍱", "Chicken Katsu essen")],
        actions=[("🌴", "Waikīkī erkunden")])

    reco.show()
    waikiki_info.show()
    # zippys()



    return 

if __name__ == "__main__":
    main()