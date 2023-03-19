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
        st.markdown("---")
        post(
            path_text="texts/food_luau_stew.md",
            path_picture="images/food_luau_stew.jpg",
            caption="Iss jetzt.",
            title="Luau Stew")
        st.markdown("---")
        post(
            path_text="texts/food_poi.md",
            path_picture="images/food_poi.jpg",
            caption="Von Grau bis Violett.")

    with st.expander(label="Lokale Gerichte"):
        st.write("""Dies sind natürlich auch hawaiianische Gerichte, 
                    doch im Gegensatz zu den vorherigen Gerichten, haben diese Gerichte einen Einfluss aus einer anderen Kultut. 
                    Diese Speisen sind ein Indiz das Hawai'i als Meltingpot des Pazifiks funktioniert. """
                 )
        post(
            path_text="texts/food_acai.md",
            path_picture="images/food_acai.jpg",
            caption="Fresh Acai Bowl from Haleiwa Bowls.",
            title="Acai Bowls")
        st.markdown("---")
        post(
            path_text="texts/food_chicken_long_rice.md",
            path_picture="images/food_chicken_long_rice.jpg",
            caption="Fine clean food.",
            title="Chicken Long Rice")
        st.markdown("---")
        post(
            path_text="texts/food_fish_tacos.md",
            path_picture="images/food_fish_tacos.jpg",
            caption="Yep tacos and fries.",
            title="Fish Tacos")
        st.markdown("---")
        post(
            path_text="texts/food_garlic_shrimp.md",
            path_picture="images/food_garlic_shrimp.jpg",
            caption="Nice plate of garlic shrimps from Giovanni's.",
            title="Garlic Shrimps")
        st.markdown("---")
        post(
            path_text="texts/food_loco_moco.md",
            path_picture="images/food_loco_moco.jpg",
            caption="Leibspeise.",
            title="Loco Moco")
        st.markdown("---")
        post(
            path_text="texts/food_mac_salad.md",
            path_picture="images/food_mac_salad.jpg",
            caption="Kühlende Beilage.",
            title="Mac Salad")
        st.markdown("---")
    return 

if __name__ == "__main__":
    main()