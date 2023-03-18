import streamlit as st
from typing import Optional

from Home import meta_info

def post(path_text:str, path_picture:Optional[str] = None, caption: Optional[str] = None, title: Optional[str] = None) -> None:
    with open(file=path_text, mode="r") as file:
        text = file.read()

    if title is None:
        title = path_text.split("_")[1].split(".")[0].capitalize()
    st.subheader(body=title)
    if not path_picture is None:
        st.image(image=path_picture, caption=caption)
    st.markdown(body=text)
    return 

def main():
    meta_info()
    post(path_text="texts/food_intro.md")
    with st.expander(label="Erzeugnisse"):
        post(
            path_text="texts/food_schokolade.md", 
            path_picture="images/food_chocolate.png", 
            caption="Manoa Schokoladenvielfalt.")
        st.markdown("---")
        post(
            path_text="texts/food_kaffee.md", 
            path_picture="images/food_coffee.jpg", 
            caption="Lion Coffee mit Macadamia-Aroma.")
        st.markdown("---")
        post(
            path_text="texts/food_macadamia_nuts.md", 
            path_picture="images/food_macnuts.jpg", 
            caption="Deez (Glazed Mac) Nuts.")
        st.markdown("---")
        post(
            path_text="texts/food_früchte.md", 
            path_picture="images/food_hawaiian_fruits.jpg", 
            caption="Hawaiian Fruits.")
    
    with st.expander(label="Hawaiianische Gerichte"):
        post(
            path_text="texts/food_huli_huli_chicken.md",
            path_picture="images/food_huli_huli_chicken.jpg",
            caption="Some fine plate with huli huli chicken",
            title="Huli Huli Chicken")
        st.markdown("---")
        post(
            path_text="texts/food_kalua_pork.md",
            path_picture="images/food_kalua_pork.jpg",
            caption="Some fine plate with kalua pork",
            title="Kālua Pork")
        st.markdown("---")
        post(
            path_text="texts/food_lau_lau.md",
            path_picture="images/food_lau_lau.jpg",
            caption="Kohlrouladen, Yaprak sarma, Dolmadakia, Lau Lau - same same but different. ",
            title="Lau Lau")
        st.markdown("---")
        post(
            path_text="texts/food_lomi_lomi_salmon.md",
            path_picture="images/food_lomi_lomi_salmon.jpg",
            caption="Fresh. Fresh. Ya.",
            title="Lomi Lomi Salmon")

    
    return 

if __name__ == "__main__":
    main()