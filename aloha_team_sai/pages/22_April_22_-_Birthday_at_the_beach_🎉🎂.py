import streamlit as st

from data.SchedulePage import ScheduleElement, RecommendBar
from metrics.meta import meta_info


def main():
    meta_info()
    st.header("Birthday at the beach 🎉🎂")
    st.success("Go, Go, Go Gianni it's your birthday . . .")
    st.balloons()

    info = ScheduleElement(
        text_path="texts/22_gianni_beach.md",
        image_path="images/location_gianni_beach.jpg",
        caption="Mmhhhh lecker. 'Happy Birthday, lo'",
    )
    info.show()

    return


if __name__ == "__main__":
    main()
