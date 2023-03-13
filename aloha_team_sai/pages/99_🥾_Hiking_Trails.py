import streamlit as st

def trail_olomana():
    with open("texts/trail_olomana.md", "r") as file:
        text = file.read()

    st.title("Olomana")
    st.write("(Olo-Mana; Drei Berge)")
    st.image("images/olomana_entrance.jpg", caption="Olomana Startpunkt")
    st.markdown(body=text)
    st.image("images/olomana_peak.jpg", caption="Auf dem ersten Gipfel")
    return

def trail_pillbox():
    with open("texts/trail_pillbox.md", "r") as file:
        text = file.read()

    st.title("Lanikai Pillbox Hike")
    st.write("(Pillbox; ebenerdige Bunker)")
    st.image("images/pillbox.jpg", caption="Views.")
    st.markdown("""
    Dauer |	Länge |	Schwierigkeit |	Location
    ----- | ----- | ------------- | --------
    1 Stunde | 1,5 km |	leicht-mittel |	Lanikai, O'ahu
    """)
    st.markdown(body=text)
    return

def trail_haiku():
    with open("texts/trail_haiku.md", "r") as file:
        text = file.read()

    st.title("Stairways to Heaven")
    st.write("(Haiku Trail)")
    st.image("images/stairways_to_heaven.jpg", caption="Stairways to Heaven")
    st.markdown(body=text)
    st.image("images/stairways_to_heaven_3.jpg", caption="Auf dem Rückweg")
    return

def main():
    with st.expander(label="O'ahu - Olomana Hike (Jungle)"):
        trail_olomana()
    with st.expander(label="O'ahu - Pillbox Hike (Ocean View)"):
        trail_pillbox()
    with st.expander(label="O'ahu - Stairways to Heaven (Sunrise View)"):
        trail_haiku()
    return 

if __name__ == "__main__":
    main()