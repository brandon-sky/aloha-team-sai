import streamlit as st
from metrics.meta import meta_info

from data. SchedulePage import ScheduleElement, RecommendBar

def main():
    meta_info()
    st.header("Get together at Sandy's 🏄‍♂️🌭🏖️")
    st.info("Lasst uns gemeinsam den Tag verbringen.")
    info = ScheduleElement(text_path="texts/09_sandys.md", image_path="images/sandys_2.jpg", caption="Sandy Beach.")
    reco = RecommendBar(
        food=[("🌭", "Hot Dogs"),
              ("🏖️","Sandy Beach"),
              ("📷","Lighthouse Makapu'u") ],
        actions=[("🏖️ ", "Waimea Beach ")]
    )
    reco.show()
    info.show()
    st.image("images/sandys.jpg", caption="Die Gang.")
    st.image("images/hotdog.png", caption="Auch er konnte nicht das Preis/Leistungs-Verhältnis glauben.")
    return 

if __name__ == "__main__":
    main()