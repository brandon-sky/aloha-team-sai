import streamlit as st

from data.SchedulePage import ScheduleElement, RecommendBar
from metrics.meta import meta_info


def main():
    meta_info()
    st.header("Easy Beach Day🌅🏖️")
    st.success("Wassup beaches?!")

    info = ScheduleElement(
        text_path="texts/18_beach_west.md",
        image_path="images/location_hapuna_beach.jpg",
        caption="Sunny-side up.",
    )
    info.show()

    return


if __name__ == "__main__":
    main()
