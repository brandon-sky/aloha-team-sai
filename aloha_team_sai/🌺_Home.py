import streamlit as st

from data.SchedulePage import ScheduleElement
from metrics.meta import meta_info
from metrics.time_info import TimeBar
from metrics.headcount import HeadCounter
from metrics.locations import MapInformation
from metrics.weather import WeatherInfo


def main():
    meta_info(side_bar=True)

    st.image("images/kaneohe.jpg")
    st.title("🌺 Aloha Famile & Freunde")
    st.success("**#AlohaTeamSai**")
    info = ScheduleElement(text_path="texts/00_home.md")
    info.show()

    with st.expander(label="Zeitinfo"):
        TimeBar()

    with st.expander(label="Wetter"):
        WeatherInfo()

    with st.expander(label="Where the Germans at?"):
        HeadCounter()

    with st.expander(label="Locations"):
        MapInformation()

    return


if __name__ == "__main__":
    main()
