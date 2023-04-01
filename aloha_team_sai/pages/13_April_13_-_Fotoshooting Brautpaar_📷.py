import streamlit as st

from data.SchedulePage import ScheduleElement
from metrics.meta import meta_info


def main():
    meta_info()
    info = ScheduleElement(
        text_path="texts/13_photoshoot.md",
        image_path="images/alissa.jpg",
        caption="Quelle: Alissa Katharina Beer",
    )
    st.header("Fotoshooting Brautpaar 📷")
    info.show()


if __name__ == "__main__":
    main()
