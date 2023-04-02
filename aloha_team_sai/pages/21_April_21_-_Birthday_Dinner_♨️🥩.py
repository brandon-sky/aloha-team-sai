import streamlit as st

from data.SchedulePage import ScheduleElement, RecommendBar
from metrics.meta import meta_info


def main():
    meta_info()
    st.header("Birthday Dinner ♨️🥩")
    st.success("Go, Go, Go Dome it's your birthday . . .")
    st.balloons()

    info = ScheduleElement(
        text_path="texts/21_dome_bbq.md",
        image_path="images/location_dome_cake.jpg",
        caption="Dies, das - Ananas. Alles Gute, ey!",
    )
    info.show()

    return


if __name__ == "__main__":
    main()
