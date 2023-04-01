import streamlit as st

from data.SchedulePage import ScheduleElement

def main():
    with st.expander(label="Free Hula Shows"):
        hula_shows = ScheduleElement(text_path="texts/events_hula.md", image_path="images/events_hula.jpg", caption="Hula Show in Waikiki")
        hula_shows.show()
    return 


if __name__ == "__main__":
    main()