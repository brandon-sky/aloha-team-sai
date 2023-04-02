import streamlit as st

from data.SchedulePage import ScheduleElement, RecommendBar
from metrics.meta import meta_info


def main():
    meta_info()
    st.header("We're going to Big Island ✈️")

    info = ScheduleElement(
        text_path="texts/17_big_island.md",
        image_path="images/location_big_island.jpg",
        caption="Big Island",
    )
    info.show()

    return


if __name__ == "__main__":
    main()
