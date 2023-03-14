import streamlit as st
from Home import meta_info

def wedding():
    with open("texts/11_wedding.md", "r") as file:
        text = file.read()
    st.error("Abfahrtpunkte und -zeiten der Shuttle-Busse werden hier aktualisiert.")
    st.header("The Wedding Day 👰🏻🤵🏽")
    st.write("Danke, dass ihr mit uns feiert.")
    st.image("images/loulu_palm_2.jpg", caption="Ceremony")
    schedule = [
        {"Zeit": "12:00 Uhr", "Aktivität": "Abfahrtort und -zeit des Shuttles"},
        {"Zeit": "14:00 Uhr", "Aktivität": "Eintreffen der Gäste LouluPalm"},
        {"Zeit": "14:30 Uhr", "Aktivität": "Zeremonie"},
        {"Zeit": "15:15 Uhr", "Aktivität": "Cheers to Love"},
        {"Zeit": "17:00 Uhr", "Aktivität": "It's time for dinner!"},
        {"Zeit": "20:00 Uhr", "Aktivität": "Party time!"},
        {"Zeit": "22:30 Uhr", "Aktivität": "Abfahrt zur After Party"}
    ]

    st.markdown(body=text)
    st.subheader("Schedule")
    st.table(schedule)
    st.image("images/loulu_palm.jpg", caption="Dinner & Entertainment.")
    return



def main():
    meta_info()
    wedding()
    return 

if __name__ == "__main__":
    main()