import streamlit as st

from metrics.meta import meta_info
from metrics.time_info import TimeBar
from metrics.headcount import HeadCounter
from metrics.locations import MapInformation
from metrics.weather import WeatherInfo

def main():
    meta_info(side_bar=True)

    st.image("images/kaneohe.jpg")

    with st.expander(label="Zeitinfo"):
        TimeBar()

    with st.expander(label="Wetter"):
        WeatherInfo()

    with st.expander(label="Where the Germans at?"):
        HeadCounter()

    with st.expander(label="Locations"):
        MapInformation()

    st.title("🌺 Aloha Famile & Freunde")
    st.markdown("""
    
    Wir freuen uns, dass ihr hier seid, um uns auf unserer Reise nach O'ahu, Hawaii zu begleiten.

    Hawaii ist ein wunderschönes Reiseziel und wir möchten euch mit Tipps und Empfehlungen unterstützen, 
    damit ihr eure Zeit auf der Insel so gut wie möglich genießen könnt. Auf unserer Website findet ihr auch einen Zeitplan für die Hochzeit und andere Aktivitäten, 
    die während unseres Aufenthalts auf Hawaii stattfinden werden.

    Wir sind überwältigt, dass so viele Menschen den Weg nach Hawaii auf sich nehmen, um uns an diesem besonderen Tag zu begleiten. 
    Wir freuen uns sehr darauf, diese unvergesslichen Erinnerungen mit euch zu teilen.

    Also, macht es euch gemütlich und erkundet die Website! 
    
    Wir können es kaum erwarten, euch auf Hawaii begrüßen zu dürfen. 

    Mahalo,   
    **Monika & Brandon**
    """)
    st.subheader("#AlohaTeamSai!")
    return


if __name__ == "__main__":
    main()
