import streamlit as st

from data.SchedulePage import ScheduleElement, RecommendBar
from metrics.meta import meta_info


def main():
    meta_info()
    st.header("Star Gazing 🔭✨🛰️")
    st.success("Florida is the man for the gang!")

    info = ScheduleElement(
        text_path="texts/19_star_gazing.md",
        image_path="images/location_stars.jpg",
        caption="Klarer werdet ihr nie ins All schauen können",
    )
    info.show()

    return


if __name__ == "__main__":
    main()
