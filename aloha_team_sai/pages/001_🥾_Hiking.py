import streamlit as st
from metrics.meta import meta_info

def trail_olomana():
    with open("texts/trail_olomana.md", "r") as file:
        text = file.read()

    st.title("Olomana")
    st.write("(Olo-Mana; Drei Berge)")
    st.image("images/olomana_entrance.jpg", caption="Olomana Startpunkt")
    hike_data = [
        {
            "Location": "Kailua, O'ahu, Hawaii", 
            "Dauer": "2-4 Stunden", 
            "Länge": "9 km Hin- und Rückweg", 
            "Schwierigkeitsgrad": "Mittel-Schwer"},
    ]

    st.table(hike_data)
    st.markdown(body=text)
    st.image("images/olomana_peak.jpg", caption="Auf dem ersten Gipfel")
    return

def trail_pillbox():
    with open("texts/trail_pillbox.md", "r") as file:
        text = file.read()

    st.title("Lanikai Pillbox Hike")
    st.write("(Pillbox; ebenerdige Bunker)")
    st.image("images/pillbox_2.jpg", caption="Sunset.")
    hike_data = [
        {
            "Location": "Kailua, O'ahu, Hawaii", 
            "Dauer": "1-2 Stunden", 
            "Länge": "2 km (Hin- und Rückweg)", 
            "Schwierigkeitsgrad": "Leicht"},
    ]

    st.table(hike_data)
    st.markdown(body=text)
    st.image("images/pillbox.jpg", caption="Views.")
    return

def trail_haiku():
    with open("texts/trail_haiku.md", "r") as file:
        text = file.read()

    st.title("Stairways to Heaven")
    st.write("(Haiku Trail)")
    st.image("images/stairways_to_heaven.jpg", caption="Stairways to Heaven")
    hike_data = [
        {
            "Location": "Haiku, O'ahu, Hawaii", 
            "Dauer": "3-5 Stunden", 
            "Länge": "5 km Hin- und Rückweg", 
            "Schwierigkeitsgrad": "Mittelschwer"
        },
    ]

    st.table(hike_data)
    st.markdown(body=text)
    st.image("images/stairways_to_heaven_3.jpg", caption="Auf dem Rückweg")
    return

def trail_maunawili():
    with open("texts/trail_maunawili.md", "r") as file:
        text = file.read()

    st.title("Maunawili Falls Hike")
    # st.write("(Haiku Trail)")
    st.image("images/maunawili_falls.jpg", caption="Das Ende der Wanderung")
    hike_data = [
        {
            "Location": "Kailua, O'ahu, Hawaii", 
            "Dauer": "2-3 Stunden", 
            "Länge": "5 km Hin- und Rückweg", 
            "Schwierigkeitsgrad": "Mittel"},
    ]

    st.table(hike_data)
    st.markdown(body=text)
    st.image("images/maunawili_falls_2.jpg", caption="Mitten im Regenwald.")
    return

def trail_waimea():
    with open("texts/trail_waimea.md", "r") as file:
        text = file.read()

    st.title("Waimea Valley Falls Hike")
    # st.write("(Haiku Trail)")
    st.image("images/waimea_valley.jpg", caption="Das Ende der Wanderung")
    hike_data = [
        {
            "Location": "Waimea, O'ahu, Hawaii", 
            "Dauer": "1-2 Stunden", 
            "Länge": "1,5 km Hin- und Rückweg", 
            "Schwierigkeitsgrad": "Leicht"},
    ]

    st.table(hike_data)
    st.markdown(body=text)
    st.image("images/waimea_valley_2.jpg", caption="Übersicht")
    return

def main():
    meta_info()
    with st.expander(label="O'ahu - Olomana Hike (Jungle)"):
        trail_olomana()
    with st.expander(label="O'ahu - Pillbox Hike (Ocean View)"):
        trail_pillbox()
    with st.expander(label="O'ahu - Stairways to Heaven (Sunrise View)"):
        trail_haiku()
    with st.expander(label="O'ahu - Maunawili Falls Hike (Waterfall)"):
        trail_maunawili()
    with st.expander(label="O'ahu - Waimea Falls Hike (Culture / Waterfall)"):
        trail_waimea()
    return 

if __name__ == "__main__":
    main()