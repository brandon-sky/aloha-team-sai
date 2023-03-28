import streamlit as st
import streamlit.components.v1 as components
from Home import meta_info

def chapter(text_path: str, image_path: str| None = None, title:str|None = None, seprator: bool = True):
    with open(text_path, "r") as file:
        text = file.read()

    if title:
        st.info(title)
    if image_path:
        st.image(image_path)

    st.write(text)

    if seprator:
        st.markdown("---")
    return 


def main():
    meta_info()
    st.header("💞 Unsere Geschichte")
    st.error("Our Love story is told by our playlists...")
    
    chapter(text_path="texts/99_lovestory_intro.md", seprator=False)
    
    with st.expander("Playlist"):
        components.iframe(src="https://open.spotify.com/embed/playlist/2frESBFCpvRADuBGv8GnlM?utm_source=generator", height=500)
    chapter(text_path="texts/99_lovestory_2018.md", image_path="images/lovestory_nighthawks.jpg", title="2018 - Wir lernen uns kennen")
    chapter(text_path="texts/99_lovestory_2019.md", image_path="images/lovestory_moscow.jpg", title="2019 - Wir sind ein Paar")
    chapter(text_path="texts/99_lovestory_2020.md", image_path="images/lovestory_mover.png", title="2020 - Wir sind ziehen zusammen")
    chapter(text_path="texts/99_lovestory_2021.md", image_path="images/lovestory_parisiens.jpg", title="2021 - Wir sind verliebt")
    chapter(text_path="texts/99_lovestory_2022.md", image_path="images/lovestory_parisiens_2.jpg", title="2021 - Wir sind verlobt")
    return 


if __name__ == "__main__":
    main()
