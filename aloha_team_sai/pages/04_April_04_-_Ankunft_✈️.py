import streamlit as st
from Home import meta_info

from data. SchedulePage import ScheduleElement, RecommendBar





def zippys():
    with st.expander("Empfehlung"):
        st.markdown("""
        #### Essen
        - 🍳 Loco Moco 
        - 🍱 Chicken Katsu 
        
        #### Landschaft/Aktivitäten
        - 🍽️ Essen genießen. 


        """)
    st.image("images/food_loco_moco.jpg", caption="Loco Moco - das leckerste Gericht")
    st.image("images/chicken_katsu.jpg", caption="Chicken Katsu, das zweitleckerste Gericht")
    return

def main():
    meta_info()

    st.header("Aloha Waikīkī 🤙🏽🏄🏽🌴")
    st.info("Für Touri-Spots muss man sich nicht schämen...")

    waikiki_info = ScheduleElement(
        text_path="texts/04_waikiki.md", 
        image_path="images/location_waikiki_duke.jpg", 
        caption="Statue von Duke Kahanamoku 3-Mal-Olympia-Sieger und Begründer des modernen Wellenreitens." )
    
    reco = RecommendBar(
        food=[("🍳", "Loco Moco essen"), ("🍱", "Chicken Katsu essen")],
        actions=[("🌴", "Waikīkī erkunden")])

    reco.show()
    waikiki_info.show()
    # zippys()



    return 

if __name__ == "__main__":
    main()