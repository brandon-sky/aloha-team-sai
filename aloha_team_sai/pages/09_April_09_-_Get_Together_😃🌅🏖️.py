import streamlit as st


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
    st.image("images/shrimps.jpg", caption="Giovanni's Shrimp Truck")
    return

def main():
    waimea()
    return 

if __name__ == "__main__":
    main()