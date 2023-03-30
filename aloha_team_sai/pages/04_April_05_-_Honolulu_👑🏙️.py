import streamlit as st
from metrics.meta import meta_info

from data. SchedulePage import ScheduleElement, RecommendBar


def main():
    meta_info()

    st.header("Honolulu 👑🏙️")
    st.info('In der hawaiischen Sprache bedeutet Honolulu „geschützte Bucht“.')

    hnl_info = ScheduleElement(
        text_path="texts/05_honolulu.md", 
        image_path="images/location_iolani_palace.jpg", 
        caption="Hawaii ist der einzige Bundesstaat, der sich mit Königspalästen rühmen kann, und Iolani ist der prächtigste von allen." )
    
    reco = RecommendBar(
        food=[("🍣", "Poke essen"), ("🥟", "Manapua essen")],
        actions=[("👑", "Iolani Palace besichtigen"), ("🇨🇳", "China Town")])

    reco.show()
    hnl_info.show()

    return 

if __name__ == "__main__":
    main()