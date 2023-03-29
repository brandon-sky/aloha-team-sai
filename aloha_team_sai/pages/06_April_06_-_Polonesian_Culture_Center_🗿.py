import streamlit as st
from metrics.meta import meta_info



def pcc():
    with open("texts/06_pcc.md", "r") as file:
        text = file.read()

    st.header("Polonesian Culture Center 🗿")
    st.info("Die Welt des Südpazifik erleben.")
    with st.expander("Empfehlung"):
        st.markdown("""
        #### Essen
        - 🌮 [Fish Tacos](https://aloha-team-sai.de/Food) at [North Shore Tacos](https://northshoretacos.com/)
        - 🍱 [Hawaiian Food](https://aloha-team-sai.de/Food) at [Papa Ole's](https://www.facebook.com/people/Papa-Oles-Kitchen-LLC/100063494113364/)
        
        #### Landschaft/Aktivitäten
        - 🗿 [Polonesian Culture Center](https://polynesia.com/)


        """)
    st.image("images/action_pcc.jpg", caption="Willkommen in der Welt des Südpazifiks")
    st.markdown(body=text)
    st.warning("Hin- und Rückweg bieten sich für Nahrungsaufnahme an (:")
    st.image("images/action_pcc_3.jpg", caption="Auf dem Fluss fahren")
    st.image("images/action_pcc_4.png", caption="Haka Show")
    return

def main():
    meta_info()
    pcc()
    return 

if __name__ == "__main__":
    main()