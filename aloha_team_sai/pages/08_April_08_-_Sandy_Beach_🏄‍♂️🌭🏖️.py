import streamlit as st
from Home import meta_info

def sandys():
    with open("texts/08_sandys.md", "r") as file:
        text = file.read()

    st.header("Beach Day at Sandy's 🏄‍♂️🌭🏖️")
    st.info("Enjoy the day.")
    with st.expander("Empfehlung"):
        st.markdown("""
        #### Essen
        - 🌭 Hot Dogs  
        
        #### Landschaft/Aktivitäten
        - 🏖️ Sandy Beach
        - 📷 Lighthouse Makapu'u 


        """)
    st.image("images/sandys_2.jpg", caption="Sandy Beach.")
    st.markdown(body=text)
    st.image("images/sandys.jpg", caption="Die Gang.")
    st.image("images/hotdog.png", caption="Auch er konnte nicht das Preis/Leistungs-Verhältnis glauben.")
    return

def main():
    meta_info()
    sandys()
    return 

if __name__ == "__main__":
    main()