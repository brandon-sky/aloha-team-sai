import streamlit as st

from data.SchedulePage import ScheduleElement, RecommendBar
from metrics.meta import meta_info


def main():
    meta_info()
    st.header("Lava Wanderung 🌋")
    st.warning("Derzeit gibt es leider keine fließende Lava zu beobachten")

    info = ScheduleElement(
        text_path="texts/20_lava.md",
        image_path="images/location_lava.jpg",
        caption="Das Bild ist von Anfang des Jahres.",
    )
    info.show()

    return


if __name__ == "__main__":
    main()
