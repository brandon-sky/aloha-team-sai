import streamlit as st
from metrics.meta import meta_info

from data. SchedulePage import ScheduleElement, RecommendBar


def main():
    meta_info()
    st.header("Hang Loose 🤙🏽")
    st.info("Today I don't feel like doing anything. . . 🎵")

    ppc_info = ScheduleElement(text_path="texts/07_hula_show.md", image_path="images/location_royal_hawaiian_center.jpg",caption="Musikalische Unterhaltung von Malu Nui im The Royal Grove.")
    reco = RecommendBar(
        food=[("🍴", "Die Fatboys Filiale in Waikiki [Alaea](https://fatboyshawaii.com/restaurants/alaea-waikiki/)"),
              ("😋", "Sicherlich gibt es auch hier ein [Zippy's](https://www.zippys.com/)")
              ],
        actions=[("📸", "Ein Show-Angebot wahrnehmen [Free Hula Shows](https://aloha-team-sai.de/Events)")]
    )
    reco.show()
    ppc_info.show()
    return 

if __name__ == "__main__":
    main()