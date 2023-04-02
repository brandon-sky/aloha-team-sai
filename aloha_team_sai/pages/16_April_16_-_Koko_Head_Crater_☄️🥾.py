import streamlit as st

from data.SchedulePage import ScheduleElement, RecommendBar
from metrics.meta import meta_info


def main():
    meta_info()
    st.header("Koko Head Crater ☄️🥾")

    info = ScheduleElement(
        text_path="texts/16_heads.md",
        image_path="images/location_koko_head.jpg",
        caption="Koko Head Crater - über eine alte Gleisstrecke kann man hoch",
    )
    info.show()

    return


if __name__ == "__main__":
    main()
