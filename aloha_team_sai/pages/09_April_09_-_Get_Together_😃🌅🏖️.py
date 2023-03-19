import streamlit as st
from Home import meta_info

def waimea():
    with open("texts/09_waimea.md", "r") as file:
        text = file.read()

    st.header("Get Together 😃🌅🏖️")
    st.info("Wir treffen uns alle am Sunset Beach")
    with st.expander("Empfehlung"):
        st.markdown("""
        #### Essen
        - 🦐 Giovanni Shrimp Truck 
        
        #### Landschaft/Aktivitäten
        - 🏖️ Sunset Beach  


        """)
    st.image("images/sunset_beach.jpg", caption="Sunset Beach.")
    st.markdown(body=text)
    st.image("images/food_garlic_shrimp.jpg", caption="Giovanni's Shrimp Truck")
    return

def main():
    meta_info()
    waimea()
    return 

if __name__ == "__main__":
    main()