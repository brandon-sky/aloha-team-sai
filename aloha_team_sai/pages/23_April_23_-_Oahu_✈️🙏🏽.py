import streamlit as st

from data.SchedulePage import ScheduleElement, RecommendBar
from metrics.meta import meta_info


def main():
    meta_info()
    st.header("Goodbye Family 🙏🏽")
    st.info("Count your blessings.")

    info = ScheduleElement(
        text_path="texts/23_oahu.md",
        image_path="images/location_waikiki_sunset.jpg",
        caption="Sunset at Waikiki Beach",
    )
    info.show()

    return


if __name__ == "__main__":
    main()
