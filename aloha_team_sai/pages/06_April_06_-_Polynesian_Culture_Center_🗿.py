import streamlit as st
from metrics.meta import meta_info

from data. SchedulePage import ScheduleElement, RecommendBar


def main():
    meta_info()
    st.header("Polynesian Culture Center 🗿")
    st.info("Die Welt des Südpazifik erleben.")

    ppc_info = ScheduleElement(text_path="texts/06_pcc.md", image_path="images/action_pcc.jpg",caption="Willkommen in der Welt des Südpazifiks")
    reco = RecommendBar(
        food=[("🌮", "Fish Tacos essen bei [North Shore Tacos](https://northshoretacos.com/)"),
              ("🍴", "Local Hawaiian Food bei [Papa Ole's Kitchen](https://northshoretacos.com/)")],
        actions=[("🗿", "Kultur erleben im [Polynesian Culture Center](https://polynesia.com/)")]
    )
    reco.show()
    ppc_info.show()
    st.warning("Hin- und Rückweg bieten sich für Nahrungsaufnahme an (:")
    st.image("images/action_pcc_3.jpg", caption="Auf dem Fluss fahren")
    st.image("images/action_pcc_4.png", caption="Haka Show")
    return 

if __name__ == "__main__":
    main()