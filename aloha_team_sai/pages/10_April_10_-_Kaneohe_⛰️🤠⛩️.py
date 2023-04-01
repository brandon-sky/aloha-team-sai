import streamlit as st
from metrics.meta import meta_info

from data. SchedulePage import ScheduleElement, RecommendBar

def main():
    meta_info()
    st.header("Kane'ohe ⛰️🤠⛩️")
    st.info("Meine Westentasche...")
    info = ScheduleElement(text_path="texts/10_kaneohe.md", image_path="images/stairways_to_heaven_2.jpg", caption="Blick auf Kane'ohe von den Stairways the Heaven")
    reco = RecommendBar(
        food=[("🌭", "Hot Dogs"),
              ("🏖️","Sandy Beach"),
              ("📷","Lighthouse Makapu'u") ],
        actions=[("🚣🏽‍♂️ ", "Auf die Sandbank mit dem Kanu"),("⛰️ ", "Stairways to Heaven hochlaufen"),("📸 ", "Pali Aussichtsplattform"), ("⛩️ ", "Buddah Temple besuchen")]
    )
    reco.show()
    info.show()
    return 

if __name__ == "__main__":
    main()