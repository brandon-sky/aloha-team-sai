import streamlit as st


def kailua():
    with open("texts/12_kailua.md", "r") as file:
        text = file.read()

    st.header("The Hangover Plan 🕶️")
    st.info("Hangover Plan: Gutes Frühstück, strahlende Sonne, leckeres Eis und eine tolle Aussicht")
    with st.expander("Empfehlung"):
        st.markdown("""
        #### Essen
        - 🥞😊 Macademia Nut Panecakes 
        - 🍨🌈 Shave Ice
        
        #### Landschaft/Aktivitäten
        - 🏖️ Kailua Beach Park 
        - 🥾 Pillbox Hike
        """)
    st.image("images/kaili.jpg", caption="Easy day at Kailua Beach.")
    st.markdown(body=text)
    st.image("images/shave_ice.jpg", caption="Delicious shave ice.")
    return

def main():
    kailua()
    return 

if __name__ == "__main__":
    main()