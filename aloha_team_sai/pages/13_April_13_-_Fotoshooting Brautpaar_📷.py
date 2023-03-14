import streamlit as st
from Home import meta_info

def photoshoot():
    with open("texts/13_photoshoot.md", "r") as file:
        text = file.read()

    st.header("Fotoshooting Brautpaar 📷")
    # st.write("Erinnerung: Für immer")
    st.markdown(body=text)
    st.image("images/alissa.jpg", caption="Quelle: Alissa Katharina Beer")
    # st.image("images/alissa_1.jpg", caption="Quelle: Alissa Katharina Beer")
    return

def main():
    meta_info()
    photoshoot()
    return 

if __name__ == "__main__":
    main()