import streamlit as st


def zippys():
    with open("texts/04_ankunft.md", "r") as file:
        text = file.read()

    st.header("Aloha ✈️")
    st.info("Ankommen und Hawai'i genießen")
    with st.expander("Empfehlung"):
        st.markdown("""
        #### Essen
        - 🍳 Loco Moco 
        - 🍱 Chicken Katsu 
        
        #### Landschaft/Aktivitäten
        - 🍽️ Essen genießen. 


        """)
    st.image("images/loco_moco.jpg", caption="Loco Moco - das leckerste Gericht")
    st.markdown(body=text)
    st.image("images/chicken_katsu.jpg", caption="Chicken Katsu, das zweitleckerste Gericht")
    return

def main():
    zippys()
    return 

if __name__ == "__main__":
    main()