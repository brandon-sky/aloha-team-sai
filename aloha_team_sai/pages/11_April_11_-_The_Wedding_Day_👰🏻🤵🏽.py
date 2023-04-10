import streamlit as st
import pandas as pd

from metrics.meta import meta_info
from metrics.locations import MapInformation
from data.SchedulePage import ScheduleElement


def day_schedule():
    schedule = [
        {"Zeit": "12:00 Uhr", "Aktivität": "Abfahrtort und -zeit des Shuttles"},
        {"Zeit": "14:00 Uhr", "Aktivität": "Eintreffen der Gäste LouluPalm"},
        {"Zeit": "14:30 Uhr", "Aktivität": "Zeremonie"},
        {"Zeit": "15:15 Uhr", "Aktivität": "Cheers to Love"},
        {"Zeit": "17:00 Uhr", "Aktivität": "It's time for dinner!"},
        {"Zeit": "20:00 Uhr", "Aktivität": "Party time!"},
        {"Zeit": "22:30 Uhr", "Aktivität": "Abfahrt zur After Party"},
    ]
    st.subheader("Schedule")
    st.table(schedule)
    return


def bus_assignments():
    assignments = [
        {"Bus": "Kawika (Blau)", "Name": "Brandon"},
        {"Bus": "Kawika (Blau)", "Name": "Magdalena & René"},
        {"Bus": "Kawika (Blau)", "Name": "Gianmarco & Fabiana"},
        {"Bus": "Kawika (Blau)", "Name": "Stephanie & Dominique"},
        {"Bus": "Kawika (Blau)", "Name": "Anja & Ronny"},
        {"Bus": "Kawika (Blau)", "Name": "Mama Loraine"},
        {"Bus": "Kawika (Blau)", "Name": "Gabby"},
        {"Bus": "Kawika (Blau)", "Name": "Papa Andrzej"},
        {"Bus": "Kawika (Blau)", "Name": "Nick & Sinja"},
        {"Bus": "Kawika (Blau)", "Name": "André & Johanna"},
        {"Bus": "Kawika (Blau)", "Name": "Lina & Mia"},
        {"Bus": "Kawika (Blau)", "Name": "Alexander & Lena"},
        {"Bus": "Kiha (Grün)", "Name": "Kiha"},
        {"Bus": "Kiha (Grün)", "Name": "Anja & Ralf"},
        {"Bus": "Kiha (Grün)", "Name": "Natalie & Ioannis"},
        {"Bus": "Kiha (Grün)", "Name": "Melanie & Steffen"},
        {"Bus": "Kiha (Grün)", "Name": "Marcel & Selina"},
        {"Bus": "Kiha (Grün)", "Name": "Marissa & Tobias"},
        {"Bus": "Kiha (Grün)", "Name": "Jonas & Victoria"},
        {"Bus": "Kiha (Grün)", "Name": "Florian & Püppi"},
    ]
    df = pd.DataFrame(assignments)
    df = df.set_index(df["Name"])
    st.subheader("Bus")
    st.table(df[["Bus"]])
    return


def main():
    meta_info()
    st.header("The Wedding Day 👰🏻🤵🏽")
    info = ScheduleElement(
        text_path="texts/11_wedding.md",
        image_path="images/loulu_palm_2.jpg",
        caption="Ceremony",
    )
    info.show()
    MapInformation(path="database/bus.csv", zoom=15)
    bus_assignments()
    day_schedule()

    st.image("images/loulu_palm.jpg", caption="Dinner & Entertainment.")
    return


if __name__ == "__main__":
    main()
