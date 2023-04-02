import streamlit as st

from data.SchedulePage import ScheduleElement, RecommendBar
from metrics.meta import meta_info


def main():
    meta_info()
    st.header("Last Day 💝")
    st.error("Souveniers & Hugs")

    info = ScheduleElement(
        text_path="texts/24_last_day.md",
        image_path="images/location_shopping.jpg",
        caption="Ala Moana Center the place to shop for souverniers",
    )
    info.show()

    return


if __name__ == "__main__":
    main()
